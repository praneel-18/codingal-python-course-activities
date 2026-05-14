# 1) Ask the user to enter marks for 4 subjects: math, english, science, and hindi.
maths=int(input("enter maths marks"))
science=int(input("enter science marks"))
english=int(input("enter english marks"))
hindi=int(input("enter hindi marks"))

# Store each mark in its own variable.

# 2) Add all 4 subject marks and store the total in `sum`.
sum = maths+science+english+hindi

# 3) Print the total marks stored in `sum`.

# 4) Calculate the percentage:
percentage=(sum/400)*100

# - Divide `sum` by 400 (total maximum marks for 4 subjects, assuming each is out of 100)

# - Multiply the result by 100

# Store the final value in `perc`.

# 5) Print the percentage stored in `perc`.
print(percentage)