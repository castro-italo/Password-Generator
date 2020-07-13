import os


from pass_gen import GenPass



def main():
    while True:
        # Clear the terminal output
        os.system('cls')

        # Create an GenPass instance
        new_pass = GenPass()

        file = open('screen.txt', 'r')
        for i in file:
            print(i, end='')
        
        # Take an password generate from user
        option = int(input(" > "))

        if(option == 1):
            print("")
            print(f"Your new password now is: \u001b[31m{new_pass.just_num()}\u001b[37m")
        elif(option == 2):
            print("")
            print(f"Your new password now is: \u001b[31m{new_pass.just_char()}\u001b[37m")
        else:
            print("")
            print(f"Your new password now is: \u001b[31m{new_pass.number_char()}\u001b[37m")
        
        # Continue?
        continuar = int(input("1 - Another password | 0 - Exit"))
        if(continuar == 0):
            print("")
            print("\t \u001b[32m Thanks for use Password Generator! \u001b[37m")
            os.system("pause")
            break
        else:
            pass


if(__name__ == ("__main__")):
    main()
