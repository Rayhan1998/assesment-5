log_file = open("um-server-01.txt")


def sales_reports(log_file):  # declared a function
    for line in log_file:  # for loop is looping through log_file
        line = line.rstrip()  # the strip method is removin white spaces from each line

        day = line[0:3]  # slice method start at 0 stop at 3
        if day == "Mon":  # if statements check if Monday
            print(line)  # prints line that satisfies for loop


# pass log_file as an argument to the function sales_report
sales_reports(log_file)
