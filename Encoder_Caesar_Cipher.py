import string

alphabet_lower = string.ascii_lowercase
alphabet_upper = string.ascii_uppercase

original_message = input("Enter the message you want to encrypt: ")
key = int(input("Enter the key: "))

def encoder(message, cipher):

    encrypted_message = ""

    for letter in message:

        if letter in alphabet_lower:
            position = alphabet_lower.find(letter)
            new_position = (position + cipher) % 26
            new_letter = alphabet_lower[new_position]
            encrypted_message += new_letter

        elif letter in alphabet_upper:
            position = alphabet_upper.find(letter)
            new_position = (position + cipher) % 26
            new_letter = alphabet_upper[new_position]
            encrypted_message += new_letter

        else:
            encrypted_message += letter

    return encrypted_message

print (encoder(original_message, key))


