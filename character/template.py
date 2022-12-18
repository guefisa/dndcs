#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Template:
	def __init__(self):
		self.character_name = ""
		self.player_name = ""
		self.background = ""
		self.alignment = ""
		self.race = ""
		self._class = ""
		self.level = 1
		self.experience = 0

		self.strength = 0
		self.dexterity = 0
		self.constitution = 0
		self.intelligence = 0
		self.wisdom = 0
		self.charisma = 0

		self.inspiration = 0
		self.proficiency_bonus = 0

		self.saving_throws = {
			"strength": 0,
			"dexterity": 0,
			"constitution": 0,
			"intelligence": 0,
			"wisdom": 0,
			"charisma": 0
		}

		self.skills = {
			"acrobatics": 0,
			"animal_handling": 0,
			"arcana": 0,
			"athletics": 0,
			"deception": 0,
			"history": 0,
			"insight": 0,
			"intimidation": 0,
			"investigation": 0,
			"medicine": 0,
			"nature": 0,
			"perception": 0,
			"performance": 0,
			"persuasion": 0,
			"religion": 0,
			"sleight_of_hand": 0,
			"stealth": 0,
			"survival": 0,
		}

		self.perception = 0

		self.other_proficiencies = {}
		self.languages = []

		self.armor_class = 0
		self.initiative = 0
		self.speed = 0

		self.hit_point_maximum = 0
		self.current_hit_points = 0
		self.temporary_hit_points = 0
		self.hit_dice = 0

		self.attacks = []
		self.spellcasting = {}

		self.equipment = []

		self.personality_traits = []
		self.ideals = []
		self.bonds = []
		self.flaws = []
		self.features = []
