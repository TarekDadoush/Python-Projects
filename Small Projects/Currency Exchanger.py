class CurrencyExchanger:
    def __init__(self):
        global name
        name = input('Please Enter your name: ')
        print(" ")
        print(f"Welcome to Currency Exchanger, {name}!")
        
    def usd_to_syp(self,x,y=4120):
        return f"{x*y} SYP"
    
    def syp_to_usd(self,x,y=4120):
        return f"{round(x/y,2)} USD"

    def usd_to_egp(self,x,y=20):
        return f"{x*y} EGP"

    def egp_to_usd(self,x,y=20):
        return f"{round(x/y,2)} USD"





exfun = CurrencyExchanger()

print(" ")

print(f"Before we begin, that's a short tutroial about how to use the program: \n     - Enter 'uts' to convert from USD to SYP. \n     - Enter 'stu' to convert from SYP to USD. \n     - Enter 'ute' to convert from USD to EGP. \n     - Enter 'etu' to convert from EGP to USD. \n     - Enter 'end' to close the program.")


print(" ")
print("Please enter below from which currency to which currency do you want to convert:")

while True:

    answer = input()
    if answer == 'uts':
        print(exfun.usd_to_syp(int(input('Enter value in USD: '))))
        print("If you wish to continue convertig please enter any word from the mentioned above.")
        print(" ")

    elif answer == 'stu':
        print(exfun.syp_to_usd(int(input('Enter value in SYP: '))))
        print("If you wish to continue convertig please enter any word from the mentioned above.")
        print(" ")

    elif answer == 'ute':
        print(exfun.usd_to_egp(int(input('Enter value in USD: '))))
        print("If you wish to continue convertig please enter any word from the mentioned above.")
        print(" ")

    elif answer == 'etu':
        print(exfun.egp_to_usd(int(input('Enter value in EGP: '))))
        print("If you wish to continue convertig please enter any word from the mentioned above.")
        print(" ")

    elif answer == 'end':
        print(" ")
        print(f"Thanks for using my program {name}, check my profile on Github: /TarekDadoush")
        break
    else:
        print(" ")
        print(f"It seems like you've entered somthing wrong {name}. \n     - Enter 'uts' to convert from USD to SYP. \n     - Enter 'stu' to convert from SYP to USD. \n     - Enter 'ute' to convert from USD to EGP. \n     - Enter 'etu' to convert from EGP to USD. \n     - Enter 'end' to close the program.")
        print(" ")




