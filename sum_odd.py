#A four-digit integer is given. Find the sum of odd digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.
var_int=5742
x1=var_int%10
var_int=var_int//10
x2=var_int%10
var_int=var_int//10
x3=var_int%10
x4=var_int//10
#Create a variable "sum_odd" and assign it 0.
sum_old=x1*(x1%2)+x2*(x2%2)+x3*(x3%2)+x4*(x4%2)
print(sum_old)
#Find the sum of the odd digits in the variable "var_int".
