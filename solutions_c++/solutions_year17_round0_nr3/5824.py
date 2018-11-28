/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: ck
 *
 * Created on April 8, 2017, 1:28 PM
 */

#include <bits/stdc++.h>

using namespace std;

/*
 * 
 */

void solve(long n,long k){
    string out="";
    long ls=0,rs=0;
    priority_queue<long> q;
    
    q.push(n);
    
    for(long i=0;i<k;i++){
        long val=q.top();
        ls=val/2;
        rs=val-ls;
        if(ls==rs){
            ls--;
           
        }else {

            rs--;
        }
        if(ls>0)q.push(ls);
        if(rs>0)q.push(rs);
        q.pop();
    }
    cout<<max(ls,rs)<<" "<<min(ls,rs)<<"\n";
    
}

int main(int argc, char** argv) {
    long n;
    cin>>n;
    for(int i=0;i<n;i++){
        long inn,ink;
        cin>>inn>>ink;
        cout<<"Case #"<<i+1<<": ";//<<
        solve(inn,ink);//<<"\n";
    }
    
    return 0;
}

