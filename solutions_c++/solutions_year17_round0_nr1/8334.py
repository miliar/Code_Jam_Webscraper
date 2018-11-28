#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>
#include <bitset>
#include <queue>
#include <map>

using namespace std;

char buffer[1024];
char S[101];

class Estado {
  public:
  string S;
  int  dist;

  public:

    Estado(string T, int d){
       S = T;
       dist = d;
    }

    vector <Estado> vizinhos(int K){
        vector <Estado> res;
        int tam = S.size();

        for(int i = 0; i < tam-K+1;i++){
            Estado u(S, dist+1);
            for(int j = 0; j < K; j++){
                u.S[i+j] = u.S[i+j] == '-' ? '+' : '-';
            }
            res.push_back(u);
        }
        return res;
    }

    bool isFinal(){
        int tam = S.size();
        for(int i = 0; i < tam;i++){
            if(S[i]=='-') return false;
        }
        return true;
    }

};



int bfs(char S[], int K){

    queue <Estado> fila;

    map <string,bool> visitado;

    string inicio(S);

    Estado estadoInicial(inicio,0);

    fila.push(estadoInicial);

    while( !fila.empty() ){

        Estado u = fila.front();

        fila.pop();

        //cout << "string " << u.S << "  dist " << u.dist << endl;

        if( u.isFinal() ){
            return u.dist;
        }

        visitado[u.S] = true;

        vector <Estado> Vizinhos = u.vizinhos(K);

        for(int i = 0; i < Vizinhos.size(); i++){
            if( !visitado[ Vizinhos[i].S ] ){
                fila.push( Vizinhos[i] );
            }
        }

    }

    return -1;
}


int main(){

    int K;
    int n;
    int T;
    int res;

    scanf("%d ", &T);

    for(int i = 0; i < T; i++){

        gets(buffer);

        sscanf(buffer, "%s %d", S, &K);

        res = bfs(S, K);

        if(res >= 0)
            printf("Case #%d: %d\n", i+1, res);
        else
            printf("Case #%d: IMPOSSIBLE\n", i+1);
    }

}
