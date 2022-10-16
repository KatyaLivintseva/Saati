def convert(colvo):
    try:
        colvo = int(colvo)
    except Exception:
        return -1
    return colvo
try:
    colvo=0
    colvo = int(input('сколько критериев? '))
    if (colvo < 1):
        print ('введите число от 1 до 9')
        colvo = 1 
        
    else:            
        def krit(znac, colvo): 
            for i in range(colvo): #заполнение матрицы выше диагонали
                for j in range(colvo):
                    if (i == j):
                        znac[i][j] = 1 #значения диагонали - 1
                    
                    if (i < j):
                        relation = int(input('отношение критерия {0} к {1}: '.format(i+1, j+1)))
                        if (relation<0 or relation>9):
                            colvo=1
                        else:
                            relation = convert(relation)
                            znac[i][j] = relation 
                    if (i > j):
                        znac[i][j]=1/znac[j][i]
            return znac            
                        
        def matrix_summa(znac, colvo): #сумма значений
            summa = 0
            for i in range(colvo):
                for j in range(colvo):
                    summa += znac[i][j]
            return summa

        def koffic(znac, colvo, summa): #подсчет коэффициентов
            array_koffic = list()
            for i in range(colvo):
                koffic_summa = 0
                for j in range(colvo):
                    koffic_summa += znac[i][j]
                array_koffic.append(koffic_summa/summa)
            return array_koffic
            
        a = krit([[0] * colvo for i in range(colvo)], colvo)
        a_summa = matrix_summa(a, colvo)
        vse_koffic = koffic(a, colvo, a_summa)
        
        print('полученные весовые коэффициенты: ', end=' ')
        for vk in vse_koffic:
            print("{0:.2f}".format(vk), end=' ')
        
except ValueError:
    print('введите целое число критериев')
    colvo=1

except ZeroDivisionError:
    print('введите целое число критериев от 1 до 9')
    colvo=1

while colvo==1: #если была ошибка, то просим ввести значения до тех пор, пока не получим правильные данные
    try:
        colvo=0
        colvo = int(input('\nсколько критериев? '))
        if (colvo < 1):
            print ('введите число от 1 до 9')
            colvo = 1 
            
        else:            
            def krit(znac, colvo): 
                for i in range(colvo): #заполнение матрицы выше диагонали
                    for j in range(colvo):
                        if (i == j):
                            znac[i][j] = 1 #значения диагонали - 1
                        if (i < j):
                            relation = int(input('отношение критерия {0} к {1}: '.format(i+1, j+1)))
                            if (relation<0 or relation>9):  
                                colvo=1
                            else:
                                relation = convert(relation)
                                znac[i][j] = relation

                        if (i > j):
                            znac[i][j]=1/znac[j][i]
                return znac
            
            def matrix_summa(znac, colvo): #сумма значений
                summa = 0
                for i in range(colvo):
                    for j in range(colvo):
                        summa += znac[i][j]
                return summa

            def koffic(znac, colvo, summa): #подсчет коэффициентов
                array_koffic = list()
                for i in range(colvo):
                    koffic_summa = 0
                    for j in range(colvo):
                        koffic_summa += znac[i][j]
                    array_koffic.append(koffic_summa/summa)
                return array_koffic
                
            a = krit([[0] * colvo for i in range(colvo)], colvo)
            a_summa = matrix_summa(a, colvo)
            vse_koffic = koffic(a, colvo, a_summa)
            
            print('полученные весовые коэффициенты: ', end=' ')
            for vk in vse_koffic:
                print("{0:.2f}".format(vk), end=' ')
         
    except ValueError:
        print('введите целое число критериев')
        colvo=1

    except ZeroDivisionError:
        print('введите целое число критериев от 1 до 9')
        colvo=1

