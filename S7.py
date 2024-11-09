def main():
    squareReorder = [0,0,2,4,0,5,2,10,4,0,10,2,5,11,14]
    classSize = [1,21,70,210,105,504,420,840,630,105,280,210,504,420,720]
    centralizerSize = [5040,240,72,24,48,10,12,6,8,48,18,24,10,12,7]
    X = list(range(15))
    X[0] = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    X[1] = [1,-1,1,-1,1,1,-1,-1,1,-1,1,1,-1,-1,1]
    X[2] = [6,4,3,2,2,1,1,0,0,0,0,-1,-1,-1,-1]
    X[3] = elemProd(X[2],X[1])
    X[4] = Xa(X[2],squareReorder)
    X[5] = elemProd(X[4],X[1])
    X[6] = elemDif(Xs(X[2],squareReorder),elemSum(X[0],X[2]))
    X[7] = elemProd(X[6],X[1])

    x24Norm = elemDif(elemProd(X[2],X[4]),ElemSum([X[2],X[4],X[6]])) # X_x + X_y
    x26Norm = elemDif(elemProd(X[2],X[6]),ElemSum([X[2],X[4],X[6]])) # X_y + X_z
    x46Norm = elemDif(elemProd(X[4],X[6]),ElemSum([X[2],X[4],X[4],X[6],x26Norm,x24Norm])) # X_q + x_r
    X3pow3N = elemDif(elemPow(X[2],3),ElemSum([X[0],elemMult(X[2],4),elemMult(X[4],3),elemMult(X[6],3)])) # X_x + 2 X_y + X_z = x24Norm+x26Norm = x24p26

    X[8] = elemMult(elemDif(elemPow(X[2],4),ElemSum([elemMult(X[0],4),elemMult(X[2],11),elemMult(X[4],13),X[5],elemMult(X[6],13),elemMult(X3pow3N,6),elemMult(x46Norm,3)])),.5)
    X[9] = elemProd(X[8],X[1])
    X[10] = elemDif(x46Norm,X[9])
    X[11] = elemProd(X[10],X[1])
    X[12] = elemDif(x24Norm,X[11])
    X[13] = elemDif(x26Norm,X[11])
    X[14] = elemProd(X[13],X[1])

    for i in range(len(X)):
        print(i,X[i], InnerProduct(X[i],X[i],centralizerSize) if type(X[i])==list else X[i])

    print("--------------")

    Y = [X[0],X[1],X[2],X[3],X[13],X[14],X[6],X[7],X[4],X[5],X[12],X[8],X[9],X[10],X[11]]
    for i in range(len(Y)):
        print(i,Y[i], InnerProduct(Y[i],Y[i],centralizerSize) if type(X[i])==list else X[i])

    print("--------------")

    orth = [[0 for i in range(len(X))] for j in range(len(X))]
    for i in range(len(X)):
        for j in range(len(X)):
            orth[i][j] = round(InnerProduct(X[i],X[j],centralizerSize))
    for i in orth:
        print(i)
        

def InnerProduct(xi,xj,sizes):
    return sum(elemDiv(elemProd(xi,xj),sizes))

def Xs(x,re):
    return [int(i) for i in elemProd([.5 for i in range(15)] ,elemSum(elemProd(x,x),Reorder(x,re)))]

def Xa(x,re):
    return [int(i) for i in elemProd([.5 for i in range(15)] ,elemDif(elemProd(x,x),Reorder(x,re)))]

def Reorder(x,re):
    return [x[re[i]] for i in range(len(x))]

def elemProd(xi,xj):
    return [xi[i]*xj[i] for i in range(len(xi))]

def elemPow(x,n):
    return [x[i]**n for i in range(len(x))]

def elemMult(x,n):
    return [int(x[i]*n) for i in range(len(x))]

def elemDiv(xi,xj):
    return [xi[i]/xj[i] for i in range(len(xi))]

def elemSum(xi,xj):
    return [xi[i]+xj[i] for i in range(len(xi))]

def ElemSum(X):
    return [sum([X[j][i] for j in range(len(X))]) for i in range(len(X[0]))]

def elemDif(xi,xj):
    return [xi[i]-xj[i] for i in range(len(xi))]

def printInfo(x,X,cenSize):
    inner = round(InnerProduct(x,x,cenSize))
    sumOfInner = round(sum([round(InnerProduct(x,X[i],cenSize)) for i in range(12)]))
    print(x)
    print(inner,sumOfInner, inner-sumOfInner)
main()