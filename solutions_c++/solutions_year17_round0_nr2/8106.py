#include <iostream>
#include "bits/stdc++.h"
#include "string.h"

using namespace std;

bool cert = true;



unsigned long long int T,y,soma,tamanho,atuali;
 
int main(){
	string numero;
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cin >> T;
 
    for(int y = 1; y <= T; ++y){
        cin >> numero;
        tamanho = numero.size();  
        cert = true;
  
        for(int z=tamanho-1;z > 0;--z){
 
            for(int j = z;j > 0;j--)
                if(numero[z]<numero[z-1]){
                    numero[z-1] -= 1;
                    
              for(int k=j;k<tamanho;++k)
                        numero[k]='9';
  }
 
    }
		 cout<<"Case #"<<y<<": ";
        bool inicio = true;
        for(int z = 0 ; z < tamanho; ++z){
 
            if(numero[z] != '0')
             inicio=false;
 
            if(!inicio)
                cout << numero[z];
        }
       
        cout << endl;
    }
 
    return 0;
}
 