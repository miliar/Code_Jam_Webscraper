import sys

def go_for_a_ride(rides,size_of_ride,number_of_groups,groups):
    money = 0
    i = 0
    viagem_atual = size_of_ride
    primeiro_passageiro = 1
    posicao_do_primeiro_passageiro = 0
    while rides > 0:
        if int(groups[i]) <= viagem_atual:
            if primeiro_passageiro == 1:
                viagem_atual = viagem_atual - int(groups[i])
                money = money + int(groups[i])
                posicao_do_primeiro_passageiro = i
                i = i + 1
                i = i % number_of_groups
                primeiro_passageiro = 0
            else:
                if posicao_do_primeiro_passageiro != i:
                    viagem_atual = viagem_atual - int(groups[i])
                    money = money + int(groups[i])
                    i = i + 1
                    i = i % number_of_groups
                else:
                    rides = rides - 1
                    viagem_atual = size_of_ride
                    primeiro_passageiro = 1
        else:
            rides = rides - 1
            viagem_atual = size_of_ride
            primeiro_passageiro = 1
    return money
    

def prepare_to_go_for_a_ride(arquivo):
    file = open (arquivo,"r")
    resultado = open ("result.out","w")
    sys.stdout = resultado
    numero_de_casos = int(file.readline())
    for i in range(numero_de_casos):
        (rides,size_of_ride,number_of_groups)=file.readline().split()
        rides = int(rides)
        size_of_ride = int(size_of_ride)
        number_of_groups = int(number_of_groups)
        groups = file.readline().split()
        dinheiro = go_for_a_ride(rides,size_of_ride,number_of_groups,groups)
        print "Case #%i: %s" % (i+1,dinheiro)

if __name__ == "__main__":
    prepare_to_go_for_a_ride(sys.argv[1])
    
