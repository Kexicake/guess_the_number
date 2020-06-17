max_ = 100
min_ = 0
Temp = True
def maink():
    global max_, min_, Temp
    if Temp: 
        text = 'Число меньше ' + str(int((((max_-min_)/2)+min_))) +  '?\n'
        temp = input(text)
        if temp == 'Да' or temp == 'да':
            max_ = int(((max_-min_)/2)+min_) - 1
        else:
            min_ = int(((max_-min_)/2)+min_)
            Temp = False
    else:
        text = 'Число больше ' + str(int(((max_-min_)/2)+min_)) +  '?\n'
        temp = input(text)
        if temp == 'Да' or temp == 'да':
            min_ = int(((max_-min_)/2)+min_) - 1
        else:
            max_ = int(((max_-min_)/2)+min_)
            Temp = True
        
while True:
    maink()
    if min_ == max_:
        break
print('Вы загадали число ' + str(max_) + '\nНажмите энтр чтобы выйти из программы.')
input()
