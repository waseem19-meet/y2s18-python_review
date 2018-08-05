# Write your solution for 1.4 here!

def is_prime(a):
    for i in range(2,a):
        if a%i ==0:
            return False

    return True
            

    

print(is_prime(12345))


