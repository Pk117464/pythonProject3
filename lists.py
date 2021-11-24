
#Extracting the word 'Python' from l4


l4 = [3636, 76347, 1526, 255.345, 'Hello Python 3', 75675]
print(l4[4][6:12])
print(l4[4].split(' ')[1])


#Sum all number values of l4,

l5 = l4[0:4] + l4[5:]
print(sum(l5))

my_sum = 0
for el in l4:
    if type(el)==int or type(el)==float:
        my_sum += el
print(my_sum)
l6 = [el for el in l4 if type(el)==int or type(el)==float]
sum_16 = sum([el for el in l4 if type(el)==int or type(el)==float])
print(l6)
print(sum_16)
