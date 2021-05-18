#Importação da biblioteca reactiveX
from rx import create, operators

#Função para emissão dos dados pelo o Observável
def frequency(observer1, scheduler):
    #Para cada chamada da função ON_NEXT um item é emitido. Os valores passados por parâmetro são referentes a quantidade de presenças do aluno
    observer1.on_next(90)
    observer1.on_next(-22)
    observer1.on_next(68)
    observer1.on_next(-70)
    observer1.on_next(181)
    observer1.on_next(150)
    observer1.on_next(50)
    observer1.on_next(70)
    observer1.on_next(80)
    observer1.on_next(40)
    #A Função ON_COMPLETE é chamada quando não tem mais itens a serem emitidos
    observer1.on_completed()

#A função "create" cria um observável que transmitirá os dados pela função "frequency"
observable_1 = create(frequency)

#O framework reactiveX permite a criação de conjunto de operadores a serem aplicados nos stream's criados
conjunto1 = observable_1.pipe(
    #O operador "filter" restringe os dados que são passados, baseado no filtro aplicado, 0 = Quantidade mínima de presenças e 180 é quantidade máxima
    operators.filter(lambda i: i >=0 and i <=180),
)

#No conjunto 2, temos além do filtro do conjunto 1, o operador MAP que permite a manipulação dos dados da fonte
conjunto2 = observable_1.pipe(
    operators.filter(lambda i: i >=0 and i <=180),
    #Manipulação para transformar os dados quantitativos de presença em percentual
    operators.map(lambda j: (j * 100)/180)
)

#No conjunto 3, além de incrementar os operadores do conjunto 1 e 2, também aplica mais um filtro para permitir a emissão dos dados segundo o critério estabelecido
conjunto3 = observable_1.pipe(
    operators.filter(lambda i: i >=0 and i <=180),
    operators.map(lambda j: (j * 100)/180),
    operators.filter(lambda k: k > 75)
)

#A função "subscribe" exibe os dados partindo do consumo dos operadores no conjunto especificado
#Para exibir separadamente o consumo dos operadores para cada conjunto, basta remover o comentário um de cada vez

#Para o conjunto 1
conjunto1.subscribe(
    on_next = lambda i: print("Aluno Aprovado com Média {0}".format(i)),
    on_error = lambda e: print("ERRO: {0}".format(e)),
    on_completed = lambda: print("Concluído!"),
)

#Para o conjunto 2
'''conjunto2.subscribe(
    on_next = lambda i: print("Aluno Aprovado com Média {0} %".format(i)),
    on_error = lambda e: print("ERRO: {0}".format(e)),
    on_completed = lambda: print("Concluído!"),
)'''

#Para o conjunto 3
'''conjunto3.subscribe(
    on_next = lambda i: print("Aluno Aprovado com Média {0} %".format(i)),
    on_error = lambda e: print("ERRO: {0}".format(e)),
    on_completed = lambda: print("Concluído!"),
)'''