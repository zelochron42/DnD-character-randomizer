import random
import time

#module for generating random character ideas in DnD 5e

#run randomChar for a random race, class, subclass and alignment
#run randomCharNature to generate a character along with a random Pokemon nature
#run batch_generate(n) to generate n random characters


class char_class:
    name = "class"
    combinator = ", "
    sub_classes = []
    def __init__(self, classname, combinator, *subclasses):
        self.name = classname
        self.combinator = combinator
        self.sub_classes = subclasses

#class formatting: name, combinator, subclasses
#example: "Artificer, ", ", "Alchemist" becomes "Artificer, Alchemist"
artificer = char_class("Artificer", ", ", "Alchemist", "Armorer", "Artillerist", "Battle Smith")
barbarian = char_class("Barbarian", ", primal path of ", "the Berserker", "the Totem Warrior", "the Beast", "Wild Magic", "the Ancestral Guardian", "the Storm Herald ", "the Zealot")
bard = char_class("Bard", ", College of ", "Lore", "Valor", "Creation", "Eloquence", "Glamour", "Swords", "Whispers")
cleric = char_class("Cleric", ", Divine Domain of ", "Knowledge", "Life", "Light", "Nature", "Tempest", "Trickery", "Order", "Peace", "Twilight", "Forge", "Grave")
druid = char_class("Druid", ", circle of ", "the Moon", "the Land", "Spores", "Stars", "Wildfire", "Dreams", "the Shepherd")
fighter = char_class("Fighter", ", ", "Champion", "Battle Master", "Eldritch Knight", "Psi Warrior", "Rune Knight", "Arcane Archer", "Samurai")
monk = char_class("Monk", ", way of ", "the Open Hand", "Shadow", "the Four Elements", "Mercy", "the Astral Self", "the Drunken Master", "the Kensei", "the Sun Soul")
paladin = char_class("Paladin", ", Sacred Oath of ", "Devotion", "the Ancients", "Vengeance", "Glory", "the Watchers", "Conquest", "Redemption")
ranger = char_class("Ranger", ", ", "Hunter", "Beast Master", "Fey Wanderer", "Swarmkeeper", "Gloom Stalker", "Horizon Walker", "Monster Slayer")
rogue = char_class("Rogue", ", ", "Thief", "Assassin", "Arcane Trickster", "Phantom", "Soulknife", "Inquisitive", "Mastermind", "Scout")
sorcerer = char_class("Sorcerer", ", ", "Draconic Bloodline", "Wild Magic", "Aberrant Mind", "Clockwork Soul", "Divine Soul", "Shadow Magic", "Storm Sorcery")
warlock = char_class("Warlock", ", pact of the ", "Archfey", "Fiend", "Great Old One", "Fathomless", "Genie", "Celestial", "Hexblade")
wizard = char_class("Wizard", ", school of ", "Abjuration", "Conjuration", "Divination", "Enchantment", "Evocation", "Illusion", "Necromancy", "Transmutation", "Bladesinging", "Scribes", "War Magic")

charclasses = [artificer, barbarian, bard, cleric, druid, fighter, monk, paladin, ranger, rogue, sorcerer, warlock, wizard]

def randomClass():
    return charclasses[random.randrange(0, len(charclasses))]

def randomSubClass():
    rc = randomClass()
    return rc.name + rc.combinator + rc.sub_classes[random.randrange(0, len(rc.sub_classes))]


multiclass_rarity = 10
def randomMultiClass():
    rc1 = randomClass()
    rc2 = randomClass()
    while rc2 == rc1:
        rc2 = randomClass()
    return rc1.name + "-" + rc2.name

class char_race:
    name = "race"
    sub_races = []
    def __init__(self, racename, *subraces):
        self.name = racename
        self.sub_races = subraces

#Player Handbook
dwarf = char_race("Dwarf", "Hill", "Mountain", "!Duergar")
elf = char_race("Elf", "High", "Wood", "Dark", "Sea", "!Shadar-Kai", "Astral")
halfling = char_race("Halfling", "Lightfoot", "Stout")
human = char_race("Human", "Calishite", "Chondathan", "Damaran", "Illuskan", "Mulan", "Rashemi", "Shou", "Tethyrian", "Turami")
dragonborn = char_race("Dragonborn", "Black", "Blue", "Brass", "Bronze", "Copper", "Gold", "Green", "Red", "Silver", "White")
gnome = char_race("Gnome", "Forest", "Rock", "Deep")
half_elf = char_race("Half-Elf")
half_orc = char_race("Half-Orc")
tiefling = char_race("Tiefling")

#Mordenkainen's Monsters of the Multiverse
aarakocra = char_race("Aarakocra")
aasimar = char_race("?Aasimar", "Fallen")
bugbear = char_race("Bugbear")
centaur = char_race("Centaur")
changeling = char_race("Changeling")
eladrin = char_race("Eladrin")
fairy = char_race("Fairy")
firbolg = char_race("Firbolg")
genasi = char_race("Genasi", "Air", "Earth", "Fire", "Water")
gith = char_race("Gith@", "yanki", "zerai")
goblin = char_race("Goblin")
goliath = char_race("Goliath")
harengon = char_race("Harengon")
hobgoblin = char_race("Hobgoblin")
kenku = char_race("Kenku")
kobold = char_race("Kobold")
lizardfolk = char_race("Lizardfolk")
minotaur = char_race("Minotaur")
orc = char_race("Orc")
satyr = char_race("Satyr")
shifter = char_race("?Shifter", "Werebear", "Wereboar", "Wererat", "Weretiger", "Werewolf")
tabaxi = char_race("Tabaxi")
tortle = char_race("Tortle")
triton = char_race("Triton")
yuan_ti = char_race("Yuan-Ti")

#Eberon Rising
kalashtar = char_race("Kalashtar")
warforged = char_race("Warforged")

#Spelljammer
#astral_elf = char_race("Astral Elf")
autognome = char_race("Autognome")
giff = char_race("Giff")
hadozee = char_race("Hadozee")
plasmoid = char_race("Plasmoid")
thri_kreen = char_race("Thri-Kreen")

charraces = [
    dwarf, elf, halfling, human, dragonborn, gnome, half_elf, half_orc, tiefling,
    aarakocra, aasimar, bugbear, centaur, changeling, eladrin, fairy,
    firbolg, genasi, gith, goblin, goliath, harengon, hobgoblin, kenku,
    kobold, lizardfolk, minotaur, orc, satyr, shifter, tabaxi, tortle,
    triton, yuan_ti,
    kalashtar, warforged,
    autognome, giff, hadozee, plasmoid, thri_kreen
             ]

spelljammerEnabled = False

def randomRace():
    maxval = len(charraces)
    if not spelljammerEnabled:
        maxval -= 5
    return charraces[random.randrange(0, maxval)]

def randomSubRace(race = False):
    rr = False
    if not race:
        rr = randomRace()
    else:
        rr = race
    raceName = rr.name
    if len(rr.sub_races) > 0:
        if raceName[0] == '?':
            raceName = raceName.replace('?', '')
            if random.randrange(0, 2) == 0:
                return raceName
        subRace = rr.sub_races[random.randrange(0, len(rr.sub_races))]
        if subRace[0] == '!':
            subRace = subRace.replace('!', '')
            return subRace

        if raceName[len(raceName) - 1] == '@':
            raceName = raceName.replace('@', '') + subRace
        else:
            raceName = subRace + " " + raceName
            
    return raceName

morality = ["Good", "Neutral", "Evil"]
methods = ["Lawful", "Neutral", "Chaotic"]

def randomAlignment():
    moral = morality[random.randrange(0, len(morality))]
    method = methods[random.randrange(0, len(methods))]
    alignment = method + " " + moral
    if alignment == "Neutral Neutral":
        alignment = "True Neutral"
    return "(" + alignment + ")"

def randomChar():
    rc = ""
    if random.randrange(0, multiclass_rarity) == 1:
        rc = randomMultiClass()
    else:
        rc = randomSubClass()
    return randomSubRace() + " " + rc + " " + randomAlignment()

natures = [
    "Hardy", "Lonely", "Brave", "Adamant", "Naughty", "Bold",
    "Docile", "Relaxed", "Impish", "Lax", "Timid", "Hasty",
    "Serious", "Jolly", "Naive", "Modest", "Mild", "Quiet",
    "Bashful", "Rash", "Calm", "Gentle", "Sassy", "Careful", "Quirky"
    ]
def randomCharNature():
    return randomChar() + " (" + natures[random.randrange(0, len(natures))] + ")"


def batch_generate(count):
    print("YOUR CHARACTERS ARE:")
    #funs = [randomCharNature, randomChar]
    for i in range(0, count):
        time.sleep(0.6)
        #print("#" + str(i+1) + ": " + funs[random.randrange(0, len(funs))]())
        print("#" + str(i+1) + ": " + randomChar())
