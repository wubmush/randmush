import random

class Pokemon:
    def __init__(self, name, type1, type2, hp, attack, defense, sp_attack, sp_defense, speed, ability, colour, dex):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.sp_attack = sp_attack
        self.sp_defense = sp_defense
        self.speed = speed
        self.ability = ability
        self.colour = colour
        self.base_stat_total = hp + attack + defense + sp_attack + sp_defense + speed
        self.dex = dex

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Type1: {self.type1}")
        if self.type2:
            print(f"Type2: {self.type2}")
        print(f"Colour: {self.colour}")
        print(f"Ability: {self.ability}")
        print(f"HP: {self.hp}")
        print(f"At: {self.attack}")
        print(f"Df: {self.defense}")
        print(f"SA: {self.sp_attack}")
        print(f"SD: {self.sp_defense}")
        print(f"Sp: {self.speed}")
        print(f"BST: {self.base_stat_total}")
        print(f"Dex: {self.dex}")
        print()

def generate_pokemon():
    # Sample data for types, abilities, colours, prefixes, and suffixes
    types = ["Normal", "Fire", "Water", "Grass", "Electric", "Ice", "Fighting", "Poison", "Ground", 
             "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]
    colours = ["Red", "Green", "Blue", "Yellow", "Black", "White", "Grey", "Brown", "Purple", "Orange", "Pink"]
    abilities = ["Adaptability", "Aerilate", "Aftermath", "Air Lock", "Analytic", "Anger Point", "Anticipation", "Arena Trap",
 "Aroma Veil", "Aura Break", "Bad Dreams", "Battery", "Battle Armor", "Battle Bond", "Beast Boost", "Berserk",
 "Big Pecks", "Blaze", "Bulletproof", "Cheek Pouch", "Chlorophyll", "Clear Body", "Cloud Nine", "Color Change",
 "Comatose", "Competitive", "Compound Eyes", "Contrary", "Corrosion", "Cursed Body", "Cute Charm", "Damp", "Dancer",
 "Dark Aura", "Dazzling", "Defeatist", "Defiant", "Delta Stream", "Desolate Land", "Disguise", "Download", "Drizzle",
 "Drought", "Dry Skin", "Early Bird", "Effect Spore", "Electric Surge", "Emergency Exit", "Fairy Aura", "Filter",
 "Flame Body", "Flare Boost", "Flash Fire", "Flower Gift", "Flower Veil", "Fluffy", "Forecast", "Forewarn",
 "Friend Guard", "Frisk", "Full Metal Body", "Fur Coat", "Gale Wings", "Galvanize", "Gluttony", "Gooey",
 "Grass Pelt", "Grassy Surge", "Guts", "Harvest", "Healer", "Heatproof", "Heavy Metal", "Honey Gather",
 "Huge Power", "Hustle", "Hydration", "Hyper Cutter", "Ice Body", "Ice Scales", "Illuminate", "Illusion",
 "Immunity", "Imposter", "Infiltrator", "Innards Out", "Inner Focus", "Insomnia", "Intimidate", "Iron Barbs",
 "Iron Fist", "Justified", "Keen Eye", "Klutz", "Leaf Guard", "Levitate", "Light Metal", "Lightning Rod", "Limber",
 "Liquid Ooze", "Liquid Voice", "Long Reach", "Magic Bounce", "Magic Guard", "Magician", "Magma Armor", "Magnet Pull",
 "Marvel Scale", "Mega Launcher", "Merciless", "Minus", "Misty Surge", "Mold Breaker", "Moody", "Motor Drive",
 "Moxie", "Multiscale", "Multitype", "Mummy", "Natural Cure", "Neuroforce", "No Guard", "Normalize", "Oblivious",
 "Overcoat", "Overgrow", "Own Tempo", "Parental Bond", "Pickpocket", "Pickup", "Pixilate", "Plus", "Poison Heal",
 "Poison Point", "Poison Touch", "Power Construct", "Power of Alchemy", "Prankster", "Pressure", "Primordial Sea",
 "Prism Armor", "Protean", "Psychic Surge", "Pure Power", "Queenly Majesty", "Quick Feet", "Rain Dish", "Rattled",
 "Receiver", "Reckless", "Refrigerate", "Regenerator", "Rivalry", "RKS System", "Rock Head", "Rough Skin",
 "Run Away", "Sand Force", "Sand Rush", "Sand Stream", "Sand Veil", "Sap Sipper", "Schooling", "Scrappy",
 "Serene Grace", "Shadow Shield", "Shadow Tag", "Shed Skin", "Sheer Force", "Shell Armor", "Shield Dust",
 "Shields Down", "Simple", "Skill Link", "Slow Start", "Slush Rush", "Sniper", "Snow Cloak", "Snow Warning",
 "Solar Power", "Solid Rock", "Soul-Heart", "Soundproof", "Speed Boost", "Stakeout", "Stall", "Stamina",
 "Stance Change", "Static", "Steadfast", "Steelworker", "Stench", "Sticky Hold", "Storm Drain", "Strong Jaw",
 "Sturdy", "Suction Cups", "Super Luck", "Surge Surfer", "Swarm", "Sweet Veil", "Swift Swim", "Symbiosis",
 "Synchronize", "Tangled Feet", "Tangling Hair", "Technician", "Telepathy", "Teravolt", "Thick Fat", "Tinted Lens",
 "Torrent", "Tough Claws", "Toxic Boost", "Trace", "Triage", "Truant", "Turboblaze", "Unaware", "Unburden",
 "Unnerve", "Victory Star", "Vital Spirit", "Volt Absorb", "Water Absorb", "Water Bubble", "Water Compaction",
 "Water Veil", "Weak Armor", "White Smoke", "Wimp Out", "Wonder Guard", "Wonder Skin", "Zen Mode"]

    prefixes = ["Rapid", "Mystic", "Blizzard", "Dragon", "Frost", "Boulder", "Eclipse", "Whisper", "Venom", "Moon", "Thunder", "Tidal", "Flare", "Star", "Night", "Iron", "Shadow", "Crimson", "Leaf", "Aurora", "Steel", "Whirl", "Gale", "Mistral", "Earth", "Inferno", "Spectral", "Wraith", "Dark", "Nebula", "Lava", "Zap", "Gloom", "Lunar", "Abyssal", "Vortex", "Fluff", "Electro", "Blade", "Swift", "Solar", "Echo", "Fury", "Crystal", "Magma", "Nova", "Omega", "Radiant", "Frostbite", "Polar", "Pulse", "Apex", "Chaos", "Nova", "Vivid", "Eternal", "Sonic", "Cosmic", "Celestial", "Quasar", "Infinity", "Neon", "Supernova", "Galactic", "Phoenix", "Psycho", "Serenity", "Nebula", "Orbit", "Rogue", "Twilight", "Noble", "Velocity", "Blitz", "Obsidian", "Rebel", "Eclipse", "Quantum", "Ignite", "Shiver", "Thunderbolt", "Emerald", "Cascade", "Frostfire", "Crimson", "Harmony", "Majestic", "Infernal", "Radiance", "Vapor", "Bolt", "Sapphire", "Whiplash", "Zephyr", "Galaxy", "Dusk"]
    suffixes = ["strike", "claw", "wing", "whirl", "fang", "fire", "leaf", "sting", "howl", "crash", "wave", "blaze", "shower", "claw", "fury", "beam", "storm", "shade", "wind", "flare", "chaser", "night", "wild", "dust", "flame", "shroud", "nova", "frost", "thunder", "gale", "fury", "quasar", "void", "zenith", "spark", "blitz", "blizzard", "shock", "plasma", "flare", "breeze", "strike", "vortex", "hail", "strike", "drift", "mystique", "roar", "glow", "peak", "shiver", "quake", "cascade", "crescent", "echo", "crimson", "torrent", "freeze", "whisper", "scream", "frost", "twister", "flurry", "nova", "beam", "thunder", "flash", "quake", "frost", "bolt", "storm", "stream", "burst", "haze", "blaze", "whirlpool", "wave", "flame", "fury", "cyclone", "volt", "scorch", "blizzard", "flare", "blaze", "blast", "quiver", "scourge", "frost", "shard", "gust", "inferno", "frenzy", "strike"]
    dex1 = ["scientists", "myths", "legends", "scientists of legend", "a vision", "scripture"]
    dex2 = ["can", "will", "must", "likes to", "loves to", "will reluctantly", "works as we speak to", "has already completed its mission to"]
    dex3 = ["destroy", "kill", "detonate", "explode", "hug", "breed with", "jump over", "eat", "consume", "devour", "vaporize", "liquify", "melt", "evaporate", "decimate", "annihilate", "be eaten by"]
    dex4 = ["an Indian elephant", "a dump truck", "a skyscraper", "an ancient civilization", "an entire planet", "the Shellder on its tail", "life as we know it", "several Indian elephants", "you", "its prey", "itself"]
    dex5 = ["fists", "kicks", "droppings", "psychic powers", "brain", "internal fire", "charm", "abdomen", "poison", "draconic energy"]
    dex6 = ["right here and now", "in the past", "in ancient legend", "3000 years ago", "in the future", "now", "immediately", "instantly", "in seconds", "in minutes"]

    # Randomly select attributes
    name = f"#{random.randint(10000, 99999)} " + random.choice(prefixes) + random.choice(suffixes)
    type1 = random.choice(types)
    type2 = random.choice(types) if random.random() < 0.7 else None
    hp = random.randint(20, 200)
    attack = random.randint(10, 160)
    defense = random.randint(10, 160)
    sp_attack = random.randint(10, 160)
    sp_defense = random.randint(10, 160)
    speed = random.randint(10, 160)
    ability = random.choice(abilities)
    colour = random.choice(colours)
    dex = f"According to {random.choice(dex1)}, this Pokémon {random.choice(dex2)} {random.choice(dex3)} {random.choice(dex4)} using just the power of its {random.choice(dex5)} {random.choice(dex6)}."

    return Pokemon(name, type1, type2, hp, attack, defense, sp_attack, sp_defense, speed, ability, colour, dex)

def generate_multiple_pokemon(num_pokemon):
    pokemons = []
    for _ in range(num_pokemon):
        pokemons.append(generate_pokemon())
    return pokemons

if __name__ == "__main__":
    num_pokemon = int(input("Generate how many Pokémon: "))
    pokemons = generate_multiple_pokemon(num_pokemon)
    print("\nGenerated Pokémon:")
    for pokemon in pokemons:
        pokemon.display_info()