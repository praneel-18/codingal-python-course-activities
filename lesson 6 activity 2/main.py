# 1) Ask the user to enter the numerator and store it in `numn`.
numn= int(input("enter numerator"))


# 2) Ask the user to enter the denominator and store it in `numd`.
numd= int(input("enter the denominater"))
# 3) Check if `numn` is divisible by `numd`:


# - Find the remainder when `numn` is divided by `numd`.

# - If the remainder is 0, it means perfectly divisible.
if numn % numd==0:
    print(numn,"is divisible by",numd)

else:
    print(numn,"is not divisible by",numd)    


# 4) If divisible, print that `numn` is divisible by `numd`.

# 5) Otherwise, print that `numn` is not divisible by `numd`.
