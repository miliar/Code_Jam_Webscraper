#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>

using namespace std;

int T, i, n, K, ER[1024][1024], k, ni, g, h, t;
string linha;

void preparaMatriz(){
    ni = 1;
    for(k = K; k < n; ++k){
        g = 0;
        while(g < K){
            ER[k - g][ni] = 1;
            ++g;
        }
        ++ni;
    }
    h = ni;
    for(k = 1; k < n; ++k){
        if(linha[k] == '+'){
            ER[k][h] = 0;
        }else{
            ER[k][h] = 1;
        }
    }
}

void imprimeMatriz(){
    for(k = 1; k < n; ++k){
        for(g = 1; g < h + 1; ++g){
            cout << ER[k][g] << " ";
        }
        cout << endl;
    }
    cout << endl;
}

void escalonaMatriz(){
    for(k = 1; k < n; ++k){
        for(g = k + 1; g < n; ++g){
            if(ER[g][k] == 1){
                for(t = 1; t < h + 1; ++t){
                    ER[g][t] -= ER[k][t];
                }
            }
        }
    }
}

bool verificaImpossibilidade(){
    for(k = 1; k < h; ++k){
        if(ER[k][h] < 0)    ER[k][h] *= -1;
        ER[k][h] %= 2;
        if(ER[k][k] == 0){
            if(ER[k][h] == 1)   return true;
        }
    }
    for(; k < n; ++k){
        if(ER[k][h] < 0)    ER[k][h] *= -1;
        ER[k][h] %= 2;
        if(ER[k][h] % 2 == 1)   return true;
    }
    return false;
}

int calculaResposta(){
    t = 0;
    for(k = 1; k < h; ++k){
        t += ER[k][h];
    }
    return t;
}

int main(){
    cin >> T;

    for(i = 0; i < T; ++i){
        cin >> linha >> K;
        linha = "*" + linha;

        n = linha.length();

        memset(ER, 0, sizeof(ER));
        preparaMatriz();
        //imprimeMatriz();
        escalonaMatriz();
        //imprimeMatriz();

        cout << "Case #" << i + 1 << ": ";
        if(verificaImpossibilidade()){
            cout << "IMPOSSIBLE" << endl;
        }else{
            cout << calculaResposta() << endl;
        }
        //imprimeMatriz();
    }
}
