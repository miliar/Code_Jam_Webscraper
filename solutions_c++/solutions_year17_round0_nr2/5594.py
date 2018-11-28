/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: ck
 *
 * Created on April 8, 2017, 7:43 AM
 */

#include <bits/stdc++.h>

using namespace std;

/*
 * 
 */

string correct(string input, int i){
    if(i==0){
        input.erase(input.begin());
        return input;
    }
    input[i]='9';
    for(int j=i+1;j<input.length();j++)input[j]='9';
    if(input[i-1]=='0'||input[i-1]=='1'){
        input[i-1]='9';
        
        input=correct(input,i-1);
    }
    else input[i-1]--;
    return input;
}


string solve(string input){
    

    string numb= input;
    for(int i=numb.length()-1;i>0;i--){
        if(numb[i]<numb[i-1]||numb[i]=='0'){
            
            numb=correct(numb,i);
        }
    }
    
    return numb;
    
}

int main(int argc, char** argv) {
    int n;
    cin>>n;
    for(int i=0;i<n;i++){
        string input;
        cin>>input;
        cout<<"Case #"<<i+1<<": "<<solve(input)<<"\n";
    }
    return 0;
}

