#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<map>
#include<iterator>
using namespace std;
main()
{
    map<long long,long long> mp;
    map<long long,long long>::iterator p;
    FILE* FileRead = fopen("C-small-2-attempt1.in", "r");
    FILE* FileWrite = fopen("out.txt", "w");

    int n;
    fscanf(FileRead, "%d", &n);
    long long N,K;
    for(int i=1;i<=n;i++)
    {
        fscanf(FileRead,"%lld%lld",&N,&K);
        fprintf(FileWrite, "Case #%d: ", i);
        if(N==K)fprintf(FileWrite, "0 0\n");
        else
        {
            long long ansMax;
            long long ansMin;
            if(N%2==0)
            {
                ansMax = N/2;
                ansMin = (N-1)/2;
                mp.insert({ansMax,1});
                mp.insert({ansMin,1});
            }
                else
            {
                ansMax = (N-1)/2;
                ansMin = (N-1)/2;
                mp.insert({ansMax,2});
            }
            for(int j=1;j<K;j++)
            {
                p=--mp.end();
                N=p->first;
                if(p->second==1)mp.erase(p);
                else p->second-=1;
                if(N%2==0)
                {
                    ansMax = N/2;
                    ansMin = (N-1)/2;
                    if(ansMax!=0)
                    {
                        p=mp.find(ansMax);
                        if(p->first!=ansMax)mp.insert({ansMax,1});
                        else p->second+=1;
                    }
                    if(ansMin!=0)
                    {
                        p=mp.find(ansMin);
                        if(p->first!=ansMin)mp.insert({ansMin,1});
                        else p->second+=1;
                    }
                }
                else
                {
                    ansMax = (N-1)/2;
                    ansMin = (N-1)/2;
                    if(ansMax!=0)
                    {
                        p=mp.find(ansMax);
                        if(p->first!=ansMax)mp.insert({ansMax,2});
                        else p->second+=2;
                    }
                }
            }
            fprintf(FileWrite, "%lld %lld\n", ansMax, ansMin);
        }
        mp.clear();
    }
}
