import math
truth_table = {
    (0,0):0,
    (0,1):0,
    (1,0):0,
    (1,1):1
}

def predict(w1,w2,b,x1,x2):
    z = x1*w1+x2*w2+b
    probability = 1/(1+math.exp(-z))                # sigmoid activation function
    predicted = 1 if probability > 0.5 else 0       
    return (probability, predicted)

#Initial weight and bias
w1 = 0      
w2 = 0
b = 0

#initial Loss
loss = 0

def test():
    global w1, w2, b
    completed = True
    for i in truth_table:                                                               #training epoch i
        x1 = i[0]
        x2 = i[1]
        probability, y_cap = predict(w1,w2,b,x1,x2)                                     
        y = truth_table[i]
        loss = -(y * math.log(probability) + (1-y) * math.log(1-probability))           #calculating loss
        if loss > .1 or y != y_cap:
            
            error = probability-y                                                       #calculating error
            
            # updating weight and bias

            dw1 = error*x1                      
            dw2 = error*x2
            db = error
            w1 -= .1*dw1
            w2 -= .1*dw2
            b -= .1*db 
            completed =  False
            
    return completed

def startTaining():
    i = 1
    max_epoch = 1000
    while i < max_epoch:
        print("Epoch ",i)
        if test():
            print("Training completed")
            return
        i+=1
    print("Training did not converge")
    


if __name__ == '__main__':
    startTaining()
    print("W1: ",w1,"w2: ",w2,"b: ",b)
    
    while True:
        print("Test Yourself 'ctrl+c' to exit :")
        x1 = int(input("x1: "))
        x2 = int(input("x2: "))
        print("Prediction: ",predict(w1,w2,b,x1,x2)[1],"With confidence: ",predict(w1,w2,b,x1,x2)[0])
