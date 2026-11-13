from drafter import *
from dataclasses import dataclass
import random

@dataclass
class Song:
    title: str
    artist: str
    mood: str
    activity: str
    genre: str

@dataclass
class State:
    mood: str
    activity: str
    genre: str
    songs: list[Song]
    recommendations: list[Song]
    
def create_songs():
    return [
        # POP
        Song("Lucky", "Britney Spears", "Happy", "Studying", "Pop"),
        Song("warm", "Ariana Grande", "Happy", "Studying", "Pop"),
        Song("Someone To Call My Lover", "Janet Jackson", "Happy", "Studying", "Pop"),
        Song("Diet Pepsi", "Addison Rae", "Happy", "Studying", "Pop"),
        Song("Talk talk", "Charli xcx", "Happy", "Studying", "Pop"),
        Song("Juno", "Sabrina Carpenter", "Happy", "Cleaning", "Pop"),
        Song("Girl Like Me", "PinkPantheress", "Happy", "Cleaning", "Pop"),
        Song("Tonight", "PinkPantheress", "Happy", "Cleaning", "Pop"),
        Song("Stars", "PinkPantheress", "Happy", "Cleaning", "Pop"),
        Song("CUFF IT", "Beyoncé", "Happy", "Cleaning", "Pop"),
        Song("Teenage Dream", "Katy Perry", "Happy", "Driving", "Pop"),
        Song("A Night To Remember", "beabadoobee & Laufey", "Happy", "Driving", "Pop"),
        Song("Someone To Call My Lover", "Janet Jackson", "Happy", "Driving", "Pop"),
        Song("End of the World", "Miley Cyrus", "Happy", "Driving", "Pop"),
        Song("Out of My League", "Fitz and The Tantrums", "Happy", "Driving", "Pop"),
        Song("Adore You", "Miley Cyrus", "Happy", "Working Out", "Pop"),
        Song("Girl Like Me", "PinkPantheress", "Happy", "Working Out", "Pop"),
        Song("Tonight", "PinkPantheress", "Happy", "Working Out", "Pop"),
        Song("Stars", "PinkPantheress", "Happy", "Working Out", "Pop"),
        Song("CUFF IT", "Beyoncé", "Happy", "Working Out", "Pop"),
        Song("cigarette smoke", "Olivia Rodrigo", "Sad", "Studying", "Pop"),
        Song("Lie To Girls", "Sabrina Carpenter", "Sad", "Studying", "Pop"),
        Song("Dumb & Poetic", "Sabrina Carpenter", "Sad", "Studying", "Pop"),
        Song("Don't Smile", "Sabrina Carpenter", "Sad", "Studying", "Pop"),
        Song("Sharpest Tool", "Sabrina Carpenter", "Sad", "Studying", "Pop"),
        Song("Supalonely", "BENEE", "Sad", "Cleaning", "Pop"),
        Song("because i liked a boy", "Sabrina Carpenter", "Sad", "Cleaning", "Pop"),
        Song("Revolving door", "Tate McRae", "Sad", "Cleaning", "Pop"),
        Song("Like I do", "Tate McRae", "Sad", "Cleaning", "Pop"),
        Song("Ophelia", "PinkPantheress", "Sad", "Cleaning", "Pop"),
        Song("Casual", "Chappell Roan", "Sad", "Driving", "Pop"),
        Song("Blue", "PinkPantheress", "Sad", "Driving", "Pop"),
        Song("In The Rain", "Addison Rae", "Sad", "Driving", "Pop"),
        Song("High Fashion", "Addison Rae", "Sad", "Driving", "Pop"),
        Song("Times Like These", "Addison Rae", "Sad", "Driving", "Pop"),
        Song("Miss possessive", "Tate McRae", "Sad", "Working Out", "Pop"),
        Song("bloodonmyhands", "Tate McRae & Flo Milli", "Sad", "Working Out", "Pop"),
        Song("New York", "Addison Rae", "Sad", "Working Out", "Pop"),
        Song("True romance", "PinkPantheress", "Sad", "Working Out", "Pop"),
        Song("Another life", "PinkPantheress & Rema", "Sad", "Working Out", "Pop"),
        Song("Headphones On", "Addison Rae", "Relaxing", "Studying", "Pop"),
        Song("Summer Forever", "Addison Rae", "Relaxing", "Studying", "Pop"),
        Song("intro (end of the world) - extended", "Ariana Grande", "Relaxing", "Studying", "Pop"),
        Song("You - Acoustic", "Regard, Troye Sivan & Tate McRae", "Relaxing", "Studying", "Pop"),
        Song("Snap My Finger", "KAYTRANADA & PinkPantheress", "Relaxing", "Studying", "Pop"),
        Song("telepatía", "Kali Uchis", "Relaxing", "Cleaning", "Pop"),
        Song("Money is Everything", "Addison Rae", "Relaxing", "Cleaning", "Pop"),
        Song("Fame is a Gun", "Addison Rae", "Relaxing", "Cleaning", "Pop"),
        Song("Signs", "Tate McRae", "Relaxing", "Cleaning", "Pop"),
        Song("Internet baby (interlude)", "PinkPantheress", "Relaxing", "Cleaning", "Pop"),
        Song("We Are The People", "Empire of the Sun", "Relaxing", "Driving", "Pop"),
        Song("Spring Into Summer", "Lizzy McAlpine", "Relaxing", "Driving", "Pop"),
        Song("positions", "Ariana Grande", "Relaxing", "Driving", "Pop"),
        Song("Aquamarine", "Addison Rae", "Relaxing", "Driving", "Pop"),
        Song("Stateside", "PinkPantheress", "Relaxing", "Driving", "Pop"),
        Song("Turn it up", "PinkPantheress", "Relaxing", "Working Out", "Pop"),
        Song("The aisle", "PinkPantheress", "Relaxing", "Working Out", "Pop"),
        Song("Nice to meet you", "PinkPantheress & Central Cee", "Relaxing", "Working Out", "Pop"),
        Song("Romeo", "PinkPantheress", "Relaxing", "Working Out", "Pop"),
        Song("Beaches", "beabadoobee", "Relaxing", "Working Out", "Pop"),
        Song("Illegal", "PinkPantheress", "Energetic", "Studying", "Pop"),
        Song("Femmebot", "Charli xcx, Dorian Electra & Mykki Blanco", "Energetic", "Studying", "Pop"),
        Song("Just Keep Watching", "Tate McRae", "Energetic", "Studying", "Pop"),
        Song("How Bad Do U Want Me", "Lady Gaga", "Energetic", "Studying", "Pop"),
        Song("Can't Keep A Beat", "Say Now", "Energetic", "Studying", "Pop"),
        Song("Apple", "Charli xcx", "Energetic", "Cleaning", "Pop"),
        Song("Illegal", "PinkPantheress", "Energetic", "Cleaning", "Pop"),
        Song("True romance", "PinkPantheress", "Energetic", "Cleaning", "Pop"),
        Song("Just Keep Watching", "Tate McRae", "Energetic", "Cleaning", "Pop"),
        Song("Femmebot", "Charli xcx, Dorian Electra & Mykki Blanco", "Energetic", "Cleaning", "Pop"),
        Song("Another life", "PinkPantheress & Rema", "Energetic", "Driving", "Pop"),
        Song("How Bad Do U Want Me", "Lady Gaga", "Energetic", "Driving", "Pop"),
        Song("Aquamarine", "Addison Rae", "Energetic", "Driving", "Pop"),
        Song("End of the World", "Miley Cyrus", "Energetic", "Driving", "Pop"),
        Song("Out of My League", "Fitz and The Tantrums", "Energetic", "Driving", "Pop"),
        Song("Still Into You", "Paramore", "Energetic", "Working Out", "Pop"),
        Song("Angel Of My Dreams", "JADE", "Energetic", "Working Out", "Pop"),
        Song("Just Keep Watching", "Tate McRae", "Energetic", "Working Out", "Pop"),
        Song("Can't Keep A Beat", "Say Now", "Energetic", "Working Out", "Pop"),
        Song("How Bad Do U Want Me", "Lady Gaga", "Energetic", "Working Out", "Pop"),

        # R&B
        Song("Love Me Not", "Ravyn Lenae", "Happy", "Studying", "R&B"),
        Song("Happy Now", "Kali Uchis", "Happy", "Studying", "R&B"),
        Song("Sunshine & Rain...", "Kali Uchis", "Happy", "Studying", "R&B"),
        Song("Best to You", "Blood Orange & Empress Of", "Happy", "Studying", "R&B"),
        Song("On & On", "FLO", "Happy", "Studying", "R&B"),
        Song("On & On", "FLO", "Happy", "Cleaning", "R&B"),
        Song("Love Me Not", "Ravyn Lenae", "Happy", "Cleaning", "R&B"),
        Song("Happy Now", "Kali Uchis", "Happy", "Cleaning", "R&B"),
        Song("Best to You", "Blood Orange & Empress Of", "Happy", "Cleaning", "R&B"),
        Song("BMF", "SZA", "Happy", "Cleaning", "R&B"),
        Song("Best to You", "Blood Orange & Empress Of", "Happy", "Driving", "R&B"),
        Song("Love Me Not", "Ravyn Lenae", "Happy", "Driving", "R&B"),
        Song("On & On", "FLO", "Happy", "Driving", "R&B"),
        Song("Happy Now", "Kali Uchis", "Happy", "Driving", "R&B"),
        Song("Sunshine & Rain...", "Kali Uchis", "Happy", "Driving", "R&B"),
        Song("BMF", "SZA", "Happy", "Working Out", "R&B"),
        Song("On & On", "FLO", "Happy", "Working Out", "R&B"),
        Song("Love Me Not", "Ravyn Lenae", "Happy", "Working Out", "R&B"),
        Song("Too Easy", "Tinashe", "Happy", "Working Out", "R&B"),
        Song("Best to You", "Blood Orange & Empress Of", "Happy", "Working Out", "R&B"),
        Song("Ghost in the Machine", "SZA & Phoebe Bridgers", "Sad", "Studying", "R&B"),
        Song("Normal Girl", "SZA", "Sad", "Studying", "R&B"),
        Song("Awkward", "SZA", "Sad", "Studying", "R&B"),
        Song("Drew Barrymore", "SZA", "Sad", "Studying", "R&B"),
        Song("Heaven is a Home…", "Kali Uchis", "Sad", "Studying", "R&B"),
        Song("fue mejor", "Kali Uchis & SZA", "Sad", "Cleaning", "R&B"),
        Song("Normal Girl", "SZA", "Sad", "Cleaning", "R&B"),
        Song("Awkward", "SZA", "Sad", "Cleaning", "R&B"),
        Song("Young Rich & In Love", "Kali Uchis", "Sad", "Cleaning", "R&B"),
        Song("Lose My Cool,", "Kali Uchis", "Sad", "Cleaning", "R&B"),
        Song("Burning Blue", "Mariah the Scientist", "Sad", "Driving", "R&B"),
        Song("Love Galore", "SZA & Travis Scott", "Sad", "Driving", "R&B"),
        Song("Drew Barrymore", "SZA", "Sad", "Driving", "R&B"),
        Song("Young Rich & In Love", "Kali Uchis", "Sad", "Driving", "R&B"),
        Song("One Wish", "Ravyn Lenae & Childish Gambino", "Sad", "Driving", "R&B"),
        Song("Love Is Blind", "Ravyn Lenae", "Sad", "Working Out", "R&B"),
        Song("Burning Blue", "Mariah the Scientist", "Sad", "Working Out", "R&B"),
        Song("fue mejor", "Kali Uchis & SZA", "Sad", "Working Out", "R&B"),
        Song("Love Galore", "SZA & Travis Scott", "Sad", "Working Out", "R&B"),
        Song("Getting No Sleep", "Tinashe", "Sad", "Working Out", "R&B"),
        Song("Days", "Ravyn Lenae", "Relaxing", "Studying", "R&B"),
        Song("Worth the Wait", "Kali Uchis & Omar Apollo", "Relaxing", "Studying", "R&B"),
        Song("No Simulation", "Tinashe", "Relaxing", "Studying", "R&B"),
        Song("Silk Lingerie,", "Kali Uchis", "Relaxing", "Studying", "R&B"),
        Song("For: You", "Kali Uchis", "Relaxing", "Studying", "R&B"),
        Song("telepatía", "Kali Uchis", "Relaxing", "Cleaning", "R&B"),
        Song("Days", "Ravyn Lenae", "Relaxing", "Cleaning", "R&B"),
        Song("For: You", "Kali Uchis", "Relaxing", "Cleaning", "R&B"),
        Song("Sugar! Honey! Love!", "Kali Uchis", "Relaxing", "Cleaning", "R&B"),
        Song("Worth the Wait", "Kali Uchis & Omar Apollo", "Relaxing", "Cleaning", "R&B"),
        Song("Age Ain't Nothing But a Number", "Aaliyah", "Relaxing", "Driving", "R&B"),
        Song("A Couple Minutes", "Olivia Dean", "Relaxing", "Driving", "R&B"),
        Song("Scorsese Baby Daddy", "SZA", "Relaxing", "Driving", "R&B"),
        Song("telepatía", "Kali Uchis", "Relaxing", "Driving", "R&B"),
        Song("For: You", "Kali Uchis", "Relaxing", "Driving", "R&B"),
        Song("Getting No Sleep", "Tinashe", "Relaxing", "Working Out", "R&B"),
        Song("Days", "Ravyn Lenae", "Relaxing", "Working Out", "R&B"),
        Song("Age Ain't Nothing But a Number", "Aaliyah", "Relaxing", "Working Out", "R&B"),
        Song("Scorsese Baby Daddy", "SZA", "Relaxing", "Working Out", "R&B"),
        Song("telepatía", "Kali Uchis", "Relaxing", "Working Out", "R&B"),
        Song("Too Easy", "Tinashe", "Energetic", "Studying", "R&B"),
        Song("In My Bag", "FLO & GloRilla", "Energetic", "Studying", "R&B"),
        Song("Getting No Sleep", "Tinashe", "Energetic", "Studying", "R&B"),
        Song("Dead To Me", "Kali Uchis", "Energetic", "Studying", "R&B"),
        Song("Hasta Cuando", "Kali Uchis", "Energetic", "Studying", "R&B"),
        Song("Dead To Me", "Kali Uchis", "Energetic", "Cleaning", "R&B"),
        Song("In My Bag", "FLO & GloRilla", "Energetic", "Cleaning", "R&B"),
        Song("Too Easy", "Tinashe", "Energetic", "Cleaning", "R&B"),
        Song("Getting No Sleep", "Tinashe", "Energetic", "Cleaning", "R&B"),
        Song("Spin", "Megan Thee Stallion & Victoria Monét", "Energetic", "Cleaning", "R&B"),
        Song("Too Easy", "Tinashe", "Energetic", "Driving", "R&B"),
        Song("In My Bag", "FLO & GloRilla", "Energetic", "Driving", "R&B"),
        Song("Spin", "Megan Thee Stallion & Victoria Monét", "Energetic", "Driving", "R&B"),
        Song("Hasta Cuando", "Kali Uchis", "Energetic", "Driving", "R&B"),
        Song("Dead To Me", "Kali Uchis", "Energetic", "Driving", "R&B"),
        Song("Spin", "Megan Thee Stallion & Victoria Monét", "Energetic", "Working Out", "R&B"),
        Song("Nasty Girl Remix", "Tinashe & Chlöe", "Energetic", "Working Out", "R&B"),
        Song("Too Easy", "Tinashe", "Energetic", "Working Out", "R&B"),
        Song("In My Bag", "FLO & GloRilla", "Energetic", "Working Out", "R&B"),
        Song("Getting No Sleep", "Tinashe", "Energetic", "Working Out", "R&B"),

        # KPOP
        Song("Magnetic", "ILLIT", "Happy", "Studying", "KPop"),
        Song("See U Tonight", "Kylie Cantrall & ILLIT", "Happy", "Studying", "KPop"),
        Song("LOVE COUNTDOWN", "NAYEON & Wonstein", "Happy", "Studying", "KPop"),
        Song("The Chase", "Hearts2Hearts", "Happy", "Studying", "KPop"),
        Song("TIPI-TAP", "Kep1er", "Happy", "Studying", "KPop"),
        Song("XOXZ", "IVE", "Happy", "Cleaning", "KPop"),
        Song("Keeper", "TWICE", "Happy", "Cleaning", "KPop"),
        Song("Magnetic", "ILLIT", "Happy", "Cleaning", "KPop"),
        Song("TIPI-TAP", "Kep1er", "Happy", "Cleaning", "KPop"),
        Song("See U Tonight", "Kylie Cantrall & ILLIT", "Happy", "Cleaning", "KPop"),
        Song("Gabriela", "KATSEYE", "Happy", "Driving", "KPop"),
        Song("XOXZ", "IVE", "Happy", "Driving", "KPop"),
        Song("Keeper", "TWICE", "Happy", "Driving", "KPop"),
        Song("LOVE COUNTDOWN", "NAYEON & Wonstein", "Happy", "Driving", "KPop"),
        Song("Magnetic", "ILLIT", "Happy", "Driving", "KPop"),
        Song("LOVE COUNTDOWN", "NAYEON & Wonstein", "Happy", "Working Out", "KPop"),
        Song("Gabriela", "KATSEYE", "Happy", "Working Out", "KPop"),
        Song("TIPI-TAP", "Kep1er", "Happy", "Working Out", "KPop"),
        Song("XOXZ", "IVE", "Happy", "Working Out", "KPop"),
        Song("Keeper", "TWICE", "Happy", "Working Out", "KPop"),
        Song("ONLY", "LEEHI", "Sad", "Studying", "KPop"),
        Song("start a war", "JENNIE", "Sad", "Studying", "KPop"),
        Song("Handlebars", "JENNIE & Dua Lipa", "Sad", "Studying", "KPop"),
        Song("Don't Know What To Do", "BLACKPINK", "Sad", "Studying", "KPop"),
        Song("Bad Boy", "Red Velvet", "Sad", "Studying", "KPop"),
        Song("ONLY", "LEEHI", "Sad", "Cleaning", "KPop"),
        Song("start a war", "JENNIE", "Sad", "Cleaning", "KPop"),
        Song("Handlebars", "JENNIE & Dua Lipa", "Sad", "Cleaning", "KPop"),
        Song("Don't Know What To Do", "BLACKPINK", "Sad", "Cleaning", "KPop"),
        Song("Bad Boy", "Red Velvet", "Sad", "Cleaning", "KPop"),
        Song("Don't Know What To Do", "BLACKPINK", "Sad", "Driving", "KPop"),
        Song("Bad Boy", "Red Velvet", "Sad", "Driving", "KPop"),
        Song("start a war", "JENNIE", "Sad", "Driving", "KPop"),
        Song("Handlebars", "JENNIE & Dua Lipa", "Sad", "Driving", "KPop"),
        Song("ONLY", "LEEHI", "Sad", "Driving", "KPop"),
        Song("Bad Boy", "Red Velvet", "Sad", "Working Out", "KPop"),
        Song("Don't Know What To Do", "BLACKPINK", "Sad", "Working Out", "KPop"),
        Song("start a war", "JENNIE", "Sad", "Working Out", "KPop"),
        Song("Handlebars", "JENNIE & Dua Lipa", "Sad", "Working Out", "KPop"),
        Song("ONLY", "LEEHI", "Sad", "Working Out", "KPop"),
        Song("Forever", "aespa", "Relaxing", "Studying", "KPop"),
        Song("UP NO MORE", "TWICE", "Relaxing", "Studying", "KPop"),
        Song("Intro : JANE with FKJ", "JENNIE & FKJ", "Relaxing", "Studying", "KPop"),
        Song("Seoul City", "JENNIE", "Relaxing", "Studying", "KPop"),
        Song("When I'm With You", "LISA & Tyla", "Relaxing", "Studying", "KPop"),
        Song("Forever", "aespa", "Relaxing", "Cleaning", "KPop"),
        Song("UP NO MORE", "TWICE", "Relaxing", "Cleaning", "KPop"),
        Song("Intro : JANE with FKJ", "JENNIE & FKJ", "Relaxing", "Cleaning", "KPop"),
        Song("Seoul City", "JENNIE", "Relaxing", "Cleaning", "KPop"),
        Song("When I'm With You", "LISA & Tyla", "Relaxing", "Cleaning", "KPop"),
        Song("Seoul City", "JENNIE", "Relaxing", "Driving", "KPop"),
        Song("Forever", "aespa", "Relaxing", "Driving", "KPop"),
        Song("UP NO MORE", "TWICE", "Relaxing", "Driving", "KPop"),
        Song("When I'm With You", "LISA & Tyla", "Relaxing", "Driving", "KPop"),
        Song("Intro : JANE with FKJ", "JENNIE & FKJ", "Relaxing", "Driving", "KPop"),
        Song("When I'm With You", "LISA & Tyla", "Relaxing", "Working Out", "KPop"),
        Song("UP NO MORE", "TWICE", "Relaxing", "Working Out", "KPop"),
        Song("Seoul City", "JENNIE", "Relaxing", "Working Out", "KPop"),
        Song("Forever", "aespa", "Relaxing", "Working Out", "KPop"),
        Song("Intro : JANE with FKJ", "JENNIE & FKJ", "Relaxing", "Working Out", "KPop"),
        Song("like JENNIE", "JENNIE", "Energetic", "Studying", "KPop"),
        Song("RUDE!", "Hearts2Hearts", "Energetic", "Studying", "KPop"),
        Song("Vision", "(G)I-DLE", "Energetic", "Studying", "KPop"),
        Song("Rich Man", "aespa", "Energetic", "Studying", "KPop"),
        Song("LEMONADE", "aespa", "Energetic", "Studying", "KPop"),
        Song("Vision", "(G)I-DLE", "Energetic", "Cleaning", "KPop"),
        Song("like JENNIE", "JENNIE", "Energetic", "Cleaning", "KPop"),
        Song("RUDE!", "Hearts2Hearts", "Energetic", "Cleaning", "KPop"),
        Song("Rich Man", "aespa", "Energetic", "Cleaning", "KPop"),
        Song("LEMONADE", "aespa", "Energetic", "Cleaning", "KPop"),
        Song("RUDE!", "Hearts2Hearts", "Energetic", "Driving", "KPop"),
        Song("like JENNIE", "JENNIE", "Energetic", "Driving", "KPop"),
        Song("Vision", "(G)I-DLE", "Energetic", "Driving", "KPop"),
        Song("Rich Man", "aespa", "Energetic", "Driving", "KPop"),
        Song("LEMONADE", "aespa", "Energetic", "Driving", "KPop"),
        Song("Rich Man", "aespa", "Energetic", "Working Out", "KPop"),
        Song("Mean Girls", "KATSEYE", "Energetic", "Working Out", "KPop"),
        Song("LEMONADE", "aespa", "Energetic", "Working Out", "KPop"),
        Song("like JENNIE", "JENNIE", "Energetic", "Working Out", "KPop"),
        Song("Vision", "(G)I-DLE", "Energetic", "Working Out", "KPop"),

        # RAP
        Song("High School", "Nicki Minaj & Lil Wayne", "Happy", "Studying", "Rap"),
        Song("I Don't Do Drugs", "Doja Cat & Ariana Grande", "Happy", "Studying", "Rap"),
        Song("COCONUT", "SAILORR & Eem Triplin", "Happy", "Studying", "Rap"),
        Song("Darling, I", "Tyler, The Creator & Teezo Touchdown", "Happy", "Studying", "Rap"),
        Song("Juicy", "Doja Cat & Tyga", "Happy", "Studying", "Rap"),
        Song("COCONUT", "SAILORR & Eem Triplin", "Happy", "Cleaning", "Rap"),
        Song("Juicy", "Doja Cat & Tyga", "Happy", "Cleaning", "Rap"),
        Song("I Don't Do Drugs", "Doja Cat & Ariana Grande", "Happy", "Cleaning", "Rap"),
        Song("High School", "Nicki Minaj & Lil Wayne", "Happy", "Cleaning", "Rap"),
        Song("Girls Gone Wild", "JT", "Happy", "Cleaning", "Rap"),
        Song("Girls Gone Wild", "JT", "Happy", "Driving", "Rap"),
        Song("I Don't Do Drugs", "Doja Cat & Ariana Grande", "Happy", "Driving", "Rap"),
        Song("Juicy", "Doja Cat & Tyga", "Happy", "Driving", "Rap"),
        Song("COCONUT", "SAILORR & Eem Triplin", "Happy", "Driving", "Rap"),
        Song("Deja Vu", "Beyoncé & JAY-Z", "Happy", "Driving", "Rap"),
        Song("Deja Vu", "Beyoncé & JAY-Z", "Happy", "Working Out", "Rap"),
        Song("Juicy", "Doja Cat & Tyga", "Happy", "Working Out", "Rap"),
        Song("Girls Gone Wild", "JT", "Happy", "Working Out", "Rap"),
        Song("COCONUT", "SAILORR & Eem Triplin", "Happy", "Working Out", "Rap"),
        Song("I Don't Do Drugs", "Doja Cat & Ariana Grande", "Happy", "Working Out", "Rap"),
        Song("Judge Judy", "Tyler, The Creator", "Sad", "Studying", "Rap"),
        Song("Mine", "Beyoncé & Drake", "Sad", "Studying", "Rap"),
        Song("Alone", "Doja Cat", "Sad", "Studying", "Rap"),
        Song("Darling, I", "Tyler, The Creator & Teezo Touchdown", "Sad", "Studying", "Rap"),
        Song("How to Pretend", "Lucy Bedroque", "Sad", "Studying", "Rap"),
        Song("How to Pretend", "Lucy Bedroque", "Sad", "Cleaning", "Rap"),
        Song("Alone", "Doja Cat", "Sad", "Cleaning", "Rap"),
        Song("Mine", "Beyoncé & Drake", "Sad", "Cleaning", "Rap"),
        Song("Judge Judy", "Tyler, The Creator", "Sad", "Cleaning", "Rap"),
        Song("Darling, I", "Tyler, The Creator & Teezo Touchdown", "Sad", "Cleaning", "Rap"),
        Song("Mine", "Beyoncé & Drake", "Sad", "Driving", "Rap"),
        Song("Alone", "Doja Cat", "Sad", "Driving", "Rap"),
        Song("How to Pretend", "Lucy Bedroque", "Sad", "Driving", "Rap"),
        Song("Judge Judy", "Tyler, The Creator", "Sad", "Driving", "Rap"),
        Song("Darling, I", "Tyler, The Creator & Teezo Touchdown", "Sad", "Driving", "Rap"),
        Song("Alone", "Doja Cat", "Sad", "Working Out", "Rap"),
        Song("Mine", "Beyoncé & Drake", "Sad", "Working Out", "Rap"),
        Song("How to Pretend", "Lucy Bedroque", "Sad", "Working Out", "Rap"),
        Song("Judge Judy", "Tyler, The Creator", "Sad", "Working Out", "Rap"),
        Song("Darling, I", "Tyler, The Creator & Teezo Touchdown", "Sad", "Working Out", "Rap"),
        Song("Judge Judy", "Tyler, The Creator", "Relaxing", "Studying", "Rap"),
        Song("Darling, I", "Tyler, The Creator & Teezo Touchdown", "Relaxing", "Studying", "Rap"),
        Song("Welcome To Hollywood", "Beyoncé & JAY-Z", "Relaxing", "Studying", "Rap"),
        Song("High School", "Nicki Minaj & Lil Wayne", "Relaxing", "Studying", "Rap"),
        Song("Mine", "Beyoncé & Drake", "Relaxing", "Studying", "Rap"),
        Song("Darling, I", "Tyler, The Creator & Teezo Touchdown", "Relaxing", "Cleaning", "Rap"),
        Song("Welcome To Hollywood", "Beyoncé & JAY-Z", "Relaxing", "Cleaning", "Rap"),
        Song("Judge Judy", "Tyler, The Creator", "Relaxing", "Cleaning", "Rap"),
        Song("I Don't Do Drugs", "Doja Cat & Ariana Grande", "Relaxing", "Cleaning", "Rap"),
        Song("High School", "Nicki Minaj & Lil Wayne", "Relaxing", "Cleaning", "Rap"),
        Song("Welcome To Hollywood", "Beyoncé & JAY-Z", "Relaxing", "Driving", "Rap"),
        Song("Darling, I", "Tyler, The Creator & Teezo Touchdown", "Relaxing", "Driving", "Rap"),
        Song("Judge Judy", "Tyler, The Creator", "Relaxing", "Driving", "Rap"),
        Song("I Don't Do Drugs", "Doja Cat & Ariana Grande", "Relaxing", "Driving", "Rap"),
        Song("High School", "Nicki Minaj & Lil Wayne", "Relaxing", "Driving", "Rap"),
        Song("Welcome To Hollywood", "Beyoncé & JAY-Z", "Relaxing", "Working Out", "Rap"),
        Song("Darling, I", "Tyler, The Creator & Teezo Touchdown", "Relaxing", "Working Out", "Rap"),
        Song("Judge Judy", "Tyler, The Creator", "Relaxing", "Working Out", "Rap"),
        Song("High School", "Nicki Minaj & Lil Wayne", "Relaxing", "Working Out", "Rap"),
        Song("I Don't Do Drugs", "Doja Cat & Ariana Grande", "Relaxing", "Working Out", "Rap"),
        Song("Options", "Doja Cat & JID", "Energetic", "Studying", "Rap"),
        Song("Which One", "Drake & Central Cee", "Energetic", "Studying", "Rap"),
        Song("Savage Remix", "Megan Thee Stallion & Beyoncé", "Energetic", "Studying", "Rap"),
        Song("Like That", "Doja Cat & Gucci Mane", "Energetic", "Studying", "Rap"),
        Song("AMERICA HAS A PROBLEM", "Beyoncé", "Energetic", "Studying", "Rap"),
        Song("Savage Remix", "Megan Thee Stallion & Beyoncé", "Energetic", "Cleaning", "Rap"),
        Song("Options", "Doja Cat & JID", "Energetic", "Cleaning", "Rap"),
        Song("AMERICA HAS A PROBLEM", "Beyoncé", "Energetic", "Cleaning", "Rap"),
        Song("MY HOUSE", "Beyoncé", "Energetic", "Cleaning", "Rap"),
        Song("BLACK PARADE", "Beyoncé", "Energetic", "Cleaning", "Rap"),
        Song("Which One", "Drake & Central Cee", "Energetic", "Driving", "Rap"),
        Song("AMERICA HAS A PROBLEM", "Beyoncé", "Energetic", "Driving", "Rap"),
        Song("MY HOUSE", "Beyoncé", "Energetic", "Driving", "Rap"),
        Song("SPAGHETTII", "Beyoncé, Linda Martell & Shaboozey", "Energetic", "Driving", "Rap"),
        Song("Options", "Doja Cat & JID", "Energetic", "Driving", "Rap"),
        Song("Like That", "Doja Cat & Gucci Mane", "Energetic", "Working Out", "Rap"),
        Song("Gyatt", "Latto & Ice Spice", "Energetic", "Working Out", "Rap"),
        Song("AMERICA HAS A PROBLEM", "Beyoncé", "Energetic", "Working Out", "Rap"),
        Song("MY HOUSE", "Beyoncé", "Energetic", "Working Out", "Rap"),
        Song("Savage Remix", "Megan Thee Stallion & Beyoncé", "Energetic", "Working Out", "Rap"),
    ]

initial_state = State(
    mood="Any",
    activity="Any",
    genre="Any",
    songs=create_songs(),
    recommendations=[]
    )

@route
def home(state: State) -> Page:
    return Page(
        state,
        [
            Header("What Should I Listen To?"),
            Text("Find songs that match your mood and activity!"),
            
            Header("Choose your mood"),
            SelectBox(
                "mood",
                ["Any", "Happy", "Sad", "Relaxing", "Energetic"],
                default_value="Any"
                ),
            
            Header("Choosing your activity"),
            SelectBox(
                "activity",
                ["Any", "Studying", "Working Out", "Driving", "Cleaning"],
                default_value="Any"
                ),
            
            Header("Choosing your genre"),
            SelectBox(
                "genre",
                ["Any", "Pop", "R&B", "KPop", "Rap"],
                default_value="Any"
                ),
            
            Button("Find Songs", find_songs),
            Button("Surprise Me!", "random_song"),
            Button("Browse All Songs", "browse_songs"),
            Button("About", "about"),
            Button("Help", "help"),
            Button("Add a Song", "add_song")
            ]
        )

@route
def index(state: State) -> Page:
    return home(state)

@route
def random_song(state: State) -> Page:
    song = random.choice(state.songs)
    
    return Page(state,[
        Header("Your Random Song!"),
        Text("Song: " + song.title),
        Text("Artist: " + song.artist),
        Text("Mood: " + song.mood),
        Text("Activity: " + song.activity),
        Text("Genre: " + song.genre),
        Button("Pick Another Song", "random_song"),
        Button("Back Home", "home")
        ])

@route
def find_songs(state: State, mood: str,
               activity: str, genre: str) -> Page:

    state.mood = mood
    state.activity = activity
    state.genre = genre

    state.recommendations = []

    for song in state.songs:
        if (state.mood == "Any" or song.mood == state.mood):
            if (state.activity == "Any" or song.activity == state.activity):
                if (state.genre == "Any" or song.genre == state.genre):
                    state.recommendations.append(song)

    random.shuffle(state.recommendations)
    return recommendations(state)

@route
def recommendations(state: State) -> Page:
    if not state.recommendations:
        return Page(state, [
            Header("No Songs Found"),
            Text("Sorry! No songs matched your choices."),
            Text("Try selecting different preferences."),
            Button("Go Back", "home")
        ])

    song = state.recommendations[0]

    return Page(state, [
        Header("Your Song Recommendation!"),
        Header(song.title),
        Text("Artist: " + song.artist),
        Text("Mood: " + song.mood),
        Text("Activity: " + song.activity),
        Text("Genre: " + song.genre),
        Button("Give Me Another", "give_another"),
        Button("Back Home", "home")
    ])

@route
def give_another(state: State) -> Page:
    if len(state.recommendations) > 1:
        first_song = state.recommendations.pop(0)
        state.recommendations.append(first_song)

    return recommendations(state)

@route
def browse_songs(state: State) -> Page:
    song_rows = []

    for song in state.songs:
        song_rows.append([song.title, song.artist])

    return Page(state, [
        Header("Browse All Songs"),
        Table(
            song_rows,
            ["Song Title", "Artist"]
        ),
        Button("Back Home", "home")
    ])

@route
def about(state: State) -> Page:
    return Page(state, [
        Header("About What Should I Listen To?"),
        Text("This app helps people decide what music to listen to."),
        Text("Users can choose their mood, activity, and favorite genre to receive personalized song recommendations."),
        Text("The goal is to make finding music easier and more enjoyable."),
        Text("You can also browse the song collection or let the app surprise you with a random song!"),
        Button("Back Home", "home")
    ])

@route
def help(state: State) -> Page:
    return Page(state, [
        Header("How to Use the App"),
        Header("1. Get Recommendations"),
        Text("Choose a mood, activity, and genre from the dropdown menus."),
        Text("Click Find Songs to receive a song that matches your choices."),
        Header("2. Get Another Song"),
        Text("Click Give Me Another to see another song that matches your preferences."),
        Header("3. Surprise Me"),
        Text("Click Surprise Me to receive a completely random song."),
        Header("4. Browse Songs"),
        Text("Click Browse All Songs to see the entire song collection."),
        Header("5. Add Your Own Song"),
        Text("Click Add a Song on the home page, enter the song information, and click Add Song."),
        Button("Back Home", "home")
    ])

@route
def add_song(state: State) -> Page:
    return Page(state, [
        Header("Add Your Own Song!"),
        "Enter the song title:",
        TextBox("title"),
        "Enter the artist:",
        TextBox("artist"),

        "Choose the mood:",
        SelectBox(
            "mood",
            ["Happy", "Sad", "Relaxing", "Energetic"]
        ),

        "Choose the activity:",
        SelectBox(
            "activity",
            ["Studying", "Working Out", "Driving", "Cleaning"]
        ),

        "Choose the genre:",
        SelectBox(
            "genre",
            ["Pop", "R&B", "KPop", "Rap"]
        ),

        Button("Add Song", "save_song"),
        Button("Back Home", "home")
    ])

@route
def save_song(state: State, title: str, artist: str,
              mood: str, activity: str, genre: str) -> Page:

    if title.strip() == "" or artist.strip() == "":
        return Page(state, [
            Header("Missing Information"),
            Text("Please enter both a song title and artist."),
            Button("Try Again", "add_song")
        ])

    new_song = Song(
        title,
        artist,
        mood,
        activity,
        genre
    )

    state.songs.append(new_song)

    return Page(state, [
        Header("Song Added!"),
        Text(title + " by " + artist + " was added to your collection!"),
        Button("Browse Songs", "browse_songs"),
        Button("Add Another Song", "add_song"),
        Button("Back Home", "home")
    ])

start_server(State(
    mood="Any",
    activity="Any",
    genre="Any",
    songs=create_songs(),
    recommendations=[]
))
