#Talitha Najwa Afifah (220535603474)

def greetings(katakan):
    katakan = katakan.strip().lower()

    if "hello" in katakan:
        print ('$0')
    elif katakan[0] == 'h' :
        print ('$20')
    else :
        print ('$100')

jawab = input("Type Greetings \n")

greetings(jawab)
