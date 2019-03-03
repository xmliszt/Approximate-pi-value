import random
from math import pow
import matplotlib.pyplot as plt

def pi_approx_monte_carlo(n,stored_value = []):
    raindrop = (random.uniform(-0.5,0.5), random.uniform(-0.5,0.5)) # take value from -0.5 to 0.5
    x = raindrop[0]
    y = raindrop[1]
        #print(x,y)
    if  pow(x,2) + pow(y,2) <= 0.25:
        x_reservoir.append(x)
        y_reservoir.append(y)
        stored_value.append(1)
    else:
        x_out.append(x)
        y_out.append(y)
    return stored_value

def define_graph(length_of_field = 1):
    plt.xlim(-length_of_field / 2, length_of_field / 2)
    plt.ylim(-length_of_field / 2, length_of_field / 2)

def plot_graph(x_in =[], y_in =[], x_out=[], y_out=[], num_of_drops = 0, pi_value = 0):
    ax.scatter(x_in, y_in, color='green', alpha = 0.7, label="Drops in circle")
    ax.scatter(x_out, y_out, color='red', alpha = 0.7, label="Drops out of circle")
    plt.title("Total %s drops: %s are in the circle, estimating $\pi$ as %.7f." % (num_of_drops, len(x_in), pi_value))
    plt.legend(loc = "center")
    #plt.savefig("%s_drops.%s" % (num_of_drops, 'jpg'))
    #plt.show()

status = True
while status:
    try:
        user_input = int(input("Number of raindrops to be simulated: "))
        plt.ion()
        fig, ax = plt.subplots(clear = True)
        status = False
        x_reservoir, y_reservoir, x_out, y_out = list(), list(), list(), list()
        storage = list()
        for k in range(user_input):
            count = len(pi_approx_monte_carlo(k+1, stored_value= storage))
            pi = 4*count/(k+1)
            define_graph()
            plot_graph(x_in =x_reservoir, y_in =y_reservoir, x_out=x_out, y_out=y_out, num_of_drops = k+1, pi_value = pi)   
            plt.draw()
            plt.pause(0.001)
            plt.cla()
            #ax.cla()
        ax.grid(True)
        plt.waitforbuttonpress()
    except Exception as e:
        print("Please key in a valid integer!")
        print(e)
        status = True
