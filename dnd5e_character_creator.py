print("Hello! Welcome to DND 5e Character Creator!")
character_name = input("Your character's name: ")
print("Welcome to Dungeons and Dragons, " + character_name + "!")

import random

class Dice:
    def __init__(self, sides):
        self.sides = sides
    def roll(self):
        result = random.randint(1,self.sides)
        return result

d4 = Dice(4)
d6 = Dice(6)
d8 = Dice(8)
d10 = Dice(10)
d12 = Dice(12)
d20 = Dice(20)
d100 = Dice(100)

languages = ["Common", "Elvish", "Dwarvish", "Halfling"]

class Stat:
    def __init__(self, name):
        self.name = name
        self.value = 1
    def __repr__(self):
        return self.name
    def asi(self, inc):
        self.value += inc
    def mod(self):
        if self.value == 1:
            return -5
        elif self.value >1 and self.value <4:
            return -4
        elif self.value >3 and self.value <6:
            return -3
        elif self.value >5 and self.value <8:
            return -2
        elif self.value >7 and self.value <10:
            return -1
        elif self.value >9 and self.value <12:
            return 0
        elif self.value >11 and self.value <14:
            return 1
        elif self.value >13 and self.value <16:
            return 2
        elif self.value >15 and self.value <18:
            return 3
        elif self.value >17 and self.value <20:
            return 4
        elif self.value == 20:
            return 5
        else:
            return "Error! Invalid ability score"

st = Stat("Strength")
dx = Stat("Dexterity")
cn = Stat("Constitution")
nt = Stat("Intelligence")
wm = Stat("Wisdom")
ch = Stat("Charisma")

character_race = ""
character_class = ""
character_feats = {}
character_proficiencies = []
character_languages = []
speed_probonus = []

def choose_human():
    character_race = "Human"

    st.asi(1)
    dx.asi(1)
    cn.asi(1)
    nt.asi(1)
    wm.asi(1)
    ch.asi(1)

    speed_probonus.append(30)

    character_languages.append("Common")
    print("Humans already speak one language - Common. Here are the languages you can possibly speak.")
    print(languages)
    while True:
        second_language = input(character_name + "'s second language: ")
        if second_language in languages and second_language != "Common":
            print("Sounds good!")
            break
        else:
            print("Invalid language. Try again.")
    character_languages.append(second_language)

def choose_dwarf():
    character_race = "Dwarf"

    cn.asi(2)
    
    speed_probonus.append(25)

    character_languages.append("Common")
    character_languages.append("Dwarvish")

    character_feats["Darkvision"] = "Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."
    character_feats["Dwarven Resilience"] = "You have advantage on saving throws against poison, and you have resistance against poison damage."
    character_feats["Dwarven Combat Training"] = "You have proficiency with the battleaxe, handaxe, light hammer, and warhammer."
    character_feats["Tool Proficiency"] = "You gain proficiency with the artisan's tools of your choice: smith's tools, brewer's supplies, or mason's tools."
    character_feats["Stonecunning"] = "Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus."

    character_proficiencies.append("Battleaxe")
    character_proficiencies.append("Handaxe")
    character_proficiencies.append("Light Hammer")
    character_proficiencies.append("Warhammer")
    dwarf_tool_proficiencies = ["Smith's Tools", "Brewer's Supplies", "Mason's Tools"]
    print("Dwarves can choose a tool proficiency from the following:")
    print(dwarf_tool_proficiencies)
    while True:
        chosen_tool_proficiency = input(character_name + "'s chosen proficiency: ")
        if chosen_tool_proficiency in dwarf_tool_proficiencies:
            print("Great, thanks!")
            break
        else:
            print("Invalid proficiency, try again.")
    character_proficiencies.append(chosen_tool_proficiency)

def choose_elf():
    character_race = "Elf"

    dx.asi(2)

    speed_probonus.append(30)

    character_languages.append("Common")
    character_languages.append("Elvish")

    character_feats["Darkvision"] = "Accustomed to twilit forests and the night sky, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."
    character_feats["Fey Ancestry"] = "You have advantage on saving throws against being charmed, and magic can't put you to sleep."
    character_feats["Trance"] = "Elves do not sleep. Instead they meditate deeply, remaining semi-conscious, for 4 hours a day. The Common word for this meditation is \"trance.\" While meditating, you dream after a fashion; such dreams are actually mental exercises that have become reflexive after years of practice. After resting in this way, you gain the same benefit a human would from 8 hours of sleep."
    character_feats["Keen Senses"] = "You have proficiency in the Perception skill."

    character_proficiencies.append("Perception")

def choose_halfling():
    character_race = "Halfling"

    dx.asi(2)
    
    speed_probonus.append(25)

    character_languages.append("Common")
    character_languages.append("Halfling")

    character_feats["Lucky"] = "When you roll a 1 on an attack roll, ability check, or saving throw, you can reroll the die. You must use the new result, even if it is a 1."
    character_feats["Brave"] = "You have advantage on saving throws against being frightened."
    character_feats["Nimble"] = "You can move through the space of any creature that is of a size larger than yours."

  
races = ["Human", "Dwarf", "Elf", "Halfling"]

print("Here are your choices for " + character_name + "'s race.")
print(races)
while True:
    chosen_race = input(character_name + "'s race: ")
    if chosen_race in races:
        print("Sounds fun!")
        break
    else:
        print("Invalid race. Try again.")
character_race = chosen_race

if character_race == "Human":
    choose_human()
elif character_race == "Dwarf":
    choose_dwarf()
elif character_race == "Elf":
    choose_elf()
elif character_race == "Halfling":
    choose_halfling()

def choose_fighter():
    character_class = "Fighter"
    speed_probonus.append(2)
    hit_die = Dice(10)
    character_feats["Second Wind"] = "You have a limited well of stamina that you can draw on to protect yourself from harm. On your turn, you can use a bonus action to regain hit points equal to 1d10 + your fighter level. Once you use this feature, you must finish a short or long rest before you can use it again."

    fighting_styles = ["Archery", "Defense", "Dueling", "Great Weapon Fighting", "Protection", "Two Weapon Fighting"]
    print("Fighters can choose one fighting style to start with. Here are your options:")
    print(fighting_styles)
    while True:
        chosen_style = input(character_name + "'s fighting style: ")
        if chosen_style in fighting_styles:
            print("Nice!")
            break
        else:
            print("Invalid fighting style, try again.")
    character_feats["Fighting Style"] = chosen_style

    character_proficiencies.append("All Armor")
    character_proficiencies.append("Shields")
    character_proficiencies.append("Simple Weapons")
    character_proficiencies.append("Martial Weapons")
    character_proficiencies.append("Strength Saving Throws")
    character_proficiencies.append("Constitution Saving Throws")

    print("Fighters can choose two of the following skill proficiencies.")
    fighter_skills = ["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"]
    print(fighter_skills)
    while True:
        first_skill = input(character_name + "'s first skill: ")
        if first_skill in fighter_skills:
            print("Great!")
            second_skill = input("And the second skill is: ")
            if second_skill in fighter_skills and second_skill != first_skill:
                print("Perfect.")
                break
            else:
                print("Invalid skill. Make sure you choose two different skills.")
        else:
            print("Invalid skill. Try again.")
    character_proficiencies.append(first_skill)
    character_proficiencies.append(second_skill)

def choose_ranger():
    character_class = "Ranger"
    speed_probonus.append(2)
    hit_die = Dice(10)

    favored_enemies = ["Aberrations", "Beasts", "Celestials", "Constructs", "Dragons", "Elementals", "Fey", "Fiends", "Giants", "Monstrosities", "Oozes", "Plants", "Undead"]
    print("Rangers are experts in hunting a particular type of prey. Here are your options for your favored enemy.")
    print(favored_enemies)
    while True:
        favored_enemy = input(character_name + "'s favored enemy: ")
        if favored_enemy in favored_enemies:
            print("Sounds good.")
            break
        else:
            print("Invalid enemy type. Try again.")
    character_feats["Favored Enemy"] = "You have advantage on Wisdom (Survival) checks to track " + favored_enemy + ", as well as on Intelligence checks to recall information about them."
    
    terrain_types = ["arctic", "desert", "coast", "forest", "grassland", "mountain", "swamp", "Underdark"]
    print("Rangers are also familiar with a particular type of terrain. Here are your options for terrain types:")
    print(terrain_types)
    while True:
        favored_terrain = input(character_name + "'s favored terrain type: ")
        if favored_terrain in terrain_types:
            print("Good.")
            break
        else:
            print("Invalid terrain type. Try again.")
    character_feats["Natural Explorer"] = "When you make an Intelligence or Wisdom check related to " + favored_terrain + " terrain, your proficiency bonus is doubled if you are using a skill that you\’re proficient in." + """
    While traveling for an hour or more in your favored terrain, you gain the following benefits.
    Difficult terrain doesn\’t slow your group\’s travel.
    Your group can\’t become lost except by magical means.
    Even when you are engaged in another activity while traveling (such as foraging, navigating, or tracking), you remain alert to danger.
    If you are traveling alone, you can move stealthily at a normal pace.
    When you forage, you find twice as much food as you normally would.
    While tracking other creatures, you also learn their exact number, their sizes, and how long ago they passed through the area.
    """

    character_proficiencies.append("Light Armor")
    character_proficiencies.append("Medium Armor")
    character_proficiencies.append("Shields")
    character_proficiencies.append("Simple Weapons")
    character_proficiencies.append("Martial Weapons")
    character_proficiencies.append("Strength Saving Throws")
    character_proficiencies.append("Dexterity Saving Throws")
    print("Rangers can choose three of the following skills to be proficient in:")
    druid_skills = ["Animal Handling", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth", "Survival"]
    print(druid_skills)
    while True:
        first_skill = input(character_name + "'s first skill: ")
        if first_skill in druid_skills:
            second_skill = input("And their second skill: ")
            if second_skill in druid_skills and second_skill != first_skill:
                third_skill = input("And their final skill: ")
                if third_skill in druid_skills and third_skill != first_skill:
                    print("Perfect!")
                    break
                else:
                    print("Invalid skill. Try again.")
            else:
                print("Invalid skill. Try again.")
        else:
            print("Invalid skill. Try again.")
    character_proficiencies.append(first_skill)
    character_proficiencies.append(second_skill)
    character_proficiencies.append(third_skill)

def choose_rogue():
    character_class = "Rogue"
    speed_probonus.append(2)
    hit_die = Dice(8)

    character_proficiencies.append("Light Armor")
    character_proficiencies.append("Simple Weapons")
    character_proficiencies.append("Hand Crossbows")
    character_proficiencies.append("Longswords")
    character_proficiencies.append("Rapiers")
    character_proficiencies.append("Shortswords")
    character_proficiencies.append("Thieves' Tools")
    character_proficiencies.append("Dexterity Saving Throws")
    character_proficiencies.append("Intelligence Saving Throws")
    print("Rogues can choose four skill proficiencies from the following:")
    rogue_skills = ["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight of Hand", "Stealth"]
    print(rogue_skills)
    while True:
        first_skill = input(character_name + "'s first skill: ")
        if first_skill in rogue_skills:
            second_skill = input(character_name + "'s second skill: ")
            if second_skill in rogue_skills and second_skill != first_skill:
                third_skill = input("And " + character_name + "'s third skill: ")
                if third_skill in rogue_skills and third_skill != first_skill:
                    fourth_skill = input("And lastly, " + character_name + "'s fourth and final skill: ")
                    if fourth_skill in rogue_skills and fourth_skill != first_skill:
                        print("Excellent!")
                        break
                    else:
                        print("Invalid skill. Try again.")
                else:
                    print("Invalid skill. Try again.")
            else:
                print("Invalid skill. Try again.")
        else:
            print("Invalid skill. Try again.")
    character_proficiencies.append(first_skill)
    character_proficiencies.append(second_skill)
    character_proficiencies.append(third_skill)
    character_proficiencies.append(fourth_skill)
    print("Rogues also get expertise in two of their skill proficiencies, including thieves' tools.")
    expert_skills = [first_skill, second_skill, third_skill, fourth_skill, "Thieves' Tools"]
    print(expert_skills)
    while True:
        first_expertise = input(character_name + "'s first expert skill: ")
        if first_expertise in expert_skills:
            second_expertise = input("And the second expert skill: ")
            if second_expertise in expert_skills and second_expertise != first_expertise:
                print("Fantastic!")
                break
            else:
                print("Invalid skill. Try again.")
        else:
            print("Invalid skill. Try again.")
    first_index = character_proficiencies.index(first_expertise)
    second_index = character_proficiencies.index(second_expertise)
    character_proficiencies[first_index] = first_expertise + " + Expertise"
    character_proficiencies[second_index] = second_expertise + " + Expertise"


    character_feats["Expertise"] = "Your proficiency bonus is doubled for any ability check you make that uses " + first_expertise + " or " + second_expertise + "."
    character_feats["Sneak Attack"] = "Once per turn, you can deal an extra 1d6 damage to one creature you hit with an attack if you have advantage on the attack roll. The attack must use a finesse or a ranged weapon. You don\'t need advantage on the attack roll if another enemy of the target is within 5 feet of it, that enemy isn\'t incapacitated, and you don\'t have disadvantage on the attack roll."
    character_feats["Thieves\' Cant"] = "During your rogue training you learned thieves\' cant, a secret mix of dialect, jargon, and code that allows you to hide messages in seemingly normal conversation. Only another creature that knows thieves\' cant understands such messages. It takes four times longer to convey such a message than it does to speak the same idea plainly. In addition, you understand a set of secret signs and symbols used to convey short, simple messages, such as whether an area is dangerous or the territory of a thieves\' guild, whether loot is nearby, or whether the people in an area are easy marks or will provide a safe house for thieves on the run."
    character_languages.append("Thieves\' Cant")

def choose_cleric():
    character_class = "Cleric"
    speed_probonus.append(2)
    hit_die = Dice(8)

    character_proficiencies.append("Light Armor")
    character_proficiencies.append("Medium Armor")
    character_proficiencies.append("Shields")
    character_proficiencies.append("All Simple Weapons")
    character_proficiencies.append("Wisdom Saving Throws")
    character_proficiencies.append("Charisma Saving Throws")
    print("Clerics can choose two of the following skill proficiencies:")
    cleric_skills = ["History", "Insight", "Medicine", "Persuasion", "Religion"]
    print(cleric_skills)
    while True:
        first_skill = input(character_name + "'s first skill: ")
        if first_skill in cleric_skills:
            second_skill = input(character_name + "'s second skill: ")
            if second_skill in cleric_skills and second_skill != first_skill:
                print("Wonderful!")
                break
            else:
                print("Invalid skill. Try again.")
        else:
            print("Invalid skill. Try again.")
    character_proficiencies.append(first_skill)
    character_proficiencies.append(second_skill)

    character_feats["Spellcasting"] = "You can cast Cleric spells."
    divine_domains = ["Knowledge", "Life", "Light", "Nature", "Tempest", "Trickery", "War"]
    print("Clerics must choose a Divine Domain from which they draw their power. They are as follows:")
    print(divine_domains)
    while True:
        domain = input(character_name + "'s Divine Domain: ")
        if domain in divine_domains:
            print("Good!")
            break
        else:
            print("Invalid domain. Try again.")
    character_feats["Divine Domain"] = "You have chosen the " + domain + " domain. Your Deity grants you access to " + domain + " domain spells."


classes = ["Fighter", "Ranger", "Rogue", "Cleric"]

print("Here are your choices for " + character_name + "'s class.")
print(classes)
while True:
    chosen_class = input(character_name + "'s class: ")
    if chosen_class in classes:
        print("Very cool!")
        break
    else:
        print("Invalid class, try again.")
character_class = chosen_class

if character_class == "Fighter":
    choose_fighter()
elif character_class == "Ranger":
    choose_ranger()
elif character_class == "Rogue":
    choose_rogue()
elif character_class == "Cleric":
    choose_cleric()

alignments = ["Lawful Good", "Lawful Neutral", "Lawful Evil", "Neutral Good", "True Neutral", "Neutral Evil", "Chaotic Good", "Chaotic Neutral", "Chaotic Evil"]

print("Here are the alignments you can choose from:")
print(alignments)
while True:
    chosen_alignment = input(character_name + "'s alignment: ")
    if chosen_alignment in alignments:
        print("Great choice!")
        break
    else:
        print("Invalid alignment. Try again.")
character_alignment = chosen_alignment

attributes = []

def roll_stat():
    rolls = []
    for i in range(0,4):
        rolls.append(d6.roll())
    rolls.sort()
    del(rolls[0])
    total = 0
    for num in rolls:
        total += num
    attributes.append(total)

for i in range(0, 6):
    roll_stat()

print("It's time to distribute your stats! Here are your six randomly rolled numbers.")
print(attributes)
while True:
    strength_input = input("Choose which number you will attribute to your Strength stat: ")
    strength = int(strength_input)
    if strength in attributes:
        st.asi(strength-1)
        attributes.remove(strength)
        break
    else:
        print("Error, try again.")
while True:
    dexterity_input = input("Choose which number you will attribute to your Dexterity stat: ")
    dexterity = int(dexterity_input)
    if dexterity in attributes:
        dx.asi(dexterity-1)
        attributes.remove(dexterity)
        break
    else:
        print("Error, try again.")
while True:
    constitution_input = input("Choose which number you will attribute to your Constitution stat: ")
    constitution = int(constitution_input)
    if constitution in attributes:
        cn.asi(constitution-1)
        attributes.remove(constitution)
        break
    else:
        print("Error, try again.")
while True:
    intelligence_input = input("Choose which number you will attribute to your Intelligence stat: ")
    intelligence = int(intelligence_input)
    if intelligence in attributes:
        nt.asi(intelligence-1)
        attributes.remove(intelligence)
        break
    else:
        print("Error, try again.")
while True:
    wisdom_input = input("Choose which number you will attribute to your Wisdom stat: ")
    wisdom = int(wisdom_input)
    if wisdom in attributes:
        wm.asi(wisdom-1)
        attributes.remove(wisdom)
        break
    else:
        print("Error, try again.")
while True:
    charisma_input = input("Choose which number you will attribute to your Charisma stat: ")
    charisma = int(charisma_input)
    if charisma in attributes:
        ch.asi(charisma-1)
        attributes.remove(charisma)
        break
    else:
        print("Error, try again.")


stats = {st:st.value, dx:dx.value, cn:cn.value, nt:nt.value, wm:wm.value, ch:ch.value}



stats = {st:[st.value, st.mod()], dx:[dx.value, dx.mod()], cn:[cn.value, cn.mod()], nt:[nt.value, nt.mod()], wm:[wm.value, wm.mod()], ch:[ch.value, ch.mod()]}
level = 1
armor_class = 10 + dx.mod()
initiative = dx.mod()
passive_perception = 10 + wm.mod()
max_hp = 10 + cn.mod()



print("Great job! Here's your character sheet. \n \n ")

print(character_name + ", a level " + str(level) + " " + character_alignment + " " + character_race + " " + character_class + "\n")
print("Stats:")
print("Strength: " + str(st.value) + " (" + str(st.mod()) + ")")
print("Dexterity: " + str(dx.value) + " (" + str(dx.mod()) + ")")
print("Constitution: " + str(cn.value) + " (" + str(cn.mod()) + ")")
print("Intelligence: " + str(nt.value) + " (" + str(nt.mod()) + ")")
print("Wisdom: " + str(wm.value) + " (" + str(wm.mod()) + ")")
print("Charisma: " + str(ch.value) + " (" + str(ch.mod()) + ")")

print("\n")
print("Proficiency Bonus: +" + str(speed_probonus[1]))
print("Max HP: " + str(max_hp))
print("Speed: " + str(speed_probonus[0]))
print("Armor Class: " + str(armor_class))
print("Initiative: " + str(initiative))
print("Passive Perception: " + str(passive_perception))

print("\n")
print("Character Features:")
feat_names = character_feats.keys()
print(", ".join(feat_names))
print("\n")
print("Proficiencies:")
print(", ".join(character_proficiencies))
print("\n")
print("Languages:")
print(", ".join(character_languages))
print("\n")
print("\n")
print("Thanks for using my character creator! More features will be coming!")