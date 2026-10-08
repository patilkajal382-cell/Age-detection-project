from datetime import datetime
from webcam_age import predict_age_from_webcam


print("Starting webcam age detection...")

# STEP 1: predict age
predicted_age = predict_age_from_webcam()

print("Predicted Age:", predicted_age)


# STEP 2: get DOB
dob = input("Enter your birthdate (YYYY-MM-DD): ")

birth_date = datetime.strptime(dob, "%Y-%m-%d")

today = datetime.today()

real_age = today.year - birth_date.year

print("Age from DOB:", real_age)


# STEP 3: compare ages
difference = real_age - predicted_age

if difference < 0:
    difference = -difference

print("Difference:", difference)


if difference <= 5:
    print("AGE VERIFIED")
    print("ACCESS GRANTED")
else:
    print("AGE MISMATCH")
    print("ACCESS DENIED")


# STEP 4: driving license check
if real_age >= 18:
    print("Eligible for Driving License")
else:
    print("Not Eligible for Driving License")