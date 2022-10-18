# def currencyConverter(eur):
#     result = eur * 1.1
#     msg1 = "The conversion from "
#     msg2 = " eur in chf is "
#     msg3 = " chf."
#     return msg1 + str(eur) + msg2 + str(result) + msg3


# print(currencyConverter(10))

def currencyConverter():
    eur = input ("Entrez votre montant en euros")
    msg1 = "The conversion from "
    msg2 = " eur in chf is "
    msg3 = " chf."


    result = int(eur) * 1.1
    
    
    if int(eur)>100:
        print ("vous etes super riches")
    return int(result)
print (currencyConverter())   
print ("et voila")