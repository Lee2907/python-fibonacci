# Python program to display the Fibonacci sequence

def check_fibo(n):
   if n <= 1:
       return n
   else:
       return(check_fibo(n-1) + check_fibo(n-2))

nterms = 20

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(check_fibo(i))

