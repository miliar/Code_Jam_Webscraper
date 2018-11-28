#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <utility>
#include <climits>
using namespace std;

struct Estado{
    string S;
    int giros;
    int indice;
    Estado(string S1, int giros1, int indice1):
        S(S1), giros(giros1), indice(indice1){}
    Estado(){}
};

bool feliz(string &S){
    for(int i=0; i<(int)S.size(); i++){
        if( S[i]=='-' ) return false;
    }
    return true;
}

string flip(string S, int inicio, int fin){
    while( inicio<fin ){
        S[inicio] = (( S[inicio]=='+')? '-': '+');
        inicio++;
    }
    return S;
}

int salvado(char x){
    if( x=='+' ) return 1;
    return 0;
}

void voltear(string &S, int K){
    queue < Estado > q;
    map < string , bool > Mapa;
    
    q.push( Estado(S, 0, -1));
    Mapa[ S ] = true;
    
    // búsqueda
    while(!q.empty()){
        Estado now = q.front();
        q.pop();
        
        //cout << now.S << " " << now.giros << " " << now.indice+1 << endl;
        if( feliz(now.S) ){
            cout << now.giros << endl;
            return;
        }
        
        if( now.indice==-1 ){
            if( now.S[0]=='+' ){
                q.push( Estado( now.S, now.giros, now.indice+1 ));
                //cout << now.S << " " << now.giros << " " << now.indice+1 << endl;
            }else{
                q.push( Estado( flip( now.S, 0, K), now.giros+1, now.indice+1));
                //cout << flip( now.S, 0,K) << " " << now.giros+1 << " " << now.indice+1 << endl;
            }
        }else{
            if( now.S[now.indice+1]=='+' ){
                // ¡Ya lo salve maldita sea!
                q.push( Estado( now.S, now.giros, now.indice+1 ));
                //cout << now.S << " " << now.giros << " " << now.indice+1 << endl;
            }else{
                for(int i=now.indice+1; i<=(int)(S.size()-K); i++){
                    string aux = flip( now.S, i, K+i);
                    if( !Mapa[ aux ] and aux[now.indice+1]=='+' ){
                        //cout << aux << " " << now.giros + 1 << " " << now.indice+1 << endl;
                        q.push( Estado( aux, now.giros+1, now.indice+1));
                        Mapa[ aux ] = true;
                    }
                }
            }
        }
        //cout << endl;
    }
    cout << "IMPOSSIBLE\n";
    while(!q.empty()) q.pop();
    Mapa.clear();
}

int main(){
    int T;
    cin >> T;
    for(int i=1; i<=T; i++){
        string S; int K;
        cin >> S >> K;
        printf("Case #%d: ",i);
        voltear( S,K);
    }
    return 0;
}



