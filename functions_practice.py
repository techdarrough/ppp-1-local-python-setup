def hello():
    print("Hello user")


def pack(one, two, three):
    print(str(one)+str(two)+str(three))



foods =["chiken","steak","potatoes","greenbeans"]
def eat_lunch(list):
    count = 0
    for i in list:
        count += 1
        if count==1:
            print("First I eat " + i)
        else:
            print("Then I eat "+i)

hello()
pack(1,2,3)
pack('one','two','three')
eat_lunch(foods)