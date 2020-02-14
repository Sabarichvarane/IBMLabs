num1 = int(input("enter value for num1:"))
num2 = int(input("enter value for num2:"))
print("the lcm is ", compute_lcm(num1, num2))
def compute_lcm(x,y):
    if(x > y):
        greater = x
    else:
        greater = y
        while true:
            if(greater % x ==0) and (greater % y ==0):
                lcm = greater
                break;
                greater += 1
        return lcm
