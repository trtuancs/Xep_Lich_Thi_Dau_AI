from itertools import islice

def main(file_input, file_output):
    
    # read input
    file_input = open("input.txt","r")
    Line1 = list(map(int,file_input.readline().split(" ")))
    n,k = Line1[0],Line1[1]
    Grades = [] #Diem so
    for line in islice(file_input,0,n):
        Grades.append(int(line))
    

    # run algorithm
    # write output
    return


main('input.txt', 'output.txt')
