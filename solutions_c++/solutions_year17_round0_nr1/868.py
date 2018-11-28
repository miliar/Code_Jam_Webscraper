//
//  main.cpp
//  Problem1
//
//  Created by 何凡琛 on 4/7/17.
//  Copyright © 2017 Fanchen He. All rights reserved.
//

#include <iostream>
#include <fstream>
#include<string.h>
#include<algorithm>
#include <cstdio>
#include <stdio.h>
#define maxlen 1010
using namespace std;

int main() {
    int T=0;
    freopen("A-large.in.txt","r",stdin);
    //ifstream fin;
    //ofstream fout;
    //fin.open("P1.in");
    //fout.open("P2.out");
    freopen("A-large.out.txt","w",stdout);
    cin>>T;
    //cout<<fin.is_open();
    //cout<<T;
    for (int i = 0; i<T; i++)
    {
        char str[maxlen];
        int  s[maxlen];
        int K = 0;
        cin>>str>>K;
        int len = -1;
        for (int j = 0; j<strlen(str); j++)
        {
            if (str[j]=='+') {len+=1; s[len] = 0;}
            else if (str[j]=='-') {len+=1; s[len] = 1;}
        }
        int count = 0;
        int flag = 1;
        len++;
        for (int j = 0; j<len; j++)
        {
            if (s[j] ==1)
            {
                if (j+K-1<len)
                {
                    count++; // Be careful about boundary
                    for (int t=0; t<K; t++)
                    {
                        s[j+t] = 1-s[j+t];
                    }
                    
                }
                else {flag = 0; break;}
            }
            
        }
        if (flag==1) cout<<"Case #"<<i+1<<": "<<count<<endl;
        else cout<<"Case #"<<i+1<<": "<<"IMPOSSIBLE\n";
    }
    //fin.close();
    //fout.close();
    return 0;
}
