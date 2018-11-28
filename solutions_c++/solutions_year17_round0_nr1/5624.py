/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: ck
 *
 * Created on April 9, 2017, 3:10 AM
 */

#include <bits/stdc++.h>
#include <queue>
#include <string>
#include <map>

using namespace std;

/*
 * 
 */
struct procEle{
    string input;
    int c;
};

queue<procEle> toproc;
map<string,bool> done;
int k=0, out=-1;

string flip(string inp,int index){
    string input=inp;
    for(int i=0;i<k;i++){
        input[i+index]=(input[i+index]=='-'?'+':'-');
    }
    return input;
}

void proc(procEle input){
    bool r=1;
    if(done[input.input]){
        return;
    }else{
        done[input.input]=1;
    }
    for(int i=0;i<input.input.length();i++){
        if(input.input[i]=='-'){
            r=0;
        break;
        }
    }
    if(r){
        out=input.c;
        return;
    }
    for(int i=0;i<=input.input.length()-k;i++){
        procEle temp=input;
        temp.c++;
        temp.input=flip(temp.input,i);
        toproc.push(temp);
    }
}

string solve(string input){
    procEle tem;
    tem.input=input;
    tem.c=0;
    toproc.push(tem);
    while (toproc.size()>0&&out<0) {

        procEle temp=toproc.front();
        proc(temp);
        toproc.pop();
        
    }

    return (out<0?"IMPOSSIBLE":to_string(out));
}

int main(int argc, char** argv) {

    int n;
    cin>>n;
    for(int i=0;i<n;i++){
        string input;
        cin>>input;
        cin>>k;
        out=-1;
        done.clear();
        queue<procEle> emp;
        swap(toproc,emp);
        
        cout<<"Case #"<<i+1<<": "<<solve(input)<<"\n";
    }
    return 0;
}

