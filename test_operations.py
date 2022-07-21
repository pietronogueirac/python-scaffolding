import operations

def test_operacoes(x=5): 
    
    var1 = operations.potencialidade(x)
    var = operations.raiz_quadrada(var1)
    assert x == var

def test_operacoes_2(x,y):

    var = operations.soma(x=-5,y=2)
    var1 = operations.diminuicao(var,y)

    assert x == var1



def test_operacoes_3(x=10,y=4):

    var = operations.multiplicao(x,y)
    var1 = operations.divisão(var,y)

    assert x == var1

if __name__ == "__main__":
    test_operacoes(5)
    test_operacoes_2(5,2)
    test_operacoes_2(10,4)