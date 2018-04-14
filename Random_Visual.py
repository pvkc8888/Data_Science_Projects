import random
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import matplotlib.style as style


style.use('fivethirtyeight')

figure, (axes) = plt.subplots(1, figsize=(32, 18))
listt = [0] * 100


def new_listt():
    rand = random.randint(1, 100)
    listt[rand - 1] += 1
    summ = sum(listt)
    print(summ)
    newlistt = [x / sum(listt) for x in listt]
    list1 = np.array(listt)
    maxx = max(list1)
    max_list = np.where(list1 == maxx)[0]
    max_list = [str(x + 1) for x in max_list]
    print(max_list)
    return newlistt, summ, rand, max_list


def animate(i):
    updatedlist, summ, rand, max_list = new_listt()
    axes.clear()
    axes.bar(np.arange(1, 101), updatedlist, color='red', alpha=0.75)
    axes.axis()
    plt.xticks(np.arange(1, 101, 1), fontsize=10, rotation=90)
    plt.xlabel('Number')
    plt.ylabel('Normalized Frequency')
    ylabel = axes.get_ylim()
    t1 = 'Number of iterations = ' + str(summ)
    t2 = 'Random number = ' + str(rand)
    t3 = 'Highest Frequency = '
    numbers = ', '.join(max_list)
    t3 += numbers
    plt.text(60, ylabel[1] - ylabel[1] // 10, t1, ha='right', wrap=True)
    plt.text(80, ylabel[1] - ylabel[1] // 50, t2, ha='right', wrap=True)
    plt.text(40, ylabel[1] - ylabel[1] // 50, t3, ha='right', wrap=True)


animate = animation.FuncAnimation(figure, animate, frames=100, interval=500)

plt.show()
