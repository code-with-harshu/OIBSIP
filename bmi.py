height = int(input("Enter your height "))
weight = int(input("Enter your weight ")) 
height = height / 100.0
bmi = weight / (height ** 2)
if bmi <= 15.0:
    res = "Your BMI is " + str(bmi) + "\nRemarks: Very severely underweight!!"
    print(res)
elif 15.0 < bmi <= 16.0:
    res = "Your BMI is " + str(bmi) + "\nRemarks: Severely underweight!"
    print(res)
elif 16.0 < bmi < 18.5:
    res = "Your BMI is " + str(bmi) + "\nRemarks: Underweight!"
    print(res)
elif 18.5 <= bmi <= 25.0:
    res = "Your BMI is " + str(bmi) + "\nRemarks: Normal."
    print(res)
elif 25.0 < bmi <= 30:
    res = "Your BMI is " + str(bmi) + "\nRemarks: Overweight."
    print(res)
elif 30.0 < bmi <= 35.0:
    res = "Your BMI is " + str(bmi) + "\nRemarks: Moderately obese!"
    print(res)
elif 35.0 < bmi <= 40.0:
    res = "Your BMI is " + str(bmi) + "\nRemarks: Severely obese!"
    print(res)
else:
    res = "Your BMI is " + str(bmi) + "\nRemarks: Super obese!!"
    print(res)