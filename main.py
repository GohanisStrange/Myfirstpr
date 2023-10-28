my_dict = {'names': ['Jordan', 'Jacob' , 'Sasha'],
           'user':'Pasha',
           'numbers': (99, 80)}

print(my_dict['numbers'])

z = input('Введите имя:')
instructor = {'name': 'JO', 'age': 21, 'job': 'programmer'}

print(instructor.values())
print(instructor.keys())
print(instructor.items())

if 'name' in 'instructor':
    print('Yes')
else:
    print('no')

users = {}
users["name"] = 'JO'


print(users)
print(users['name'])

cafees = {'Evos':{'Gorod': 'Tashkent','Fillialov': 'Mnogo', 'Otkritie':'Segodna'}}

cafees['Evos']['kitchen'] = 'Fast food'

my_dict = {'names': 'Jordan'}
print(my_dict)
my_dict['names'] = 'Pavel'
print(my_dict)

my_dict = {'song': 'Beliver',
           'singer': 'MagickDragom'}
print(my_dict)
my_dict.pop('singer')

my2 = {'title': 'Python for begginers'}
print(my2.get('title'))

my = dict(name='Jordan', age=23, job='programmer')
print(my)
my2 = my.copy()
print(my2)

igi = {1,2,2,3,4,5,5,6}
print(igi)
nums2 = set({'Hello','Hello', 'myname', 2, 2, 0})
print(nums2)

instructor = dict(name='Jordan',
                  age=32,
                  job='SCC programmer')
for k in instructor.keys():
    print(k)
for v in instructor.values():
     print(v)
for k,v in instructor.items():
    print(k,v)

prazniki = {'Навруз': '21 march',
            'New Year': '32 december'}

day = input('Какой праздник,')
print(prazniki.get(day))


def careate_list():
        pass


careate_list()
import requests

link = 'https://www.httpbin.org/forms/post'
data = {'comments': 'ODINOCHESTWO SWOLOCH',
        "custemail": "slon@gmil.com",
        "custname": "KRUTOY",
        "custtel": "+99899999999999",
        "delivery": "21:00",
        "size": "large",
        "topping": "onion"
        }
response = requests.post(link, data=data)
print(response.status_code)
