def add(number_one, number_two):
    result = number_one + number_two
    print(result)
add(5,3)    

def substract(number_one, number_two):
    result = number_one - number_two
    print(result)
substract(5,3) 

def add(number_one, number_two):
    result = number_one + number_two
    return result

total = add(3,7)
print(total)
total = add(5,10)
print(total)


def substract(number_one, number_two):
    return number_one - number_two
    
print (substract(5,2))

def greet(name, weather):
    message = "Hi " + name + ". It is a " + weather + " day."
    return message

greetings = greet("Sasha", "rainy")
print(greetings)

greetings = greet("Carl", "sunny")
print(greetings)