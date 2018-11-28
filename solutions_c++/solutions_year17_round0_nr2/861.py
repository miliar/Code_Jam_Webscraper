//
//  main.cpp
//  Problem2
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
#define maxlen 30
using namespace std;

int main() {
    int T=0;
    ifstream fin;
    ofstream fout;
    fin.open("B-large.in");
    fout.open("B-large.out");
    fin>>T;
    for (int i = 0; i<T; i++)
    {
        char str[maxlen];
        int  s[maxlen];
        fin>>str;
        for (int j = 0; j<strlen(str); j++)
            s[j]=str[j]-'0';
        int len=strlen(str);
        int current=strlen(str)-1;
        while (current>0)
        {
            if (s[current]>=s[current-1]) current--;
            else
            {
                s[current-1]--;
                for (int j = current; j<len; j++)
                    s[j] = 9;
            }
        }
        int start=0;
        while (start<len-1 && s[start]==0) start++;
        fout<<"Case #"<<i+1<<": ";
        for (int j = start; j<len; j++)
            fout<<s[j];
        fout<<endl;
    }
    //cout<<fin.is_open();
    //cout<<T;

    return 0;
}
