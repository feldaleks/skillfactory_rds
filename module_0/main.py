import numpy as np

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = np.random.randint(1,101)
    while number != predict:
        count+=1
        if number > predict: 
            predict += 1
        elif number < predict: 
            predict -= 1
    return(count) # выход из цикла, если угадали
	
def game_core_v3(number):
    '''Сначала устанавливаем predict = 50 (середина интервала) и в зависимости от того, больше или меньше, идем вправо или влево'''
    count = 1
    predict = 50
    left = 0
    right = 100
    
    while number != predict:
        count+=1
        if number > predict: 
            left = predict
        elif number < predict: 
            right = predict
        
        # в случае если number = 100 мы должны взять Predict = right, иначе (99+100) // 2 всегда будет = 99
        if right - left > 1:
            predict = (right + left) //2
        else:
            predict = right
    return(count) # выход из цикла, если угадали

# Проверяем
print ('game_core_2')
score_game(game_core_v2)
print ('')
print ('game_core_3')
score_game(game_core_v3)