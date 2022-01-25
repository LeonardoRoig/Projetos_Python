
import random
caracters = int(input("Qual a quantidade de caracteres? Valor máximo de 70 caracteres..."))

lower = "abcdefghijklmnopqrstuvxwyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVXWYZ"
NUMBER = "0123456789"
symbol = "!@#$%&*_"

all = lower + upper + NUMBER + symbol
length = caracters
password = "".join(random.sample(all, length))

print (f"You password is:\033[32m {password} "[:70])


