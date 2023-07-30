# # 

# # #names =['David', 'Alice' , 'Caroline']
# # # counter =0

# # # myNames =['Ali']
# # # names = names[0:] + myNames[0:]
  

# # # for i in (names):
# # #   if names[0] =='David':
# # #     names = names[1:]
# # #     print(names)
# max =0
# sum=0.00
# avg =0.00
# count=0

# list1=[1,2,3,'9','8',3.7,4.5,'r',8,9]
# min = list1[0]
# for i in list1:
#    if type(i)==str:
#      continue
#    count =count+1 
#    sum = sum+i
#    if i>max:
#      max=i
#    if i< min:
#      min =i
  
# avg = sum/count
# print(sum)
# print(avg)

# print('the maxvalue is',max)
# print('the minvalue is ',min)
  



  # # #
# # person = {'name': 'ali', 'age': 33, 'country': 'jordan'}
# # print(person['name'])
# # person['gender'] = 'male'
# # print(person)
# # person['parent'] = {'father': 'ahmad', 'mother': 'sara'}
# # print(person)
# # person['skills'] = {'python', 'java', 'c'}
# # print(person)
# # print('_' * 50)
# # print('name: ' + person['name'])
# # print('age: ' + str(person['age']))
# # print('country: ' + person['country'])
# # print('parent: ', person['parent'])
# # print('skills:', person['skills'])
# # print('gender:' + person['gender'])
# # print('_'*50)

# # #del person['parent']['father']
# # #print(person['parent'])
# # person['parent']['father']='salem'
# # print(person['parent'])
# # for i in person:
# #   print(i ,':', person[i])
# #   for key,value in person.items():
# #     print('key\n : ' ,key)
# #     print('value: ', value)
# # print('_'*50)
# # person2=person.copy()
# # print(person2)
# # person2.clear()
# # print(person2)

# # print('_'*50)
# # print(person.get('name'))
# # print(person.items())
# # print(person.keys())
# # print(person.values())

# # print(person.setdefault('name','sami'))

n = int(input('enter the number of elements:'))

student={}
for i in range(n):
  key =input('enter the key:')
  value = input ('enter the value :')
  student[key] = value

print(student)

for i in (student):
  print(i , ':', student[i]) 
  
an_other_student = bool(input('do you want to add an other student?'))
if an_other_student==True:
  n = int(input('enter the number of elements:'))

  student={}
  for i in range(n):
    key =input('enter the key:')
    value = input ('enter the value :')
    student[key] = value

    print(student)


  ### adding two dictionaries to the original dictionary(student)

  student['subjects'] = {'Math': '', 'English': '', 'science': '', 'Arabic': ''}

for j in (student['subjects']):
  student['subjects'][j] = int(input('enter the subjects grade :'))

student['teachers'] = {'Math': '', 'Arabic': '', 'science': '', 'Arabic': ''}

for c in (student['teachers']):
  student['teachers'][c] = input('enter the teachers name :')

print(student)
