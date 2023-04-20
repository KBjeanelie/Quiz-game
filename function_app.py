"""
    THIS PART IS THE PART OF DECLARE AND DEFINITION OF OUR FUNCTION FOR OUR GAME PROGRAMME
    We are four major functions
"""

gamer_name = ""
gamer_age = ""
# exit_game = False
score = 0
good_response = 0
wrong_answer = 0
QUESTION_TABLE = [
    "En quelle année le Titanic a t-il coulé dans l'océan Atlantique le 15 avril, lors de son premier voyage au départ"
    " de Southampton?",
    "Qui a inventé la boîte de conserve pour conserver les aliments en 1810?",
    "Quelle ancienne actrice de Doctor Who a joué le rôle de Nebula dans 'Avengers: Infinity War'?",
    " Qui a lâché un marteau et une plume sur la Lune pour démontrer que sans air ils tombent au même rythme?",
    "Quelle est la température de surface moyenne sur Vénus?",
    "Combien d'eau y a-t-il sur Terre par être humain?",
    "Indiquez l'année où ont eu lieu: Naissance de William Shakespeare",
    "Indiquez l'année où ont eu lieu: Martin Luther lance la Réforme",
    "Indiquez l'année où ont eu lieu: La naissance de Bouddha",
    "Quelle est la taille de la grille sur un jeu de Scrabble ?"
]
RESPONSES = [
    ["1205", 1912, "2005", "1935", 2],
    ["Micheal Jackson", "Christ Champagne", " Pierre Durand", "Percy Shaw", 3],
    ["Karen Gillan", " Mickey Rourke", "Jason Statham", 1],
    ["Émile Berliner", "David R. Scott", "Morgan freeman", 2],
    ["60 ° C (220 ° F)", "780 ° C (900 ° F)", "260 ° C (460 ° F)", "460 ° C (860 ° F)", 4],
    ["125,480, 500 libre par personne", " 210,000,000,000 XNUMX XNUMX XNUMX litres d'eau par personne", "", 2],
    ["1245", "1921", "1564", "1955", 3],
    ["1517", "1924", "2011", "1518", 1],
    ["254BC", "486AV", "520AJ", "1200", 2],
    ["15 x 15", "16 x 16", "17 x 17", 1]
]


def validate_age(name, age: int):
    if age < 18:
        print("Désolé", name, ":(")
        print(
            "Vous n'êtes pas éligible de jouer à ce jeu ! \nVous avez moin de 18, patienter jusqu'à ce que vous serez "
            "majeur :")
    else:
        print("\n\n\n")
        print("-------------------------- Initialisation du Programme -------------------------------")


# This function is used for validate input
# It's verify if the value send is an integer
def validate_input_to_int(_input) -> bool:
    try:
        value = int(_input)
    except:
        print("ERREUR : Vous devez entrer un nombre")
        return False
    return True


# This funtion get the name and the age of our gamer and return them
# It is return a string and an integer
def get_name_and_age():
    name = input("Quel est votre nom ? ")
    while name == "":
        name = input("Quel est votre nom ? ")

    age = input("Quel âge avez vous ? ")

    while not validate_input_to_int(age):
        age = input("Quel âge avez vous ? ")

    validate_age(name, int(age))

    programme_initialization(name, int(age))


# This function is used for initialization our game programme
def programme_initialization(name, age: int):
    global gamer_age, gamer_name
    gamer_name = name
    gamer_age = age
    print("Nom   :", gamer_name)
    print("Age   :", gamer_age, "ans")
    print("Score :", score)
    print("--------------------------------------------------------------------------------------")


def validate_input_response_user(user_input) -> int:
    user_input = input("Repondre>> ")
    while not validate_input_to_int(user_input):
        user_input = input("Repondre>> ")
    return int(user_input)


# This function is used for asking a question
def question(_question, _good_answer: int, _rep1, _rep2, _rep3="", _rep4="", user_rep="", ):
    global good_response, wrong_answer
    print()
    print("--------------------------------------------------------------------------------------")
    print(_question)
    print("1 :", _rep1)
    print("2 :", _rep2)
    if _rep3 != "":
        print("3 :", _rep3)
    if _rep4 != "":
        print("4 :", _rep4)

    user_rep = validate_input_response_user(user_rep)
    while _rep3 == "" and user_rep >= 3:
        print("ERREURE : Saisi éroné, recommencer ")
        user_rep = validate_input_response_user(user_rep)

    while _rep4 == "" and user_rep >= 4:
        print("ERREURE : Saisi éroné, recommencer ")
        user_rep = validate_input_response_user(user_rep)

    global score
    if _good_answer == user_rep:
        score += 10
        print("Bonne réponse :) ")
        print("--------------------------------------------------------------------------------------")
        good_response += 1
    else:
        score -= 2
        print("Mauvaise réponse :(")
        print("--------------------------------------------------------------------------------------")
        wrong_answer += 1


# Display all question
def questions():
    question(QUESTION_TABLE[0], RESPONSES[0][4], RESPONSES[0][0], RESPONSES[0][1], RESPONSES[0][2], RESPONSES[0][3])
    question(QUESTION_TABLE[1], RESPONSES[1][4], RESPONSES[1][0], RESPONSES[1][1], RESPONSES[1][2], RESPONSES[1][3])
    question(QUESTION_TABLE[2], RESPONSES[2][3], RESPONSES[2][0], RESPONSES[2][1], RESPONSES[2][2])
    question(QUESTION_TABLE[3], RESPONSES[3][3], RESPONSES[3][0], RESPONSES[3][1], RESPONSES[3][2])
    question(QUESTION_TABLE[4], RESPONSES[4][4], RESPONSES[4][0], RESPONSES[4][1], RESPONSES[4][2], RESPONSES[4][3])
    question(QUESTION_TABLE[5], RESPONSES[5][3], RESPONSES[5][0], RESPONSES[5][1], RESPONSES[5][2])
    question(QUESTION_TABLE[6], RESPONSES[6][4], RESPONSES[6][0], RESPONSES[6][1], RESPONSES[6][2], RESPONSES[6][3])
    question(QUESTION_TABLE[7], RESPONSES[7][4], RESPONSES[7][0], RESPONSES[7][1], RESPONSES[7][2], RESPONSES[7][3])
    question(QUESTION_TABLE[8], RESPONSES[8][4], RESPONSES[8][0], RESPONSES[8][1], RESPONSES[8][2], RESPONSES[8][3])
    question(QUESTION_TABLE[9], RESPONSES[9][3], RESPONSES[9][0], RESPONSES[9][1], RESPONSES[9][2])


def profile():
    print("Votre nom :", gamer_name)
    print("Age : ", gamer_age, "ans")
    print("Nombre de Bonne réponse :", good_response)
    print("Nombre de Mauvaise réponse:", wrong_answer)
    print("Score :", score)


# main of our programme
def start():
    get_name_and_age()
    if int(gamer_age) < 18:
        return

    questions()

    print()
    if 5 <= good_response <= 8:
        print("--------------------------------------------------------------------------------------")
        print("Félicitation", gamer_name, " !!!!!!!!")
        print("Vous avez réussit le quiz :), vous avez une bonne culture ")
        profile()
        print("--------------------------------------------------------------------------------------")
        return
    if good_response > 8:
        print("--------------------------------------------------------------------------------------")
        print("Félicitation", gamer_name, " !!!!!!!!")
        print("Vous avez réussit le quiz avec succès :)")
        print("Vous êtes très intélligent et avez une bonne culture générale")
        profile()
        print("--------------------------------------------------------------------------------------")
        return

    print("--------------------------------------------------------------------------------------")
    print("Désolé ", gamer_name)
    print("Vous n'avez pas réussit le quiz")
    profile()
    print("--------------------------------------------------------------------------------------")

    
    import random

operator = random.randint(1, 4)

first_number = random.randint(1, 20)

second_number = random.randint(1, 10)

scores = 0

chance = 5


def check_int(val: str) -> float:
    while not val.isnumeric():
        val = "ERREUR: Entrer un nombre: "
    return float(val)


def addition(number1: int, number2: int):
    global scores
    response = number1 + number2
    response_input = input("Calculer : " + str(number1) + " + " + str(number2) + " : ")
    rep = check_int(response_input)

    if rep == response:
        print("Bravo, bonne réponse !")
        print("Vous avez gagnez 10 points :)")
        scores += 10
        return

    print("Désolé, mauvaise réponse !")
    print("Vous avez perdu 2 points :(")
    scores -= 2


def substraction(number1: int, number2: int):
    global scores
    response = number1 - number2
    response_input = input("Calculer : " + str(number1) + " - " + str(number2) + " : ")
    rep = check_int(response_input)

    if rep == response:
        print("Bravo, bonne réponse !")
        print("Vous avez gagnez 12 points :)")
        scores += 12
        return

    print("Désolé, mauvaise réponse !")
    print("Vous avez perdu 3 points :(")
    scores -= 3


def multiplication(number1: int, number2: int):
    global scores
    response = number1 * number2
    response_input = input("Combien font : " + str(number1) + " x " + str(number2) + " : ")
    rep = check_int(response_input)

    if rep == response:
        print("Bravo, bonne réponse !")
        print("Vous avez gagnez 20 points :)")
        scores += 20
        return
    print("Désolé, mauvaise réponse !")
    print("Vous avez perdu 10 points :(")
    scores -= 10


def division(number1: int, number2: int):
    global scores
    response = number1 / number2
    response_input = input("Combien font : " + str(number1) + " / " + str(number2) + " : ")
    rep = check_int(response_input)

    if rep == response:
        print("Bravo, bonne réponse !")
        print("Vous avez gagnez 30 points :)")
        scores += 30
        return
    print("Désolé, mauvaise réponse !")
    print("Vous avez perdu 25 points :(")
    scores -= 25


def question(number1: int, number2: int, op: int):

    i = 0
    while i < chance:
        if op == 1:
            addition(number1, number2)
        elif op == 2:
            substraction(number1, number2)
        elif op == 3:
            multiplication(number1, number2)
        else:
            division(number1, number2)

        op = random.randint(1, 4)
        number1 = random.randint(1, 20)
        number2 = random.randint(1, 10)
        i += 1
    
    print("--------------------------------------------------------------------------------")
    print("Votre Score est de : ", scores)
    print("--------------------------------------------------------------------------------")

start()
