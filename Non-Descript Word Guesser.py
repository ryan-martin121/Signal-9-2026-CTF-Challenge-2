from cryptography.fernet import Fernet

#I hope you don't think I'm dumb enough to leave the answers in plain text :)

key = b'UvmdMIhiqGLThlCy0ono2GEh_CnLg2sK4jbA5_zVQ0E='
fernet = Fernet(key)

#Wordle Function
def wordGuesser(word):
    wordLetters = list(word)
    correct = False
    sequence = ["grey"] * 5

    while not correct:
        guess = input("Enter a five letter word (lowercase): ")
        if len(guess) != 5:
            print("Please enter a five letter word")
            continue
        guessLetters = list(guess)
        copyWord = list(word)

        for letter in range(len(guessLetters)):
            if guessLetters[letter] == wordLetters[letter]:
                sequence[letter] = "green"
                copyWord[letter] = None

        for letter in range(len(guessLetters)):
            if sequence[letter] == "green":
                continue
            if guessLetters[letter] in copyWord:
                sequence[letter] = "yellow"
                index = copyWord.index(guessLetters[letter])
                copyWord[index] = None

        output = " ".join(sequence)
        print(output)
        if sequence == ["green"] * 5:
            correct = True
        sequence = ["grey"] * 5




#Password to receive flag
PASSWORD = fernet.decrypt(b'gAAAAABqkm9lqrrsvMjU60K3xGW5PhsGOpClDxyP3ggl8bENBbA2xwwnsa2dXIQ3Ggh4cISdVdWxJGQtBRGARUbwQJykye00cw==').decode()
passGuess = ""

#Menu Variables
choice = 0

print("Welcome to the Non-Descript Word Guessing Game!")
while choice != 6:
    #Menu
    print("Please select one of the following options:")
    print("1. Play Level 1")
    print("2. Play Level 2")
    print("3. Play Level 3")
    print("4. Play Level 4")
    print("5. Play Level 5")
    print("6. Enter Password")
    try:
        choice = int(input("Choice: "))
    except ValueError:
        print("Please enter a number.")
        choice = 0

    match choice:
        case 1:
            wordGuesser(fernet.decrypt(b'gAAAAABqkm7h_HRDzJkgJ7bpU2TKqPCP0E1gfuPM-1hrpiFM66x7ym7vvriTBpBDe-HS5OVE0LOwtVMXuvvJkSlHNJxPwYEaQw==').decode())
            print("The first letter of the password is " + fernet.decrypt(b'gAAAAABqkm-dDRBnBJmW5VwlKf3qs4K_SgacywR0NHBPyMPfay1ni4rqwbvNo5VSSaNmMVrkmYdlybKL3CbdcXhIRjgCSi4-jA==').decode())
            continue
        case 2:
            wordGuesser(fernet.decrypt(b'gAAAAABqkm72dgSMtCb4cbHQe6jd05HSAW4or9SQ-fyK6rxuuNtjagGjQ0ZtUyTByS3Djez1IOsGk4XXZf03LxZGXwPToUCBQw==').decode())
            print("The second letter of the password is " + fernet.decrypt(b'gAAAAABqknABWfAPIeYK0GF2aMUQB2Oj5UIWqA9HDhpX7UWapwlJRH9kXequEAKtitV2N9fccG31TJx7c5RI0Ospni8DQbtOAA==').decode())
            continue
        case 3:
            wordGuesser(fernet.decrypt(b'gAAAAABqkm8KAlSeYA6i4BdAKQW6hH_-iMxuvqqNQM4PdEBwZD8GLQYQoRPNq1y2dO3WRKI3Ybj3HyVV5kGWTgtrN79nKLI3tA==').decode())
            print("The third letter of the password is " + fernet.decrypt(b'gAAAAABqknAY3DwT4zC2cuvM-kFfk91OkRMeazZIMBE9hlCIsGox5mvHrEHv8YO22HF98DsYbRP5Ok50YTUou1iFMGUDhXfIpQ==').decode())
            continue
        case 4:
            wordGuesser(fernet.decrypt(b'gAAAAABqkm8szU6lja2_7mxa2jc4NeaxLgIWrTY49gbIa7k9eHZkV0Swk-4qnloYqDodAX9mEpxZfvKxilcpUZ3xn56wuMTc7g==').decode())
            print("The fourth letter of the password is " + fernet.decrypt(b'gAAAAABqknAniy-kRSBwZoIqV-MuNIMMiLFtAt0POuT1reOpskLbNpRdo-dZuOhJkTKn4SbwPsqY1CSgTe6nZhn0nLp1F-32oA==').decode())
            continue
        case 5:
            wordGuesser(fernet.decrypt(b'gAAAAABqkm9Irg4hJHk2sRSyJKrkUJJEhpdUD_ChpN4QMBwnkuG6UHHh9uXTTJP1oQv6dvFC0-1HDKwJtr1AIb_z9APqu0WRnA==').decode())
            print("The fifth letter of the password is " + fernet.decrypt(b'gAAAAABqkm6SUX_Zk8EXP-w7kDHclnzAIsk0HsAlc0bncl1YYs5lXbd6WnQ8sHdiSh9fRRdbf14ik-kGnTAybgGuWfcoGvraag==').decode())
            continue
        case 6:
            passGuess = str(input("Enter the password to receive your prize (It is case sensitive): "))
            if passGuess == PASSWORD:
                print("Congratulations! Here is your prize:")
                print(fernet.decrypt(b'gAAAAABqkm4BfyA9jBt6GSItNUSY9PykO7a9ANBB'
                                     b'-BS6g9msizbxyGskrKb4p5OTU8dE_5qfWfEjdgnGpau0P7dHjXYOImvFAg==').decode())
            else:
                choice = 0
                print("Sorry, your password is incorrect. Please try again.")
            continue
        case _:
            print("Invalid option. Try again.")
            continue