def readFile(path):
    with open(path, 'r') as file:
        datas = file.readlines()

    for i in datas:
        datas = i.strip().split(" ")
        print(lista)

def changeDate(date):
    date = date.split("/")
    newData = date[2]+"-"+date[1]+"-"+date[0]
    return newData

def joinDateHour(date, hour):
    return date+" "+hour
data = changeDate("12/09/2024")
print(joinDateHour(data, "11:38:17"))