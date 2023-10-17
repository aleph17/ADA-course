# this code is written without using any libraries but only relying on the basic tools
# every function should be used separately together with get_data in order to avoid consufion in global variables


def get_data():

   try:
       with open('interactive_data.csv', 'r') as f:
           category = f.readline()
           data = []
           for line in f.readlines():
               i = line.rstrip().split(',')
               datum = []
               for j in i:
                   datum.append(j.strip('"'))
               data.append(datum)
   except OSError:
       exit('file problem')
   return data

def task1():
    data = get_data()
    global suicide, overall_death
    for i in data:
        if i[0] == '1':
            overall_death = int(i[5])
        if i[1] == 'Suicide':
            suicide = int(i[5])
            break
    return suicide/overall_death

def task2():
    data = get_data()
    for i in data:
        if i[1] == 'Suicide' and i[2] == 'Male':
            male_suicide = int(i[5])
            break
    return male_suicide/suicide

def task3():
    data = get_data()
    global overall_homicide
    for i in data:
        if i[1] == 'Homicide':
            overall_homicide = int(i[5])
            break
    return overall_homicide/overall_death

def task4():
    data = get_data()
    found = False
    for i in data:
        if i[1] == 'Homicide' and i[2] == 'Male' and i[3] == '15 - 34' and not found:
            hommale15 = int(i[5])
            found = True
        if i[1] == 'Homicide' and i[2] == 'Male' and i[3] == '15 - 34' and i[4] == 'Black':
            homiafro = int(i[5])
            break
    return homiafro/hommale15
    
def task5():
    data = get_data()
    for i in data:
        if i[1] == 'Homicide' and i[2] == 'Female':
            homifem = int(i[5])
            break
    return homifem / overall_homicide

if __name__ == '__main__':
    task3()
    print(task5)