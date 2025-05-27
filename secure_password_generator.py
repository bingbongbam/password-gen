import os,sys

def clear_screen():
    cmd = 'cls' if os.name == 'nt' else 'clear'
    os.system(cmd)

def restart_program():
    clear_screen()
    python = sys.executable
    os.execl(python, python, *sys.argv)


alphabet = "abcdefghijklmnopqrstuvwxyz" 


def main():
    s = input("Enter your word that only has LETTERS, trust me gang :P : ").strip()

    if not s.isalpha():
        print("Did you not see me say LETTERS, perhaps I should have a retard alert coded in too. You don't know what I can do.")
        input("press enter and retry from the beginning pal")
        restart_program()

    key = str(input("Enter the key: ")).strip()
    
    if not key.isdigit():
        print("that's not an INTEGER gang >:( don't make me mad you downloaded this file off your computer from ME.)")
        input("press enter and retry from the beginning pal")
        restart_program()

    key = int(key)

    if (key < 0) or (key >= 26):
            print("forgot to say it MUST to be a number between 1 and 26 or 25 I might've messed up the code? nevertheless, don't piss me off.")
            input("press enter and retry from the beginning pal")
            restart_program()

    encrypted = []
    for ch in s:
        orig_idx = alphabet.index(ch.lower())
        new_idx = (orig_idx + key) % 26 
        new_char = alphabet[new_idx]
        encrypted.append(new_char.upper() if ch.isupper() else new_char)

    encrypted = "".join(encrypted)
    print(f"Your encrypted password is: {encrypted}")
    print("I hope you like it, I worked hard on it, and I hope you don't try to hack me or something.")
    print("If you do, I will find you and I will make you regret it, just kidding, I don't have that kinda power yet.")


if __name__ == "__main__":
    clear_screen()
    print("Welcome to your semi-'secure' Password Generator! (press enter to continue :))")
    print("If you know who I am and don't trust the security of this program that is hurtful but understandable")
    print("But if you don't, trust me im a genius")
    print("Anywhoo I'm gonna take a word from you then also take an integer from you and whip you up a nice encrypted password.")
    main()
    input('Press RETURN to finish')