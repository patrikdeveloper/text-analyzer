"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Patrik Hlaváč
email: pathlavac@seznam.cz
discord: patrik_py
"""

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30N and the Union Pacific Railroad,
    which traverse the valley.''',

    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',

    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]



users = {                                    
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")
             # kontrola přihlašovacích údajů
if  username_input not in users or users[username_input] != password_input: 
    print("$ python projekt1.py")
    print(f"username: {username_input}")
    print(f"password: {password_input}")
    print("Unregistered user, terminating program..")
else:
    print("$ python projekt1.py")
    print(f"username: {username_input}")
    print(f"password: {password_input}")
    print(f"-" * 40)
    print(f"Welcome to the app, {username_input}\nWe have 3 texts to be analyzed.")
    print("-" * 40)
    text_choice = (input("Enter a number btw. 1 and 3 to select: ")).strip()
    print("-" * 40)
    if not text_choice.isdigit():
        print("Your choice is not a number, terminating the program..")
    else:
        choice = int(text_choice)
            # kontrola, zda je číslo v rozsahu 1 až 3
        if choice < 1 or choice > 3:
            print("Your choice is invalid, terminating the program..")
        else:
            
            text = TEXTS[choice - 1]
            # rozdělení textu na slova
            words = text.split()  
            total_words = len(words)  
            capitalized_words = sum(1 for word in words if word[0].isupper())  
            upper_words = sum(1 for word in words if word.isupper() and word.isalpha())
            numeric_strings = sum(1 for word in words if word.isdigit())
            lower_words = sum(1 for word in words if word.islower())
            sum_numbers = sum(int(word) for word in words if word.isdigit())
            print(f"There are {total_words} words in the selected text.")
            print(f"There are {capitalized_words} titlecase words.")
            print(f"There are {upper_words} uppercase words")
            print(f"There are {lower_words} lowercase words.")
            print(f"There are {numeric_strings} numeric strings.")
            print(f"The sum all of the numbers {sum_numbers}")
            print('-' * 40)
            # odstraněni interpunkce
            len_words = [len(word.strip("?!.,")) for word in words] 
            slovnik = {}
            for i in len_words:
                if i in slovnik:
                    slovnik[i] += 1
                else:
                    slovnik[i] = 1
            
            # tisk hlavičky tabulky
            print(f"{'-' * 40}")
            print(f"{'LEN':>3} | {'OCCURRENCES':^20} | {'NR.':>3}")
            print(f"{'-' * 40}")

            # tisk jednotlivých řádků s údaji
            for i in sorted(slovnik):
                print(f"{i:>3} | {'*' * slovnik[i]:<20} | {slovnik[i]:<3}")  
            print(f"{'-' * 40}")

