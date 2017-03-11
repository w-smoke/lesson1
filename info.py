user_info = {'first_name': 'W', 'last_name': 'W'}
user_info['first_name']=input("Name:")
user_info['last_name']=input("Last Name:")
print(user_info['first_name'])
print(user_info['last_name'])
print(user_info)
def privet():
	print('Hi!')
privet()
def summ_something(som, som_2):
	result = str(som) + str(som_2)
	return result.upper()
print(summ_something(user_info['first_name'],user_info['last_name']))
#result=summ_something()
#print(result)