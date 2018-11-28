#include<iostream>
#include<string>
#include<stdlib.h>
using namespace std;

int main(){
    int T,K,tam,post = 0, cont,cases = 0,casos;
    string S;
    cin >> T;
    while (T != cases){
        cin >> S;
        cin >> K;
        casos = 0;
        tam = S.size();
        for(int x = 0; x < tam; x++){
            int cont = K - 1;
            if(S[x] == 45){
                while (cont != -1){
                    if (S[x + cont] == 45){
                        if(x + cont < tam){
                            S[x + cont] = 43;
                            cont--;
                        }
                        else
                            cont = -1;
                    }
                    else{
                        if (x + cont < tam){
                            S[x + cont] = 45;
                            cont--;
                        }
                        else
                            cont = -1;
                    }
                }
                casos++;
            }
            
        }
        for(int x = 0; x < tam;x++){
            if( S[x] == 43){
                post++;
            }
        }
        if(post == tam)
            cout << "Case #"<< cases + 1 <<": "<<casos<<endl;
        else
            cout << "Case #"<< cases + 1 <<": IMPOSSIBLE"<<endl;
        cases++;
        post = 0;
    }
    return 0;
}