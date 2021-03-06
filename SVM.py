import numpy as np
from matplotlib import pyplot as plt

#Step 1 - Define our data

#Input data - Of the form [X value, Y value, Bias term]
X = np.array([
    [-2,4,-1],
    [4,1,-1],
    [1, 6, -1],
    [2, 4, -1],
    [6, 2, -1],
])

#Associated output labels
y = np.array([-1,-1,1,1,1])

#lets plot these examples on a 2D graph!
#for each example
for d, sample in enumerate(X):
    print(d,sample)
    if y[d] < 0:
        plt.scatter(sample[0], sample[1], s=120, marker='_', linewidths=2)
    else:
        plt.scatter(sample[0], sample[1], s=120, marker='+', linewidths=2)
plt.show()

# lets perform stochastic gradient descent to learn the seperating hyperplane between both classes

def svm_sgd_plot(X, Y, epochs):
    # Initialize our SVMs weight vector with zeros (3 values)
    w = np.zeros(len(X[0]))
    # The learning rate
    eta = 1
    # how many iterations to train for
    # store misclassifications so we can plot how they change over time
    error = 0
    errors = []
    # training part, gradient descent part
    for epoch in range(1, epochs):
        for i, x in enumerate(X):
            # misclassification
            if (Y[i] * np.dot(X[i], w)) < 1:
                # misclassified update for ours weights
                w = w + eta * ((X[i] * Y[i]) + (-2 * (1 / epoch) * w))
                error += 1
            else:
                # correct classification, update our weights
                w = w + eta * (-2 * (1 / epoch) * w)
        errors.append(error)

    # lets plot the rate of classification errors during training for our SVM
    plt.plot(errors)
    plt.xlabel('Epoch')
    plt.ylabel('Misclassified')
    plt.show()
    return w

w = svm_sgd_plot(X, y, epochs=10000000)


for d, sample in enumerate(X):
    # Plot the negative samples
    if y[d] < 0:
        plt.scatter(sample[0], sample[1], s=120, marker='_', linewidths=2)
    # Plot the positive samples
    else:
        plt.scatter(sample[0], sample[1], s=120, marker='+', linewidths=2)

# Add our test samples
# plt.scatter(2,2, s=120, marker='_', linewidths=2, color='yellow')
# plt.scatter(4,3, s=120, marker='+', linewidths=2, color='blue')

# Print the hyperplane calculated by svm_sgd()

x2=[w[0],w[1],-w[1],w[0]]
x3=[w[0],w[1],w[1],-w[0]]

x2x3 =np.array([x2,x3])
X,Y,U,V = zip(*x2x3)
ax = plt.gca()
ax.quiver(X,Y,U,V,scale=1, color='blue')
plt.show()

# END