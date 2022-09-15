#Talitha Najwa Afifah (220535603474)

def greetings(bilang):
    bilang = bilang.strip().lower()

    if "hello" in bilang:
        print ('$0')
    elif bilang[0] == 'h' :
        print ('$20')
    else :
        print ('$100')

jawab = input("Type Greetings \n")

greetings(jawab)
