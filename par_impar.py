number = int(input('Digite um número para ver se ele é IMPAR ou PAR: '))
def verifi(number):
	calc = number % 2 == 0
	return calc
	
print(f'O número {number} é PAR') if verifi(number) == True else None, print(f'O número {number} é IMPAR') if verifi(number) == False else None
# print(,verifi(number))