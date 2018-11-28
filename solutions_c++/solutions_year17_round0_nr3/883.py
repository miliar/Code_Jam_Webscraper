//
//  main.cpp
//  Problem3
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

int main()
{
    int T=0;
    ifstream fin;
    ofstream fout;
    fin.open("C-large.in");
    fout.open("C-large.out");
    fin>>T;
    for (int i = 0; i<T; i++)
    {
        long long N,K;
        fin>>N>>K;
        int flag = 1;
        long long current=1;
        long long N_interval=2,N_s=1,N_l=1;
        long long sm=(N-1)>>1,lg=N-1-sm;
        //cout<<sm<<' '<<lg<<endl;
        if (K==1)
        {
            flag=0;
            fout<<"Case #"<<i+1<<": "<<lg<<' '<<sm <<endl;
        }
        while (flag==1)
        {
            if (K>current+N_interval)
            {
                current = current+N_interval;
                N_interval*=2;
                if (sm==lg)
                {
                    N_s*=2; N_l*=2;
                    long long N_now = sm;
                    sm = (N_now-1)>>1;
                    lg = (N_now-1)-sm;
                }
                else if ((sm & 1) == 1)
                {
                    N_s = 2*N_s+N_l; //N_l = N_l;
                    long long N_now = lg;
                    sm = (N_now-1)>>1;
                    lg = (N_now-1)-sm;
                }
                else
                {
                    N_l = N_l*2+N_s;
                    long long N_now = sm;
                    sm = (N_now-1)>>1;
                    lg = (N_now-1)-sm;
                }
            }
            else
            {
                if (K<=current+N_l)
                {
                    long long MinLR =((lg-1)>>1);
                    long long MaxLR = lg-1- MinLR;
                    fout<<"Case #"<<i+1<<": "<<MaxLR<<' '<<MinLR <<endl;
                    flag = 0;
                    break;
                }
                else
                {
                    long long MinLR =((sm-1)>>1);
                    long long MaxLR = sm-1- MinLR;
                    fout<<"Case #"<<i+1<<": "<<MaxLR<<' '<<MinLR <<endl;
                    flag = 0;
                    break;
                }

            }
        }
    }
    return 0;
}
