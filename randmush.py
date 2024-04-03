import random

class Mushroom:
    def __init__(self, cap_color, spot_color, height, bendiness, job):
        self.cap_color = cap_color
        self.spot_color = spot_color
        self.height = height
        self.bendiness = bendiness
        self.job = job

    def __str__(self):
        return f"cap colour: {self.cap_color}\nspot colour: {self.spot_color}\nheight: {self.height} cm\nbendiness: {self.bendiness} (from 0 to 1)\njob: {self.job}"

def generate_random_mushroom():
    cap_colors = ["red", "yellow", "blue", "white", "brown", "purple", "green", "black", "orange", "pink"]
    spot_colors = ["red", "yellow", "blue", "white", "brown", "purple", "green", "black", "orange", "pink"]
    jobs = [
        "engineer", "scientist", "programmer", "pirate", "ninja", "robot", "monster", "zombie",
        "teacher", "professor", "librarian", "musician",
        "doctor", "nurse", "soldier", "sailor", "pilot", "policeman",
        "painter", "detective", "fisherman", "farmer", "businessman",
        "chef", "baker", "lawyer", "judge", "magician", "knight", "wizard"
    ]
    height = random.randint(3, 500)  # height in cm (3 cm to 500 cm)
    bendiness = random.random()  # bendiness represented as a float between 0 and 1
    job = random.choice(jobs)

    return Mushroom(
        cap_color=random.choice(cap_colors),
        spot_color=random.choice(spot_colors),
        height=height,
        bendiness=bendiness,
        job=job
    )

def main():
    num_mushrooms = int(input("how many mushes do u want? "))

    for _ in range(num_mushrooms):
        mushroom = generate_random_mushroom()
        print(mushroom)
        print()  # Adding an empty line between mushrooms for neatness

if __name__ == "__main__":
    main()
