import numpy as np

class PCA():
    def __init__(self,num_dim=None):
        self.num_dim = num_dim
        self.mean = np.zeros([1,784]) # means of training data
        self.W = None # projection matrix

    def fit(self,X):
        # normalize the data to make it centered at zero (also store the means as class attribute)
        self.mean = np.mean(X, axis=0)
        newX = X - self.mean
            
        # finding the projection matrix that maximize the variance (Hint: for eigen computation, use numpy.eigh instead of numpy.eig)
        cm = np.cov(newX)
        vals, vects = np.linalg.eigh(np.mat(cm))

        if self.num_dim is None:
            # select the reduced dimension that keep >90% of the variance
            arr = np.sort(vals)[-1::-1]
            arrSum = sum(arr)

            tmp = 0
            num = 0
            for i in arr:
                tmp+=i
                num+=1
                if tmp >= arrSum*.9:
                    self.num_dim = num
                    #print(tmp)
            self.num_dim = 784 # placeholder

        # determine the projection matrix and store it as class attribute
        self.W = None # placeholder

        # project the high-dimensional data to low-dimensional one
        X_pca = X # placeholder

        return X_pca, self.num_dim

    def predict(self,X):
        # normalize the test data based on training statistics

        # project the test data
        X_pca = X # placeholder

        return X_pca

    def params(self):
        return self.W, self.mean, self.num_dim
