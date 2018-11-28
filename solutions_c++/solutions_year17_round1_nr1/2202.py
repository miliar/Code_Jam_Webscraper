//
//  2008prob2.cpp
//  
//
//  Created by srikar on 01/04/17.
//
//

#include <stdio.h>
//
//  main.cpp
//  dfd
//
//  Created by srikar on 28/03/17.
//  Copyright © 2017 srikar. All rights reserved.
//

//Lawnmover 2003 prob b

#include <iostream>
#include <string>
#include <queue>
#include <unordered_set>
#include<limits.h>
#include <fstream>
using namespace std;
void fill( vector <string> &vec,int i,int j,int r,int c){
    int mi=j-1,ma=j+1,mar=i+1,mir=i-1;
    char w=vec[i][j];
    while(ma<c && vec[i][ma]=='?')
    {
        ma++;
    }
    while(mi>=0 && vec[i][mi]=='?')
    {
        mi--;
    }
    ma--;
    mi++;
    while(mar<r){
        int k=mi;
        for(k=mi;k<=ma;k++)
        {
            if(vec[mar][k]!='?'){
                break;
            }
        }
        if(k<=ma)
            break;
        mar++;
    }
    while(mir>=0){
        int k=mi;
        for(k=mi;k<=ma;k++)
        {
            if(vec[mir][k]!='?'){
                break;
            }
        }
        if(k<=ma)
            break;
        mir--;
    }
    mar--;
    mir++;
    for(int i1=mir;i1<=mar;i1++){
        for(int j1=mi;j1<=ma;j1++){
            vec[i1][j1]=w;
        }
    }
}
int main() {
    int t;
    cin >> t;
    int l=1;
    ofstream myfile;
    myfile.open ("1small.txt");
    vector <string> vec(50);
    vector <int> b(26);
    while(t--){
        int r,c;
        cin >> r >> c;
        for(int i=0;i<26;i++){
            b[i]=0;
            
        }
        for(int i=0;i<r;i++){
            
            cin >> vec[i];
        }
        for(int i=0;i<r;i++){
            for(int j=0;j<vec[i].length();j++){
                if(vec[i][j]!='?'){
                    if(b[vec[i][j]-'A']==1)
                        continue;
                    
                    fill(vec,i,j,r,c);
                    b[vec[i][j]-'A']=1;
                }
            }
        }
       
        
        myfile << "Case #";
        myfile << l;
        myfile << ":" <<endl;
        for(int i=0;i<r;i++){
            myfile << vec[i] <<endl;
        }
       
        l++;
        
    }
    return 0;
}
