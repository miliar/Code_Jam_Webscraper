//
//  main.cpp
//  A
//
//  Created by Franco Ariel Ramirez Villa on 08/04/17.
//  Copyright © 2017 Franco Ariel Ramirez Villa. All rights reserved.
//

#include <iostream>
#define ENDL '\n'
using namespace std;
int main(){
    cin.tie(NULL);
    ios_base::sync_with_stdio(NULL);
    short int c,i,t,j,cont,casos=1,tam;
    string cad;
    cin>>c;
    while (c--) {
        cont=0;
        cin>>cad>>t;
        tam=cad.size();
        for (i=0; i<=tam-t; i++) {
            if (cad[i]=='-') {
                cont++;
                for (j=i; j<i+t; j++) {
                    if (cad[j]=='-') {
                        cad[j]='+';
                    }else cad[j]='-';
                }
            }
        }
        for (i=0,t=1; i<tam; i++) {
            if (cad[i]=='-') {
                t=0;
                break;
            }
        }
        if (t) {
            cout<<"Case #"<<casos<<": "<<cont<<ENDL;
        }else   cout<<"Case #"<<casos<<": "<<"IMPOSSIBLE"<<ENDL;
        casos++;
    }
    return 0;
}
