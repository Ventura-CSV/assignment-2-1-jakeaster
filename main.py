def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    male_students = (input)("Enter the number of male students: ")
    female_students = (input)("Enter the number of female students: ")
    male_students_int = int(male_students)
    female_students_int = int(female_students)

    total_students = male_students_int + female_students_int
    m_perc = (male_students_int / total_students) * 100
    f_perc = (female_students_int / total_students) * 100

    print(f'The total number of students: \t \t {total_students}')
    print(
        f'The number of males and females: \t {male_students_int} \t {female_students_int}')
    print(
        f'The Percentage of males and females: \t {m_perc:.2f}%  {f_perc:.2f}%')

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
