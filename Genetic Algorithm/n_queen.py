# here we are going to use the same concept to place N queen in a N X N board in a way no 2 queen attack each other
import random



def individual():
    return [random.randint(0,n-1) for _ in range(n)]

def fitness(board):
    fitness_score = 0
    for q1 in range(len(board)):
        conflict = False
        for q2 in range(len(board)):
            if q1 == q2:
                continue
            if board[q2] == board[q1]:
                conflict = True
            if board[q2]-q2 == board[q1]-q1:
                conflict = True
            if board[q2]+q2 == board[q1]+q1:
                conflict = True

        if not conflict:
            fitness_score+=1
    return fitness_score


def mutate(kid):
    return [random.randint(0,n-1) if random.random() <= mutate_rate else c for c in kid]

def crossover(parent1,parent2):
    p = random.randint(1,n-1)
    kid = parent1[:p]+parent2[p:]
    return kid

def display(board):
    for i in range(n):
        for j in range(n):
            if j == board[i]:
                print('Q',end=" ")
            else:
                print(".",end=" ")
        print()


def evolve():
    new_pop = [individual() for _ in range(population)]
    gen = 0
    while True:
        gen += 1
        fittest1 = [[],-1]
        fittest2 = [[],-1]
        pop = new_pop
        for i in pop:
            if i == fittest1[0] or i == fittest2[0]:
                continue
            fitness_score = fitness(i)
            if fitness_score > fittest1[1]:
                fittest2 = fittest1
                fittest1 = [i,fitness_score]
            elif fitness_score > fittest2[1]:
                fittest2 = [i,fitness_score]
        print(f"gen {gen} fitness {fittest1[1]}")
        display(fittest1[0])
        if fittest1[1] == n:
            print("Total evaluations:", gen * population)
            break

        new_pop = [mutate(crossover(fittest1[0],fittest2[0])) for _ in range(population)]

if __name__ == "__main__":
    n = int(input("Enter N N x N board: "))
    population = 500
    mutate_rate = 1/n
    evolve()