import re

# Create alphabet
alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encrypt_caesar(plaintext, shift):
    # Format plaintext and save it to plaintext as the formatted text.
    plaintext = format_text(plaintext)
    # Declare ciphertext as an empty string
    ciphertext = ""
    # Looks through all chars in the formattet plaintext
    for char in plaintext:
        # Saves the indexes of every char to result
        result = alp.index(char)
        # Takes the result and uses modulo with the lenght to start over
        ciphertext += alp[(result + shift) % len(alp)]
        # Returns the indexes of all the chars in the alphabet
    return ciphertext


def decrypt_caesar(ciphertext, shift):
    # Format plaintext and save it to plaintext as the formatted text.
    ciphertext = format_text(ciphertext)
    # Declare ciphertext as an empty string
    plaintext = ""
    # Looks through all chars in the formattet plaintext
    for char in ciphertext:
        # Saves the indexes of every char to result
        result = alp.index(char)
        # Takes the result and uses modulo with the lenght to start over
        plaintext += alp[(result - shift) % len(alp)]
        # Returns the indexes of all the chars in the alphabet
    return plaintext


def generateVigenereKey(string, key):
  key = list(key)
  if len(string) == len(key):
    return(key)
  else:
    for i in range(len(string) -len(key)):
      key.append(key[i % len(key)])
  return("" . join(key))


def format_text(text):
    # Replace everything that is not in the alphabet, with nothing.
    formatted_text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Format all text to uppercase
    formatted_text = formatted_text.upper()
    # Replaces all spaces with no spaces.
    formatted_text = formatted_text.replace(" ", "")
    # Returns formattet text
    return formatted_text


plaintext = "Dette er min text, encrypt / decrypt den!"

# Example usage of caesar encrypt / decrypt
print("Caesar encrypt / decrypt")
shift = 15
ciphertext = encrypt_caesar(plaintext, shift)
print("Ciphertext: ", ciphertext)
decrypted_plaintext = decrypt_caesar(ciphertext, shift)
print("Decrypted: ", decrypted_plaintext)

# Example usage of Vigenère encrypt / decrypt
print("\nVigenère encrypt / decrypt")
keyword = "TILLID"
key = generateVigenereKey(plaintext, keyword)

encrypt_text = ""
decrypt_text = ""
for i in range(len(format_text(plaintext))):
    encrypt_text += encrypt_caesar(format_text(plaintext)[i], alp.index(key[i]))
    decrypt_text += decrypt_caesar(encrypt_text[i], alp.index(key[i]))

print("Ciphertext:", encrypt_text)
print("Decrypted:", decrypt_text)
