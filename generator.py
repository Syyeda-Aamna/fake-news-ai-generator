import random

subjects = [
    "Virat Kohli",
    "Elon Musk",
    "Narendra Modi",
    "A group of monkeys",
    "NASA scientists",
    "Shahrukh Khan",
    "Delhi auto drivers"
]

actions = [
    "launches",
    "buys",
    "invests in",
    "destroys",
    "celebrates",
    "secretly builds"
]

objects = [
    "AI startup",
    "crypto exchange",
    "robot army",
    "space mission",
    "samosa company",
    "cricket academy"
]

places = [
    "at India Gate",
    "in Mumbai local train",
    "during IPL match",
    "inside parliament",
    "at a tech conference"
]


def generate_fake_headline():

    subject = random.choice(subjects)
    action = random.choice(actions)
    obj = random.choice(objects)
    place = random.choice(places)

    return f"{subject} {action} {obj} {place}"


def generate_ai_headline(topic):

    templates = [
        f"Breaking: {topic} secretly launches AI-powered samosa startup",
        f"Shocking: {topic} spotted building robots in Mumbai",
        f"Experts reveal {topic} planning a secret tech empire",
        f"{topic} invests billions in futuristic cricket AI",
        f"Global news: {topic} partners with NASA for space cricket",
        f"{topic} announces revolutionary AI project in India"
    ]

    return random.choice(templates)