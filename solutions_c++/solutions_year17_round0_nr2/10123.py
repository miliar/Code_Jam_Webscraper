#include <iostream>
#include <algorithm>
#include <queue>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <climits>
#include <stack>
#include <map>
using namespace std;

typedef unsigned long long int ulli;
vector < int > v;

void ini(){
    
    queue < int > q;
    // Números origen
    v.push_back(0);
    for(int i=1; i<=9; i++){
        v.push_back(i);
        q.push(i);
    }
    
    int numeros = 9;
    // Hacer numeros tidy
    while(!q.empty()){
        if( numeros==1002 ) break;
        int now = q.front();
        q.pop();
        
        //cout << now << " ";
        
        int digit = now%10;
        for( ; digit<=9; digit++){
            int aux = now*10 + digit;
            q.push(aux);
            v.push_back(aux);
        }
        numeros++;
    }
    // Vaciar
    while(!q.empty()) q.pop();
    //cout << endl;
}

int bs(int inicio, int fin, int X){
    
    while( inicio <= fin ){
        int mitad = (inicio+fin)/2;
        if( v[mitad]==X ) return v[mitad];
        if( v[mitad-1]<=X and X<=v[mitad] ) return v[mitad-1];
        if( v[mitad]>X ) fin = mitad;
        else inicio = mitad+1;
    }
    
    return -1;
}

int main(){
    ini();
    int T,N;
    cin >> T;
    for(int i=1; i<=T; i++){
        cin >> N;
        printf("Case #%d: %d\n", i, bs(0,(int)v.size(),N));
    }
    return 0;
}
