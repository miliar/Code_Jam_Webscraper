/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: Juan Diego
 *
 * Created on 8 de abril de 2017, 06:42 AM
 */

#include <bits/stdc++.h>
#define SSTR( x ) static_cast< std::ostringstream & >( \
        ( std::ostringstream() << std::dec << x ) ).str()
using namespace std;

/*
 * 
 */


int main(int argc, char** argv) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);
    int numT;
    cin >> numT;
    for(int i = 0; i < numT; i++){
        string num;
        cin >> num;
        int aux;
        aux = atoi(num.c_str());
        while(true){
            bool valido = true;
            for(int j = 0; j < num.length() - 1; j++){
                if(num[j] > num[j+1]){
                    valido = false;                    
                }
            } 
            if(valido){
                break;
            }else{
                int aux = atoi(num.c_str());
                aux--;
                num = SSTR(aux);
            }
        } 
        cout <<"Case #" <<i+1<<": "<< num<<'\n';
    }
    return 0;
}

