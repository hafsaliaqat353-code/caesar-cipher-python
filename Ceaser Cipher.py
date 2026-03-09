def caesar(text,shift, encrypt=True):
    if not isinstance(shift,int):
        return 'Shift must  be an integer value.'
    if not isinstance(text,str):
        return "Text must be an alphabet form Aa to Zz"
    if shift < 1 or shift > 25:
        return 'Shift must be between 1 and 25.'
    if not encrypt:
        shift = -shift
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet =  alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text
def encrypt(text,shift):
    return caesar(text,shift)
def decrypt(text,shift):
    return caesar(text,shift,encrypt = False)
action = input('Do you want to encrypt or decrypt? (e/d): ')
if action == 'e':
    message = input('What message you want to encrypt?')
    key = input('What is the special key?')
    encrypt_message = encrypt(message, int(key))
    print(encrypt_message)
elif action == "d":
    message = input('What message you want to decrypt?')
    key = input('What is the special key?')
    decrypt_message = decrypt(message,int(key))
    print(decrypt_message)
else:
    print('Invalid Input')
