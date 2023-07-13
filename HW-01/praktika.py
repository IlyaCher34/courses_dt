import numpy as np
def random_predict(number:int=1) ->int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    left_limit=1 #нижний предел
    right_limit=101 # верхний предел 
    predict_number = np.random.randint(1, 101) # предполагаемое число

    while number != predict_number:
        if (right_limit-left_limit) < 2: #условие для выхода из цикла 
            break  
        count += 1
        if predict_number> number:
            right_limit=predict_number
            predict_number= round((left_limit+right_limit)/2) #сужаем область угадывания
        else:
            left_limit=predict_number
            predict_number= round ((left_limit+right_limit)/2) #сужаем область угадывания
        
    return(count)

print(f'Количество попыток: {random_predict()}')
def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)
    # RUN
score_game(random_predict)