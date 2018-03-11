def trifeca(word):
    """
    Checks whether word contains three consecutive double-letter pairs.
    word: string
    returns: bool
    """
    counter = 0
    i = 0
    while i < (len(word)-1):
        if word[i+1] == word[i]:
            counter = counter+1           
            i= i+2
        else:
            i = i+1
            if counter < 3:
                counter = 0
                               

    if counter == 3:
        return True
    else:
        return False
    
def check_palindrome():
   """
   Runs through all 6-digit numbers and checks the mentioned conditions.
   The function prints out the numbers that satisfy this condition. 
   
   Note: It should print out the first number (with a palindrome in its last 4 digits), 
   not all 4 "versions" of it.
   """
   for i in range(100000,999999):
       number = str(i)
       number = number[2:]
       if number [0] != number [3] or  number [1] != number [2]:
           continue
       number = str(i+1)
       number = number[1:]
       if number [0] != number [4] or  number [1] != number [3]:
           continue
       number = str(i+2)
       number = number [1:5]
       if number [0] != number [3] or  number [1] != number [2]:
           continue
       number = str(i+3)
       if number [0] != number [5] or  number [1] != number [4] or number [2] != number [3]:
           continue
       return i




def compare_subjects_within_student(subj1_all_students,
                                    subj2_all_students):
    """
    Compare the two subjects with their students and print out the "preferred"
    subject for each student. Single-subject students shouldn't be printed.

    Choice for the data structure of the function's arguments is up to you.

    '''
    mock data :
    math = {'Jack': [90, 80], 'Jill': [80, 99], 'Maayan':[100, 100], 'Eliav': [49, 78], 'yossi': [100,95]}
    geography = {'Jack': [68, 83], 'Jill': [76, 81], 'Maayan':[96, 85], 'Eliav': [71, 80]}

    """
    high_subjects = {}
    first = input('please insert the first subject name\n')
    second = input('please insert the second subject name\n')

    both = [i for i in subj1_all_students if i in subj2_all_students]
    

    for i in both:
        name = i
        max_1 = max (subj1_all_students [name])
        max_2 = max (subj2_all_students [name])
        grades = [max_1,  max_2]
        if  max_1 > max_2:
            name_subject = first
        elif max_1 < max_2:
            name_subject = second
        else:
            name_subject = first+ ' and '+ second
                           
        high_subjects[i] = name_subject

    return high_subjects
    
    
             




