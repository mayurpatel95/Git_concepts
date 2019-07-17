# Following some basic concepts of Python.... 

# 1.String (Working with textual data)
"""
msg1 = "\n\nOne line commment using hash #"
print(msg1)

msg1 = 'Mayur Patel.'

# 1) print normal string.
print("\nString :\n"+msg1)

# 2) lenght of string.
print(len(msg1)) 

# 3) array representation of string
print("String representation using array :")
print(msg1[0:12]) 

# 4)Convert string to Upper and lowercase
print(msg1.lower())
print(msg1.upper())

# 5) count, find replace
print(msg1.count('a'))
print(msg1.find('a'))
print(msg1.replace('Patel','Koli patel'))

# Example of String 
greeting = "Hi"
name = "Mayur Patel."
msg = f'{greeting}, {name}. Welcome!'
print("\n"+msg)

# print(dir(name))

# print(help(str)))


# numbers

num = 23

# 1) type for data
print(type(num))

# 2) arithmetic operators : + - * / % // **
n1 = 3
n2 = 4
num  = num + 1 
print(num)
print(abs(-3))
print(round(3.75,1))

# comparision operator : > < <= >= == !=
print(n1<n2)
n1 = '3'
n2 = '4'
print(int(n1)+ int(n2))


# List , tupes , Dictionary

cors = ['Math', 'ComSci', 'Physics']
print(cors[-1])
print(cors[0:])
print(cors[:2])
cors.append('Art')
print(cors)
cor2 = ['Education', 'Art']
cors.insert(0,cor2)
print(cors)
cors.extend( cor2)
print(cors)
cors.remove('Math')
print(cors)
cors.pop()
print(cors)
cors.reverse()
print(cors)
cor2.sort()
print(cor2)

# print(min(list),max(list))

print('Art' in cors)
print(cors.index('Art'))
for item in cors:
	print(item)
for item,index in enumerate(cors,start=0):
	print(item,index)
cors = ' - '.join(cor2)
nlist = cors.split(' - ')
print(cor2)
print(nlist)

tpl = ('Name', 'Middlename', 'Surname')
tpl2 = tpl
print(tpl)
print(tpl2)

# set

tpl = {'Name', 'Middlename', 'Surname'}
tpl2 = {'Pincode','Address'}
print(tpl)
print('Math' in tpl)
print(tpl.intersection(tpl2))
print(tpl.difference(tpl2))
print(tpl.union(tpl2))

# Dictionary

dict = {'name':'Mayur', 'sirname': 'patel' ,'address': ['pin','state']}
print(dict.get('address'))
print(dict.get('phone','not found'))
dict.update({'phone':456789123})
print(dict)

# del dict['']

print(dict.keys())
print(dict.values())
print(dict.items())

for key, value in dict.items():
	print(key,value)

lang = 'Java'
if lang == 'python':
	print('this is python')
elif lang == 'Java':
	print('this is Java')
else:
	print('not found')

user = 'admin'
login = True

if user == 'admin' and login:
	print('Admin Page')
else:
	print('Bad Creds')

if user == 'admin' or login:
	print('Admin Page')
if not login:
	print('Bad Creds')


a = [1,2,3]
b = [1,2,3]

if a == b:
	print("Both are qual")
if id(a) == id(b):
	print("Both values are equal")
else:
	print("Values not equal")

num = {1,2,3,4,5}

for n1 in num:
	if n1 == 5:
		print("it's 5")
		break
	elif n1 == 3:
		print("Skip-->(3) ")
		continue
	print(n1)

for n1 in num:
	for ltr in 'abc':
		print(n1, ltr)

for i in range(10):
	print(i)
"""
def hl_func():
	print('hi')

print("hello") 