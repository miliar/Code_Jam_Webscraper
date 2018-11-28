//
//  main.cpp
//  B
//
//  Created by Franco Ariel Ramirez Villa on 08/04/17.
//  Copyright © 2017 Franco Ariel Ramirez Villa. All rights reserved.
//

#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#define ENDL '\n'
using namespace std;
int main(){
    cin.tie(NULL);
    ios_base::sync_with_stdio(NULL);
    unsigned long long c,num,i;
    short int j,dir;
    char aux[25];
    bool x=false;
    string a,b;
    cin>>c;
    i=1;
    while (c--) {
        cin>>num;
        do {
            sprintf(aux,"%llu",num);
            for (dir=0,x=false,j=0; j<strlen(aux)-1; j++) {
                if (aux[j]>aux[j+1]) {
                    dir=j;
                    x=true;
                    break;
                }
            }
            if (x) {
                aux[j]--;
                for (j++; j<strlen(aux); j++) {
                    aux[j]='9';
                }
                num=atoll(aux);
            }
            sprintf(aux,"%llu",num);
            a=aux;
            b=a;
            sort(b.begin(),b.end());
            if (a==b) {
                cout<<"Case #"<<i<<": "<<a<<ENDL;
                i++;
                break;
            }
        }while (num--);
    }
    return 0;
}
