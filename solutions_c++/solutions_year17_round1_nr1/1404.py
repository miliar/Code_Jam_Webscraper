//
//  main.cpp
//  gcj_1a_1
//
//  Created by yupeng gou on 4/14/17.
//  Copyright © 2017 yupeng gou. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <stack>
using namespace std;

bool replace(string &s){
    
    stack <int> index;
    char c = '?';
    for(int i = 0 ; i < s.length() ; i++){
        if(s[i] == '?'){
            index.push(i);
        }else{
            c = s[i];
            while(!index.empty()){
                int tmp = index.top();
                s[tmp] = s[i];
                index.pop();
            }
        }
    }
    
    if(index.empty())   return true;
    if(c =='?') return false;
    while(!index.empty()){
        int tmp = index.top();
        s[tmp] = c;
        index.pop();
    }
    return true;
    
}
int main(int argc, const char * argv[]) {
    freopen("/Users/yupenggou/Documents/gcj_1a_1/in.txt", "r", stdin);
    freopen("/Users/yupenggou/Documents/gcj_1a_1/out.txt", "w", stdout);
    int cases;
    cin >> cases;
    for(int it = 1 ;it <= cases; it++){
        vector<string> maps;
        stack <string> index;
        int r,c;
        string tmp,s;
        cin >> r >> c;
        for(int i = 0 ; i < r ; i++){
            cin >> tmp;
            if(!replace(tmp)){
                index.push(tmp);
            }else{
                s = tmp;
                while(!index.empty()){
                    maps.push_back(tmp);
                    index.pop();
                }
                maps.push_back(tmp);
            }
        }
        
        while(!index.empty()){
            index.pop();
            maps.push_back(s);
        }
        
        cout<<"Case #"<<it<<":"<<endl;
        for(int i = 0 ; i < r ; i++)
            cout<<maps[i]<<endl;
    }
    return 0;
}
