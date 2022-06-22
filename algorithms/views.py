from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import numpy as np
import pandas as pd
import random as rd
from random import randint


def index(request):
    if request.method == 'GET' and 'ben1' in request.GET:
        ben1 = float(request.GET.get('ben1'))
        ben2 = float(request.GET.get('ben2'))
        ben3 = float(request.GET.get('ben3'))
        ben4 = float(request.GET.get('ben4'))
        ben5 = float(request.GET.get('ben5'))
        ben6 = float(request.GET.get('ben6'))
        ben7 = float(request.GET.get('ben7'))
        wei1 = float(request.GET.get('wei1'))
        wei2 =float(request.GET.get('wei2'))
        wei3 = float(request.GET.get('wei3'))
        wei4 = float(request.GET.get('wei4'))
        wei5 = float(request.GET.get('wei5'))
        wei6 = float(request.GET.get('wei6'))
        wei7 = float(request.GET.get('wei7'))
        maximum = int(request.GET.get('maximum'))
        item_number = np.arange(1,8) # list of items number 1 2 .....6 7
        knapsack_threshold = maximum    #max weight
        weight=[]  # weights list
        weight.append(wei1) # add  new weight to list
        weight.append(wei2)
        weight.append(wei3)
        weight.append(wei4)
        weight.append(wei5)
        weight.append(wei6)
        weight.append(wei7)
        value=[] # values list
        value.append(ben1) # add  new value to list
        value.append(ben2)
        value.append(ben3)
        value.append(ben4)
        value.append(ben5)
        value.append(ben6)
        value.append(ben7)
        solutions_per_pop = 4 #
        pop_size = (solutions_per_pop, item_number.shape[0])
        initial_population = np.random.randint(2, size = pop_size) #Generate random population of n chromosomes 
        initial_population = initial_population.astype(int)
        num_generations = 50
        def cal_fitness(weight, value, population, threshold):#fitness function weight, cost, weight_limit,
            # chromosome
                fitness = np.empty(population.shape[0]) #empty 
                for i in range(population.shape[0]): #for
                    S1 = np.sum(population[i] * value) 
                    S2 = np.sum(population[i] * weight)
                    if S2 <= threshold:#if
                        fitness[i] = S1
                    else :
                        fitness[i] = 0 #end if
                return fitness.astype(int)  #end for #fitness
        def selection(fitness, num_parents, population):#roulette selection based on fitness score 
                fitness = list(fitness)
                parents = np.empty((num_parents, population.shape[1]))
                for i in range(num_parents):
                    max_fitness_idx = np.where(fitness == np.max(fitness))
                    parents[i,:] = population[max_fitness_idx[0][0], :]
                    fitness[max_fitness_idx[0][0]] = -999999 #selected parents
                return parents #select population and fitness, perform roulette selection via probability 
        def crossover(parents, num_offsprings):#num_offsprings= probability for crossover
                offsprings = np.empty((num_offsprings, parents.shape[1]))
                crossover_point = int(parents.shape[1]/2)
                crossover_rate = 0.8
                i=0
                while (parents.shape[0] < num_offsprings):
                    parent1_index = i%parents.shape[0]
                    parent2_index = (i+1)%parents.shape[0]
                    x = rd.random()
                    if x > crossover_rate:
                        continue
                    parent1_index = i%parents.shape[0]
                    parent2_index = (i+1)%parents.shape[0]
                    offsprings[i,0:crossover_point] = parents[parent1_index,0:crossover_point]
                    offsprings[i,crossover_point:] = parents[parent2_index,crossover_point:]
                    i=+1
                return offsprings    #returning the crossover childs 
        def mutation(offsprings):# With a mutation probability
            mutants = np.empty((offsprings.shape))
            mutation_rate = 0.4
            for i in range(mutants.shape[0]):
                random_value = rd.random()
                mutants[i,:] = offsprings[i,:]
                if random_value > mutation_rate:
                    continue
                int_random_value = randint(0,offsprings.shape[1]-1)    
                if mutants[i,int_random_value] == 0 :
                    mutants[i,int_random_value] = 1
                else :
                    mutants[i,int_random_value] = 0
            return mutants  #mutattion of bits from 1 to 0 and 0 to 1 based on probability 
        def optimize(weight, value, population, pop_size, num_generations, threshold):
            parameters, fitness_history = [], []
            num_parents = int(pop_size[0]/2)
            num_offsprings = pop_size[0] - num_parents 
            for i in range(num_generations):
                fitness = cal_fitness(weight, value, population, threshold)#parents based on fitness
                fitness_history.append(fitness)#adding new parents to mutated list to make orignal pop size
                parents = selection(fitness, num_parents, population)#do selection
                offsprings = crossover(parents, num_offsprings)#do crossover
                mutants = mutation(offsprings)#do mutation
                population[0:parents.shape[0], :] = parents
                population[parents.shape[0]:, :] = mutants
            fitness_last_gen = cal_fitness(weight, value, population, threshold)  
            max_fitness = np.where(fitness_last_gen == np.max(fitness_last_gen))
            parameters.append(population[max_fitness[0][0],:])
            return parameters, fitness_history 
        parameters, fitness_history = optimize(weight, value, initial_population, pop_size, num_generations, knapsack_threshold) 
        selected_items = item_number * parameters
        myresult=" "
        for i in range(selected_items.shape[1]):
              if selected_items[0][i] != 0:
                  myresult=myresult+'{}\n'.format(selected_items[0][i])+"<br>"
        #printknapSack(W, wt, val, n):
        
        val = value 
        wt = weight 
        W=maximum
        n = len(value)
        K = [[0 for w in range(W + 1)]
                for i in range(n + 1)]
                
        # Build table K[][] in bottom
        # up manner
        
        for i in range(n + 1):
            for w in range(W + 1):
                if i == 0 or w == 0:
                    K[i][w] = 0
                elif wt[i - 1] <= w:
                    K[i][w] = max(val[i - 1]
                    + K[i - 1][int(w - wt[i - 1])],
                                K[i - 1][w])
                else:
                    K[i][w] = K[i - 1][w]

        # stores the result of Knapsack
        res = K[n][W]
        
        
        w = W
        mystr=""
        for i in range(n, 0, -1):
            if res <= 0:
                break
            # either the result comes from the
            # top (K[i-1][w]) or from (val[i-1]
            # + K[i-1] [w-wt[i-1]]) as in Knapsack
            # table. If it comes from the latter
            # one/ it means the item is included.
            if res == K[int(i - 1)][ int(w)]:
                continue
            else:

                # This item is included.
                mystr= mystr +str( i)+"  "
                
                # Since this weight is included
                # its value is deducted
                res = res - val[int(i - 1)]
                w = w - wt[int(i - 1)]
        return JsonResponse(
            {
                'result' :"<h2>Knapsack holds a maximum of : "+ str(maximum) +"</h2><br>"
                +"<h2>Genetic Algorithm :</h2><br>"
                +'Population size = {}'.format(pop_size)+"<br>"
                +'Initial population: \n{}'.format(initial_population)+"<br>"
                +'The optimized parameters for the given inputs are: \n{}'.format(parameters)+"<br>"
                +'\nSelected items that will maximize the knapsack without breaking it:'+"<br>"
                +myresult+"<br>"
                +"<h2>Dynamic Programming Algorithm :</h2><br>"
                
                +"item number:" +mystr+"<br>"
           ,     
            },
            status=200,
        )

    return render(
        request,
        'main.html'
    )
