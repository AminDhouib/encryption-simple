from cryptography.fernet import Fernet

KEY = "fd4KEVX0yBFmHMtf3Kdzw9ecQqU5lF7s3g0YgfxtBZs="
fernet = Fernet(KEY)

TO_LOCK_FILENAME = "1to_lock.txt"
LOCKED_FILENAME = "2locked.txt"

TO_UNLOCK_FILENAME = "3to_unlock.txt"
UNLOCKED_FILENAME = "4unlocked.txt"

doLock = False

if doLock:
    encWords = []
    with open(TO_LOCK_FILENAME, 'r') as file:
        for word in file:
            encWord = fernet.encrypt(word.encode())
            encWords.append(encWord)

    with open(LOCKED_FILENAME, 'w') as file:
        for encWord in encWords:
            file.write(encWord.decode() + "\n")
    print("Encrypted words!")
else:
    decryptedWords = []
    with open(TO_UNLOCK_FILENAME, 'r') as file:
        for encWord in file:
            decryptedWord = fernet.decrypt(encWord.encode()).decode()
            decryptedWords.append(decryptedWord)

    with open(UNLOCKED_FILENAME, 'w') as file:
        for decryptedWord in decryptedWords:
            file.write(decryptedWord)
    print("Decrypted words!")
