import string

alphabet_lower = string.ascii_lowercase
alphabet_upper = string.ascii_uppercase

encrypted_message = input("Enter the message you want to decrypt: ")
key = int(input("Enter the key: "))

def encoder(message, cipher):

    original_message = ""

    for letter in message:

        if letter in alphabet_lower:
            position = alphabet_lower.find(letter)
            new_position = (position - cipher) % 26
            new_letter = alphabet_lower[new_position]
            original_message += new_letter

        elif letter in alphabet_upper:
            position = alphabet_upper.find(letter)
            new_position = (position - cipher) % 26
            new_letter = alphabet_upper[new_position]
            original_message += new_letter

        else:
            original_message += letter

    return original_message

print(encoder(encrypted_message, key))


