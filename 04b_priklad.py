# Priklad: Toggle line comment CTRL

# # flight_number = "LH 853"
# # prefix = flight_number[0] + flight_number[1]

# # print(prefix)

# if prefix == "BA": #musí být 2 rovná se! to je pro porovnání
#     company = "British Airways"
# elif prefix == "LH":
#     company = "Lufthansa"
# else:
#     company = "Neznámá společnost"

# print(f"Letíte se společností {company}")

# Seznam:
# guest_list = ["Jirka", "Klára", "Natálie"]
# POZICE:       1.        2.        3.
# INDEX:        0         1         2

# print(guest_list[1])

# Seznam seznamů:
school_marks = [
    ["Jiří", 1, 4, 3, 2],
    ["Natálie", 2, 3, 4, 3],
    ["Tereza", 1, 1, 2, 1],
]

print(school_marks[1][0][-1])

print(school_marks[2][-2])