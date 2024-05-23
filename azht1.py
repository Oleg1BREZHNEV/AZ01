import pandas as pd


#Основные функции Pandas
#Перейдём к работе с готовым датасетом, который мы скачали с сайта
# Kaggle. Для этого используем функцию, считывающую информацию
# из csv-файлов. В круглых скобках указываем название
# файла (его можно скопировать, щёлкнув по файлу правой кнопкой
# мыши и выбрав в списке Copy.
#С помощью функции head вывести пять первых строк,
# хранящихся в csv-файле. Можно вывести и большее/меньшее
# количество строк — для этого надо указать точное их количество
# в круглых скобках после прописанной функции. Для этого прописываем:
# print(df.head()) и запускаем (Run).
#В окне вывода мы видим первые пять строк датасета.
# При этом столбец с многоточиями указывает на то, что между
# колонками пропущено ещё какое-то количество столбцов — это
# происходит потому, что вся таблица не умещается в окне вывода.
# Однако мы можем видеть информацию о колличестве  колонок.
df = pd.read_csv('salaries _2.csv')
#3. Если нужно просмотреть последние строки датасета,
# вместо функции head используем функцию tail, для
# этого пишем: print(df.tail()) Таким образом, мы можем узнать,
# колличество строк .
print("Первые пять строк")
print(df.head())
#4. Чтобы посмотреть базовую информацию о датафрейме,
# используем функцию info. Прописываем: print(df.info())
#Здесь выводится информация о том, сколько всего данных
# содержится в датасете, названия всех столбцов и какое
# количество столбцов содержит в себе информацию, а также
# тип хранящихся данных, сколько памяти тратится.
print("Информация о колличественном содержании")
print(df.info())
#5. Информацию о датафрейме также можно почерпнуть,
# прописав функцию describe. Эта функция позволяет
# получить статистические данные: найти минимальные,
# максимальные и средние значения, количество и т.д.
# Для этого прописываем:
print("Статистические данные о датасете")
print(df.describe())
#Также с помощью функций можно выводить конкретную информацию,
# например, сведения из определённого столбца.
# Для этого используем название датафрейма (df) и название
# интересующего столбца. Прописываем:
print("Сведения из определённого столбца")
print(df["salary"])
#8. Чтобы вывести одновременно несколько столбцов, нужно названия
# столбцов заключить в двойные квадратные скобки и указать
# названия столбцов через запятую. Прописываем:
print("Сведения из нескольких столбцов")
print(df[["job_title", "salary"]])
#9. Также можно вывести не весь столбец, а определённую строку; для
# этого надо использовать функцию loc и указать индекс строки.
print("Вывод одной 1 строки")
print(df.loc[1])
#В результате в окне вывода мы видим всю информацию, которая есть
# в строке 56 по всем колонкам.

#10.  Если нас интересует не вся имеющаяся в строке информация, нужно
# выводить строку не по индексу, а с указанием номера строки и
# названием интересующего нас столбца в кавычках. Название столбца
# можно скопировать из предыдущего окна вывода. Прописываем:
print("Один показатель по конкретной строке (56) ")
print(df.loc[1, 'salary'])
#В результате мы получаем только один показатель по конкретной
# строке:


#11. Можно вывести информацию, отвечающую определённому условию.
# Например, нам необходимо найти в столбце Healthy life expectancy
# все показатели выше 0.7. Для этого необходимо написать:
print(df[df['salary'] > 1020000])
#Таким образом, в этой строке мы указали, что из датафрейма необходимо
# извлечь информацию из конкретного столбца, которая при этом
# подчиняется конкретному условию.
#В результате мы видим, что в анализируемом датафрейме всего 18 рядов
# отвечает этому условию.