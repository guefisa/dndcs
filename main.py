#!/usr/bin/env python
# -*- coding: utf-8 -*-


import streamlit as st
import base64
from character import Character

st.set_page_config(
	page_title="D&D Character creator",
	page_icon="馃",
	layout="wide",
	initial_sidebar_state="expanded"
)



choices_languages = (
	'Com煤n',
	'脡lfico',
	'Enano',
	'Gigante',
	'Gnomo',
	'Trasgo',
	'Mediano',
	'Orco',
	)

choices_wizard_spells_0 = (
	'Agarre electrizante',
	'Descarga de fuego',
	'Ilusi贸n menor',
	'Luces danzante',
	'Luz',
	'Mano de mago',
	'Prestidigitaci贸n',
	'Rayo de escarcha',
	'rociada venenosa',
	'Salpicadura 谩cida',
	)

choices_tools = (
	'Herramientas de artesano',
	'Herramientas de alba帽il',
	'Herramientas de alfarero',
	'Herramientas de carpintero',
	'Herramientas de cart贸grafo',
	'Herramientas de constructor',
	'Herramientas de herrero',
	'Herramientas de joyero',
	'Herramientas de peletero',
	'Herramientas de pintor',
	'Herramientas de soplador de vidrio',
	'Herramientas de tallador de madera',
	'Herramientas de tejedor',
	'Herramientas de zapatero'
	)

choices_skills = {
	'acrobatics':'Acrobacias',
	'animal_handling':'T. con Animales',
	'arcana':'C. Arcano',
	'athletics':'Atletismo',
	'deception':'Enga帽o',
	'history':'Historia',
	'insight':'Interpretaci贸n',
	'intimidation':'Intimidaci贸n',
	'investigation':'Investigaci贸n',
	'medicine':'Medicina',
	'nature':'Naturaleza',
	'perception':'Percepci贸n',
	'performance':'Perspicac铆a',
	'persuasion':'Persuasi贸n',
	'religion':'Religi贸n',
	'sleight_of_hand':'Juegos de Manos',
	'stealth':'Sigilo',
	'survival':'Supervivencia'
	}

choices_rogue_skills = {
	'acrobatics':'Acrobacias',
	'athletics':'Atletismo',
	'deception':'Enga帽o',
	'insight':'Interpretaci贸n',
	'intimidation':'Intimidaci贸n',
	'investigation':'Investigaci贸n',
	'perception':'Percepci贸n',
	'performance':'Perspicac铆a',
	'persuasion':'Persuasi贸n',
	'sleight_of_hand':'Juegos de Manos',
	'stealth':'Sigilo',
	}

choices_rogue_expertise = {
	'thieves_tools':'Herramientas de ladr贸n',
	'acrobatics':'Acrobacias',
	'athletics':'Atletismo',
	'deception':'Enga帽o',
	'insight':'Interpretaci贸n',
	'intimidation':'Intimidaci贸n',
	'investigation':'Investigaci贸n',
	'perception':'Percepci贸n',
	'performance':'Perspicac铆a',
	'persuasion':'Persuasi贸n',
	'sleight_of_hand':'Juegos de Manos',
	'stealth':'Sigilo',
	}

choices_wizard_skills = {
	'arcana':'C. Arcano',
	'history':'Historia',
	'investigation':'Investigaci贸n',
	'medicine':'Medicina',
	'performance':'Perspicac铆a',
	'religion':'Religi贸n'
	}

choices_fighter_skills = {
	'acrobatics':'Acrobacias',
	'animal_handling':'T. con Animales',
	'athletics':'Atletismo',
	'history':'Historia',
	'intimidation':'Intimidaci贸n',
	'perception':'Percepci贸n',
	'performance':'Perspicac铆a',
	'survival':'Supervivencia'
	}

choices_cleric_skills = {
	'history':'Historia',
	'medicine':'Medicina',
	'performance':'Perspicac铆a',
	'persuasion':'Persuasi贸n',
	'religion':'Religi贸n',
	}

choices_races = {None:'','elf':'Elfo', 'dwarf':'Enano', 'human':'Humano', 'halfling':'Mediano'}
choices_subraces = {
	'elf': {None:'','high_elf':'Alto elfo', 'forest_elf':'Elfo de los Bosques'}, 
	'dwarf': {None:'','hill_dwarf':'Enano de las Colinas', 'mountain_dwarf':'Enano de las monta帽as'}, 
	'halfling': {None:'','stout':'Fornido', 'light_feet':'Piesligeros'}
	}

choices_classes = {None:'','fighter':'Guerrero', 'bard':'Bardo', 'cleric':'Clerigo', 'wizard':'Mago', 'rogue':'P铆caro'}
choices_combat_styles = ('Combate con Armas a Dos Manos', 'Combate con Dos Armas', 'Defensa', 'Duelo', 'Protecci贸n', 'Tiro con Arco')
choices_musical_tools = ('Caramillo', 'Cuerno', 'Dulcimer', 'Flauta', 'Flauta de pan', 'Gaita', 'La煤d', 'Lira', 'Tambor', 'Viola')
choices_simple_weapons_mele = ('Bast贸n','Clava','Daga','Gran clava','Hacha de mano','Hoz','Jabalina','Lanza','Martillo ligero','Maza')
choices_simple_weapons_ranged = ('Arco corto','Ballesta ligera','Dardo','Honda')
choices_bard_spells_0 = ('Burla da帽ina', 'Ilusi贸n menor', 'Luz', 'Mano de mago', 'Presidigitaci贸n', 'Reparar')
choices_bard_spells_1 = ('Ca铆da de pluma','Curar heridas','Detectar magia (ritual)','Disfrazarse','Dormir','Entender idiomas (ritual)','Fuego fe茅rico','Hechizar persona','Identificar (ritual)','Imagen silenciada','Ola atronadora','Palabra de curaci贸n','Zancada prodigiosa')
choices_cleric_spells_0 = ('Gu铆a','Llama sagrada','Luz','Reparar','Resistencia','Taumaturg铆a')
choices_cleric_spells_1 = ('Bendici贸n','Curar heridas','Detectar magia (ritual)','Escudo de fe','Infllingir heridas','Orden imperiosa','Palabra de curaci贸n','Saeta gu铆a', 'Santuario')
choices_wizard_spells_0 = (
	'Agarre electrizante (evocaci贸n)',
	'Descarga de fuego (evocaci贸n)',
	'Ilusi贸n menor (ilusionismo)',
	'Luces danzantes (evocaci贸n)',
	'Luz (evocaci贸n)',
	'Mano de mago (conjuraci贸n)',
	'Prestidigitaci贸n (trasmutaci贸n)',
	'Rayo de escarcha (evocaci贸n)',
	'Rociada venenosa (conjuraci贸n)',
	'Salpicadura 谩cida (conjuraci贸n)'
	)
choices_wizard_spells_1 = (
	'Armadura de mago (abjuraci贸n)',
	'Ca铆da de pluma (trasmutaci贸n)',
	'Detectar magia (adivinaci贸n, ritual)',
	'Disfrazarse (ilusionismo)',
	'Dormir (encantamiento)',
	'Entender idiomas (adivinaci贸n, ritual)',
	'Escudo (abjuraci贸n)',
	'Hechizar persona (encantamiento)',
	'Identificar (adivinaci贸n, ritual)',
	'Imagen silenciosa (ilusionismo)',
	'Manos ardientes (evocaci贸n)',
	'Ola atronadora (evocaci贸n)',
	'Poyectil m谩gico (evocaci贸n)',
	'Zancada prodigiosa (trasmutaci贸n)'
	)

def main():
	with st.sidebar:
		name = st.text_input('Nombre del personaje', '')
		level = st.text_input('Nivel', 1, disabled=True)
		race = st.selectbox("Raza", choices_races.keys(), format_func=lambda x:choices_races[x])
		subrace = st.selectbox("Subraza", choices_subraces[race].keys(), format_func=lambda x:choices_subraces[race][x]) if race in choices_subraces.keys() else None
		_class = st.selectbox('Clase', choices_classes.keys(), format_func=lambda x:choices_classes[x])

		st.markdown("""---""") 
		strength = st.slider('Fuerza', 1, 18, 10)
		dexterity = st.slider('Destreza', 1, 18, 10)
		constitution = st.slider('Constituci贸n', 1, 18, 10)
		intelligence = st.slider('Inteligencia', 1, 18, 10)
		wisdom = st.slider('Sabiduria', 1, 18, 10)
		charisma = st.slider('Carisma', 1, 18, 10)

		# Race choices
		st.markdown("""---""") 
		human_extra_languages = [st.selectbox("Idioma extra", ['',] + [x for x in choices_languages if x != "Com煤n"]),] if race == 'human' else None
		high_elf_extra_languages = [st.selectbox("Idioma extra", ['',] + [x for x in choices_languages if x not in ["Com煤n", "脡lfico"]]),] if subrace == 'high_elf' else None
		high_elf_extra_spells = [st.selectbox("Truco de mago",  ('',) + choices_wizard_spells_0),] if subrace == 'high_elf' else None
		dwarf_extra_tools = [st.selectbox("Competencia con una herramienta", ('',) + choices_tools),] if race == 'dwarf' else None

		# Class choices
		st.markdown("""---""") 
		bard_tools = st.multiselect('Competencia con instrumentos', choices_musical_tools, max_selections=3) if _class == 'bard' else None
		bard_skills = st.multiselect('Habilidades', choices_skills.keys(), format_func=lambda x:choices_skills[x], max_selections=3) if _class == 'bard' else None
		bard_equip1 = st.selectbox('Equipamiento, arma', ('','Estoque', 'Espada larga',) + choices_simple_weapons_mele + choices_simple_weapons_ranged) if _class == 'bard' else None
		bard_equip2 = st.selectbox('Equipamiento, paquete', ('', 'Paquete de diplom谩tico', 'Paquete de artista')) if _class == 'bard' else None
		bard_equip3 = st.selectbox('Equipamiento, intrumento', ('',) + choices_musical_tools) if _class == 'bard' else None
		bard_spells_0 = st.multiselect('Trucos de bardo', choices_bard_spells_0, max_selections=2) if _class == 'bard' else None
		bard_spells_1 = st.multiselect('Conjuros de bardo de nivel 1', choices_bard_spells_1, max_selections=4) if _class == 'bard' else None

		cleric_skills = st.multiselect('Habilidades', choices_cleric_skills.keys(), format_func=lambda x:choices_cleric_skills[x], max_selections=2) if _class == 'cleric' else None
		cleric_equip1 = st.selectbox('Equipamiento, arma', ('', 'Maza', 'Martillo de guerra')) if _class == 'cleric' else None
		cleric_equip2 = st.selectbox('Equipamiento, armadura', ('', 'Cota de escamas', 'Armadura de cuero', 'Cota de malla')) if _class == 'cleric' else None
		cleric_equip3 = st.selectbox('Equipamiento, arma secundaria', ('', 'Ballesta ligera y 20 virotes',) + choices_simple_weapons_mele) if _class == 'cleric' else None
		cleric_equip4 = st.selectbox('Equipamiento, paquete', ('', 'Paquete de sacerdote', 'Paquete de explorador')) if _class == 'cleric' else None
		cleric_spells_0 = st.multiselect('Trucos de cl茅rigo', choices_cleric_spells_0, max_selections=3) if _class == 'cleric' else None
		cleric_spells_1 = st.multiselect('Conjuros de cl茅rigo de nivel 1', choices_cleric_spells_1, max_selections=2) if _class == 'cleric' else None
		cleric_domain = st.selectbox('Dominios divinos', ('','Dominio de la Guerra', 'Dominio de la Vida')) if _class == 'cleric' else None

		fighter_skills = st.multiselect('Habilidades', choices_fighter_skills.keys(), format_func=lambda x:choices_fighter_skills[x], max_selections=2) if _class == 'fighter' else None
		fighter_combat_style = [st.selectbox('Estilo de combate', ('',) + choices_combat_styles),] if _class == 'fighter' else None
		fighter_equip1 = st.selectbox('Equipamiento', ('', 'Cota de malla', 'Armadura de cuero, arco largo y 20 flechas')) if _class == 'fighter' else None
		fighter_equip2 = st.selectbox('Equipamiento', ('', 'Un arma marcial y un escudo', 'Dos armas marciales', 'Cota de malla')) if _class == 'fighter' else None
		fighter_equip3 = st.selectbox('Equipamiento, arma secundaria', ('', 'Una ballesta ligera y 20 virotes','dos hachas de mano')) if _class == 'fighter' else None
		fighter_equip4 = st.selectbox('Equipamiento, paquete', ('', 'Paquete de explorador de mazmorras', 'Paquete de explorador')) if _class == 'fighter' else None

		wizard_skills = st.multiselect('Habilidades', choices_wizard_skills.keys(), format_func=lambda x:choices_wizard_skills[x], max_selections=2) if _class == 'wizard' else None
		wizard_equip1 = st.selectbox('Equipamiento, arma', ('','Bast贸n', 'Daga',)) if _class == 'wizard' else None
		wizard_equip2 = st.selectbox('Equipamiento, componentes', ('', 'Un saquito de componentes', 'Un canalizador arcano')) if _class == 'wizard' else None
		wizard_equip3 = st.selectbox('Equipamiento, paquete', ('','Un paquete de erudito', 'Un paquete de explorador') ) if _class == 'wizard' else None
		wizard_spells_0 = st.multiselect('Trucos de mago', choices_wizard_spells_0, max_selections=3) if _class == 'wizard' else None
		wizard_spells_1 = st.multiselect('Conjuros de mago de nivel 1', choices_wizard_spells_1, max_selections=6) if _class == 'wizard' else None

		rogue_skills = st.multiselect('Habilidades', choices_rogue_skills.keys(), format_func=lambda x:choices_rogue_skills[x], max_selections=4) if _class == 'rogue' else None
		rogue_equip1 = st.selectbox('Equipamiento, arma', ('','Un estoque', 'Una espada corta',)) if _class == 'rogue' else None
		rogue_equip2 = st.selectbox('Equipamiento, arma secundaria', ('', 'Un arco corto y una aljaba de 20 flechas', 'Una espada corta')) if _class == 'rogue' else None
		rogue_equip3 = st.selectbox('Equipamiento, paquete', ('','Un paquete de ladr贸n', 'Un paquete de explorador') ) if _class == 'rogue' else None
		rogue_expertise = st.multiselect('Pericia',  choices_rogue_expertise.keys(), format_func=lambda x:choices_rogue_expertise[x], max_selections=2) if _class == 'rogue' else None

	character = Character()
	character.set_name(name)
	character.set_race(race)
	character.set_subrace(subrace)
	character.set_class(_class)

	character.set_abilities(
		strength,
		dexterity,
		constitution,
		intelligence,
		wisdom,
		charisma)

	# Race
	character.add_languages(human_extra_languages)
	character.add_languages(high_elf_extra_languages)
	character.add_spells(0, high_elf_extra_spells)
	character.add_tools(dwarf_extra_tools)
	
	# Bard
	character.add_tools(bard_tools)
	character.add_skills(bard_skills)
	character.add_equipment(bard_equip1)
	character.add_equipment(bard_equip2)
	character.add_equipment(bard_equip3)
	character.add_spells(0, bard_spells_0)
	character.add_spells(1, bard_spells_1)

	# Cleric
	character.add_skills(cleric_skills)
	character.add_equipment(cleric_equip1)
	character.add_equipment(cleric_equip2)
	character.add_equipment(cleric_equip3)
	character.add_equipment(cleric_equip4)
	character.add_spells(0, cleric_spells_0)
	character.add_spells(1, cleric_spells_1)
	character.set_domain(cleric_domain)

	# Fighter
	character.add_skills(fighter_skills)
	character.add_features(fighter_combat_style)
	character.add_equipment(fighter_equip1)
	character.add_equipment(fighter_equip2)
	character.add_equipment(fighter_equip3)
	character.add_equipment(fighter_equip4)

	# Wizard
	character.add_skills(wizard_skills)
	character.add_equipment(wizard_equip1)
	character.add_equipment(wizard_equip2)
	character.add_equipment(wizard_equip3)
	character.add_spells(0, wizard_spells_0)
	character.add_spells(1, wizard_spells_1)

	# Rogue
	character.add_skills(rogue_skills)
	character.add_equipment(rogue_equip1)
	character.add_equipment(rogue_equip2)
	character.add_equipment(rogue_equip3)
	character.apply_expertise(rogue_expertise)

	# Others
	character.apply_mods()
	character.remove_duplication()


	file_path = './pdf/dnd_5e_charactersheet.pdf'
	with open(file_path,"rb") as f:
		base64_pdf = base64.b64encode(f.read()).decode('utf-8')

	pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="820" height="1200" type="application/pdf"></iframe>'
	st.markdown(pdf_display, unsafe_allow_html=True)

	# result = st.json(character.__str__())
	st.code(character.__str__(), language="json")


if __name__ == "__main__":
	main()