def zakodovat(file_name):
    file = list(open(file_name, "r"))

    abeceda = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    new_file = ""

    for i in file:
        for a in i:
            if a.lower() in abeceda:
                new_char = (abeceda[(abeceda.index(a.lower())+3)%26])
                new_file += new_char
            else:
                new_file += a

    with open("zakodovany_file.txt", "w") as my_file:
        my_file.write(new_file)

zakodovat("file")


def dekodovat(file_name):
    file = list(open(file_name, "r"))

    abeceda = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']

    new_file = ""

    for i in file:
        for a in i:
            if a.lower() in abeceda:
                new_char = (abeceda[(abeceda.index(a.lower()) - 3) % 26])
                new_file += new_char
            else:
                new_file += a

    with open("odkodovany_file.txt", "w") as my_file:
        my_file.write(new_file)

dekodovat("zakodovany_file.txt")