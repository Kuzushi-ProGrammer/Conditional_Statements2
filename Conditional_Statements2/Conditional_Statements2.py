# Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours
# Rewrite your pay program using 'try' and 'except' so that your program handles non-numeric input and re-prompts for another value (This program)

print("Now that you've worked at our company, please state your pay and we will evaluate how well you need to be compensated!")         

Valid = False                                                           # Sets Valid to false on startup so it can function properly                        
while Valid is False:                                                   # Loops program as long as Valid is False
    try:                                                                    # Checks if the variables 'Hours' and 'PPhour" can be converted into floats
        Hours = float(input('Hours Worked: '))                                                                   # Takes the input for hours and money per hour and converts to floats
        PPHour = float(input('Money per hour: ')) 
        if Hours >= 40:                                                                                                                  # Checks if Hours worked is above 40
            pay = (PPHour*1.5)                                                                                                        # Takes pay per hour and multiplies it by 1.5
            Compensation = ('Gross pay: ${}').format(pay)                                                                               # Formats the variable 'pay' into the string
            print('Congratulations! The company deems you worthy of further compensation, your pay has been raised by 1.5 times!')              # Flavour text
            print(Compensation)                                                                                                             # Prints resultant compensation
            Valid = True
         
        elif Hours < 40:                                                                                                        # Checks if hours worked is under 40
            print('Unfortunately our company deems you incapable of further compensation, try harder next time!')               # If hours worked is not above 40 then a discouraging message appears
            NoCompensate = ('Gross pay: ${}').format(PPHour)                                                                    # Formats the variable 'NoCompensate' 
            print(NoCompensate)                                                                                                      # Prints original value of 'PPHour' in a string
            Valid = True

                                                                                                             
    except:                                                                         # If the variables 'Hours' and 'PPHour' cannot be converted to floats, notifies the user and repeats the process
        print('The character(s) you inputted was invalid, please try again')
        Valid = False                                                               # Sets valid to False so the program try function repeats
        
                                                                       
input('-Press Any Key to Exit Program-')                # Prevents program from closing until key is pressed

# If there's any issues, let me know and i'll fix them! ^^

