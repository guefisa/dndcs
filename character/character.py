#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json 
from . import Template

races = {
	'human': {
		'strength':1,
		'dexterity': 1,
		'constitution': 1,
		'intelligence': 1,
		'wisdom': 1,
		'charisma': 1,
		'speed': 30,
		'languages': ['Común',]
	},
	'elf': {
		'speed': 30,
		'languages': ['Común', 'Élfico'],
		'features': ["Visión en la Oscuridad: 60'", 'Linaje Feérico. Tienes ventaja en las tiradas salvación para evitar que te hechicen y la magia no puede dormirte.', 'Trance. Los elfos no necesitan dormir.'],
		'skills': {'perception': 2},
		'dexterity': 2
	},
	'dwarf': {
		'speed': 25,
		'languages': ['Común', 'Enano'],
		'features': ["Visión en la Oscuridad: 60'", 'Resistencia Enana', 'Afinidad con la Piedra'],
		'other_proficiencies': {
			'weapons': ['Hacha de guerra', 'Hacha de mano', 'Martillo de guerra', 'Martillo ligero'],
			},
		'constitution': 2
	},
	'halfling': {
		'speed': 25,
		'languages': ['Común', 'Mediano'],
		'features': ['Afortunado', 'Valiente', 'Agilidad del Mediano'],
		'dexterity': 2
	}
}

subraces = {
	'high_elf': {
		'other_proficiencies': {
			'weapons': ['Espada corta', 'Espada larga', 'Arco corto', 'Arco largo'],
			},
		'intelligence': 1
	},
	'forest_elf': {
		'speed': 5,
		'features': ['Máscara de la Naturaleza'],
		'other_proficiencies': {
			'weapons': ['Espada corta', 'Espada larga', 'Arco corto', 'Arco largo'],
			},
		'wisdom': 1
	},
	'hill_dwarf': {
		'hit_point_maximum': 1,
		'wisdom': 1
	},
	'mountain_dwarf': {
		'other_proficiencies': {
			'armors': ['Armadura ligera', 'Armadura mediana',],
			},
		'strength': 2
	},
	'stout': {
		'features': ['Resistencia de Fornido',],
		'constitution': 1
	},
	'lightfeet': {
		'features': ['Sigiloso por Naturaleza',],
		'charisma': 1
	},
}

classes = {
	'bard': {
		'hit_point_maximum': 8,
		'hit_dice': 8,
		'other_proficiencies': {
			'armors': ['Armadura ligera',],
			'weapons': ['Todas las armas sencillas', 'Ballesta de mano', 'Espada corta', 'Espada larga', 'Estoque'],
		},
		'saving_throws': {
			'dexterity': 2,
			'charisma': 2
		},
		'equipment': [
			'Armadura de cuero',
			'Daga',
		],
		'features': ['Inspiración Bárdica: 1d6',]
	},
	'cleric': {
		'hit_point_maximum': 8,
		'hit_dice': 8,
		'other_proficiencies': {
			'armors': ['Armadura ligera', 'Armadura media', 'Escudo'],
			'weapons': ['Todas las armas sencillas',],
		},
		'saving_throws': {
			'wisdom': 2,
			'charisma': 2
		},
		'equipment': [
			'Escudo',
			'Simbolo sagrado',
		],
	},
	'fighter': {
		'hit_point_maximum': 10,
		'hit_dice': 10,
		'other_proficiencies': {
			'armors': ['Todas las armaduras y escudos',],
			'weapons': ['Todas las armas sencillas', 'Todas las armas marciales'],
		},
		'saving_throws': {
			'strength': 2,
			'constitution': 2
		},
		'features': ['Tomar aliento: 1d10 + Nivel de guerrero',]
	},
	'wizard': {
		'hit_point_maximum': 6,
		'hit_dice': 6,
		'other_proficiencies': {
			'weapons': ['Ballesta ligera', 'Bastón', 'Daga', 'Dardo', 'Honda'],
		},
		'saving_throws': {
			'intelligence': 2,
			'wisdom': 2
		},
		'equipment': [
			'Libro de conjuros',
		],
	},
	'rogue': {
		'hit_point_maximum': 8,
		'hit_dice': 8,
		'other_proficiencies': {
			'armors': ['Armadura ligera',],
			'weapons': ['Todas las armas sencillas', 'Ballesta de mano', 'Espada corta', 'Espada larga', 'Estoque'],
			'tools': ['Herramientas de ladrón',]
		},
		'saving_throws': {
			'dexterity': 2,
			'intelligence': 2
		},
		'equipment': [
			'Armadura de cuero',
			'Dos dagas',
			'Herramientas de ladrón',
		],
		'features': ['Pericia','Ataque Furtivo', 'Jerga de Ladrones']
	},
}

simple_weapons_mele = ('Bastón','Clava','Daga','Gran clava','Hacha de mano','Hoz','Jabalina','Lanza','Martillo ligero','Maza')
simple_weapons_ranged = ('Arco corto','Ballesta ligera','Dardo','Honda')
martial_weapons_mele = ('Alabarda','Cimitarra','Espada corta','Espada larga','Estoque','Gran hacha','Guja','Hacha de guerra','Lanza de caballería','Látigo','Lucero del alba','Mandoble','Mangual','Martillo de guerra','Mazo de guerra','Pica','Pico de guerra','Tridente')
martial_weapons_ranged = ('Aguja de cerbatana','Arco largo','Ballesta de mano','Ballesta pesada', 'Red')

class Character(Template):
	def __init__(self):
		super().__init__()
		self.proficiency_bonus += 2

	def set_name(self, character_name):
		if character_name:
			self.character_name = character_name

	def set_race(self, race):
		if race:
			self.apply_race(race)

	def set_subrace(self, subrace):
		if subrace:
			self.apply_subrace(subrace)

	def set_class(self, _class):
		if _class:
			self.apply_class(_class)

	def set_domain(self, domain):
		if domain:			
			if domain == 'Dominio de la Guerra':
				proficiencies = {
					'other_proficiencies': {
						'armors': ['Armadura pesada',],
						'weapons': ['Todas las armas marciales',],
					},
				}
				self.add_dict(proficiencies)
				self.add_features([domain, 'Sacerdote guerrero. Cuando lleves acabo la acción de atacar durante tu turno, puedes emplear la accion adicional para hacer otro ataque con arma. Puedes emplear este rasgo una cantidad de veces igual a tu modificador de Sabiduria.'])

			elif domain == 'Dominio de la Vida':
				proficiencies = {
					'other_proficiencies': {
						'armors': ['Armadura pesada',],
					},
				}
				self.add_dict(proficiencies)
				self.add_features([domain, 'Discipulo de la vida. Tus conjuros de curación se vuelven más efectivos, (+3 puntos de golpe en conjuros de nivel 1)'])

	def set_abilities(self, strength, dexterity, constitution, intelligence, wisdom, charisma):
		self.strength += strength if strength else 0
		self.dexterity += dexterity if dexterity else 0
		self.constitution += constitution if constitution else 0
		self.intelligence += intelligence if intelligence else 0
		self.wisdom += wisdom if wisdom else 0
		self.charisma += charisma if charisma else 0

	def add_languages(self, languages):
		if languages:
			self.languages += languages

	def add_spells(self, range, spells):
		if spells:
			if self.spellcasting.get(range):
				self.spellcasting[range] += spells
			else:
				self.spellcasting[range] = spells

	def add_tools(self, tools):
		if tools:
			if self.other_proficiencies.get('tools'):
				self.other_proficiencies['tools'] += tools
			else:
				self.other_proficiencies['tools'] = tools

	def add_skills(self, skills):
		if skills:
			for skill in skills:
				self.skills[skill] += self.proficiency_bonus

	def add_features(self, features):
		if features:
			self.features += features

	def add_equipment(self, equipment):
		if equipment:
			self.equipment += [equipment,]

	def apply_race(self, race):
		self.race = race
		self.add_dict(races.get(race))

	def apply_subrace(self, subrace):
		self.race = subrace
		self.add_dict(subraces.get(subrace))

	def apply_class(self, _class):
		self._class = _class
		self.add_dict(classes.get(_class))

	def apply_expertise(self, skills):
		if skills:
			for skill in skills:
				if skill == 'thieves_tools':
					self.other_proficiencies['tools'] = [x for x in self.other_proficiencies['tools'] if x != "Herramientas de ladrón"]
					self.other_proficiencies['tools'] += ["Herramientas de ladrón: Percicia x2",]
				else:
					self.skills[skill] *= 2

	def apply_mods(self):
		self.hit_point_maximum += self.get_mod(self.constitution)

	def add_dict(self, target_dict):
		if target_dict:
			for property, value in target_dict.items():
				if isinstance(value, (int, list)):
					setattr(self, property, getattr(self, property) + value)

				if isinstance(value, dict):
					d1=getattr(self, property)
					d2=value
					for x, y in d2.items():
						if isinstance(y, list):
							for item in y:
								if d1.get(x):
									if item not in d1[x]:
										d1[x].append(item)
								else:
									d1[x] = [item]
						elif isinstance(y, int):
							if d1.get(x):
								d1[x]+=y
							else:
								d1[x]=y

					setattr(self, property, d1)

	def remove_duplication(self):
		if self.other_proficiencies.get('weapons'):
			if 'Todas las armas sencillas' in self.other_proficiencies['weapons']:
				for weapon in simple_weapons_mele + simple_weapons_ranged:
					if weapon in self.other_proficiencies['weapons']:
						self.other_proficiencies['weapons'].remove(weapon)

			if 'Todas las armas marciales' in self.other_proficiencies['weapons']:
				for weapon in martial_weapons_mele + martial_weapons_ranged:
					if weapon in self.other_proficiencies['weapons']:
						self.other_proficiencies['weapons'].remove(weapon)

		if self.other_proficiencies.get('armors'):
			if 'Todas las armaduras y escudos' in self.other_proficiencies['armors']:
				self.other_proficiencies['armors'] = ['Todas las armaduras y escudos',]

	def get_mod(self, value):
		mods = {  1:-5,
			2:-4, 3:-4,
			4:-3, 5:-3,
			6:-2, 7:-2,
			8:-1, 9:-1,
			10:0, 11:0,
			12:1, 13:1,
			14:2, 15:2,
			16:3, 17:3,
			18:4, 19:4,
			20:5, 21:5,
			22:6, 23:6,
			24:7, 25:7 }
		return mods.get(value)


	def __str__(self):
		return json.dumps(self, default=vars, ensure_ascii=False, indent=2).encode('utf8').decode()