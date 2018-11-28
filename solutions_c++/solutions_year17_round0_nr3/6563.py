/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: UTENTE
 *
 * Created on 8 aprile 2017, 13.43
 */

#include <cstdlib>
#include<iostream>
#include<fstream>
#include<list>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    
    int n=0, bagni, persone,dist1,dist2,j,i,tmp;
    
    list<int> lista;
    list<int>::iterator p,q;
    
    ifstream in("input.txt");
    ofstream out("output.txt");
    
    in>>n;
    
    for(i=1;i<=n;i++){
        
        in>>bagni>>persone;
        lista.push_back(bagni);
        
        for(j=0;j<persone;j++){
            q=lista.begin();
            for(p=lista.begin();p!=lista.end();p++){
                if(*p>*q){
                    q=p;
                }
            }
            tmp=*q;
            if(tmp%2 == 0){
                dist1=*q/2;
                dist2=dist1-1;
            }
            else{
                dist1=dist2=*q/2;
            }
            lista.erase(q);
            
            if(dist2>0) lista.push_back(dist2);
            
            if(dist1>0) lista.push_back(dist1);
            
        }
        out<<"Case #"<<i<<": "<<dist1<<" "<<dist2<<endl;
        lista.clear();
        
    }

    return 0;
}

