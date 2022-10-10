import random
import string


pass_len=int(input("Enter the length of password, I suggest you to choose at least 10 digit:"))
if pass_len != type(int):
    pass


sample0=string.ascii_lowercase
# print(sample0,"\\")

sample1=string.ascii_uppercase
# print(sample1,"\\")

sample2=string.digits
# print(sample2,"\\")

sample3=string.punctuation
# print(sample3,"\\")

sample=list(sample0)
sample.extend(sample1)
sample.extend(sample2)
sample.extend(sample3)

# print(sample)
random.shuffle(sample)
# print("---------------------------------------------------------------------------------------------")
# print(sample)

print("Generating Your Password......")
print(f"Your {pass_len} digits password will be:", "".join(sample[0:pass_len]))
