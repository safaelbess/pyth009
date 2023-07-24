# 

# #names =['David', 'Alice' , 'Caroline']
# # counter =0

# # myNames =['Ali']
# # names = names[0:] + myNames[0:]
  

# # for i in (names):
# #   if names[0] =='David':
# #     names = names[1:]
# #     print(names)
max =0
sum=0.00
avg =0.00
count=0

list1=[1,2,3,'9','8',3.7,4.5,'r',8,9]
min = list1[0]
for i in list1:
   if type(i)==str:
     continue
   count =count+1 
   sum = sum+i
   if i>max:
     max=i
   if i< min:
     min =i
  
avg = sum/count
print(sum)
print(avg)

print('the maxvalue is',max)
print('the minvalue is ',min)
  