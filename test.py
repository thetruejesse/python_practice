#if age is 5 go to kindergarten
#ages 6 -> 17 go to 1->12
# ages greater than 17 go to college
#  try to complete program with 10 lines or less

#ask input from student and store age

age = eval(input('please enter your age '))
if (age < 5):
    print('child is not eligible for school')

elif (age == 5):
    print('go to kindergarten')

elif (age >= 6) and (age <= 17):
    grade = age - 5
    print('go to {}th grade'.format(grade))

else:
    print('go to college')