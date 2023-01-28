with open("Input/Names/invited_names.txt", mode="r") as names:
    names_list = names.readlines()


with open("Input/Letters/starting_letter.txt", mode="r") as letter:
    letters = letter.read()


for name in names_list:
    invites = letters.replace("[name]", name.strip())
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
        file.write(f"{invites}")

