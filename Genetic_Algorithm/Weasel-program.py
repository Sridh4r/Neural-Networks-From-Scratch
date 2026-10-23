# Works based on survival of the fittest

import string, random


population_size = 500

characters = string.ascii_lowercase + " "


def individual():
    return "".join([random.choice(characters) for _ in range(len(target))])

def fitness_score(s):
    score = 0
    for i in range(len(s)):
        if s[i] == target[i]:
            score+=1
    return score

def crossover(parent1, parent2):
    p = random.randint(1,len(target)-1)
    kid = parent1[:p]+parent2[p:]
    return kid

def mutate(s):
    return "".join(
                random.choice(characters) if random.random() <= mutation_rate else c 
                for c in s
            )

def evolve():
    fittest1 = ("",-1)
    fittest2 = ("",-1)
    
    gen = 0
    new_pop = [individual() for _ in range(population_size)]
    while True:
        breeding_pool = []
        gen+=1
        pop = new_pop
        for i in pop:
            if i == fittest1[0]:
                continue
            score = fitness_score(i)
            breeding_pool.append((i,score))
        breeding_pool = sorted(breeding_pool , key= lambda x :x[1] , reverse= True)
        print(f"gen {gen} | {breeding_pool[0][0]} | fittness {breeding_pool[0][1]}/{len(target)}")
        if breeding_pool[0][0] == target:
            print(f"total evolution {gen*population_size}")
            break
        breeding_pool = breeding_pool[:31]
      
        new_pop = [mutate(crossover(random.choice(breeding_pool)[0],random.choice(breeding_pool)[0])) for _ in range(population_size)]


if __name__ == "__main__":
    valid = False
    while not valid:
        target = input("Enter your String (a-z): ")
        target = target.lower()
        if len(target)<2:
            print("Enter atleast 2 character")
            continue
        for i in target:
            if i not in characters:
                print("Invalid character")
                break
        else:
            valid = True

    mutation_rate = 1/len(target)
    evolve()