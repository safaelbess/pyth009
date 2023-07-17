 c= 1
 while (c<=3):
  num1 =int(input('enter a number'))
  for i in range(2,num1):
    if num1%i==0:
      print('the number is not prime')
      break
   
    else: 
      print('the number is prime')
      
      
  if num1%2==0:
    print ("the number is even")
  else:
    print('the number is odd')
  
  str1=input('enter your word')  
  for j in range (0,len(str1)):
    if str1[j]=='u' or str1[j]=='l':
      str1=str1.replce(str1[j],'*')
      print(str1)
      
  c =c+1  
  
  