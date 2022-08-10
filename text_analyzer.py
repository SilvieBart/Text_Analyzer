"""
text_analyzer.py: první projekt do Engeto Online Python Akademie

author: Silvie Bartošíková
email: silviebartosikova@gmail.com
discord: Silvie B.#8828
"""

from muj_balicek.task_template import TEXTS

# Uložené vstupní hodnoty registrovaných uživatelů
users = {"bob": "123", "ann": "pass123", "mike": "passwor123", "liz": "pass123"}

# Pomocné proměnné
separator = 40 * "-"
texts_len = len(TEXTS)

# Požadavek uživatele o zadání hodnot pro proměnné "name" a "password"
name = input("username: ".capitalize())
password = input("password: ".capitalize())
print(separator)

# Ověření registrovaného uživatele
if users.get(name) == password:

    # ... pokud souhlasí, přivítá uživatele jménem
    print(f"Welcome to the app, {name}.",
          f"We have {texts_len} texts to be analyzed.", separator, sep="\n")

else:
    # ... pokud nesouhlasí, upozorní jej na chybné údaje
    print(f"Username: {name}",
          f"Password: {password} ",
          f"Unregistered user, terminating the program..",
          sep="\n")
    quit()

# Program nechá uživatele vybrat mezi třemi texty:
selected_number = input(f"Enter a number btw. 1 and {texts_len} to select: ")

# Program ověří výběr uživatele
if not selected_number.isdecimal():
    print("'" + selected_number + "' is not number")
    quit()

selected_idx = int(selected_number)

if selected_idx > texts_len or selected_idx < 1:
    print(f"The selected number must be used between 1-{texts_len}, "
          f"terminating the program..")
    quit()

# Odstraní nežádoucí znaky
words = list()

for word in TEXTS[selected_idx - 1].split():
    words.append(word.strip(",.:;"))

# Zjistí výskyt jednotlivých slov a dosadi je do proměnných
all_count = len(words)
titlecase = "title"
uppercase = "upper"
lowercase = "lower"
numeric = "numeric"
sum_numbers = 0

word_stat: dict = dict()
length_stat: dict = dict()
word_stat[titlecase] = 0
word_stat[uppercase] = 0
word_stat[lowercase] = 0
word_stat[numeric] = 0

for word in words:
    if len(word) >= 2 and word[0].isupper() and word[1].islower():
        word_stat[titlecase] += 1

    elif word.isupper():
        word_stat[uppercase] += 1

    elif word.islower():
        word_stat[lowercase] += 1

    elif word.isnumeric():
        word_stat[numeric] += 1
        sum_numbers = sum_numbers + int(word)

    if len(word) not in length_stat:
        length_stat[len(word)] = 1
    else:
        length_stat[len(word)] += 1

# Program vypíše získané hodnoty formou vět
else:
    print(separator,
          f"There are {all_count} words in the selected text.",
          f"There are {word_stat[titlecase]} titlecase words",
          f"There are {word_stat[uppercase]} uppercase words.",
          f"There are {word_stat[lowercase]} lowercase words.",
          f"There are {word_stat[numeric]} numeric strings.",
          f"The sum of all the numbers is {sum_numbers}.",
          sep="\n")

# Seřadí počet slov od nejkratších délek a uloží do proměnné
length_sorted = sorted(length_stat, key=length_stat.get(0), reverse=False)

# Vytvoří proměnné pro formátování sloupcového grafu
column1_name = "LEN"
column2_name = "OCCURRENCES"

# ... počítá šířku prvního sloupce
len_width = max(len(column1_name),
                len(str(length_sorted[len(length_sorted) - 1])))

# ... počítá šířku druhého sloupce
max_count = 0

for stat in length_stat:
    if length_stat[stat] > max_count:
        max_count = length_stat[stat]

# Vypíše záhlaví grafu
occurrences_width = max(len(column2_name), max_count + 3)

print(separator,
      column1_name.rjust(len_width) + "|"
      + column2_name.center(occurrences_width) + "|NR.",
      separator,
      sep="\n")

# Vypíše sloupcový graf
for index, length in enumerate(length_sorted):
    print(str(length).rjust(len_width) + "|"
          + (("*" * (length_stat[length])).ljust(occurrences_width))
          + "|" + str(length_stat[length]))
