#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <cstdio>
#include <iomanip>
#include <map>
#include <string.h>
#include <utility>
using namespace std;
int t;
int n;
int k;
int remain;
int shuzu[1000005]={0};
ifstream infile("file.in");
ofstream outfile("file.out");
void digui(int n,int ceng)
{
    if(ceng==0)
    {
        shuzu[n]++;
    }
    else
    {
        if(n%2)
        {
            digui((n-1)/2,ceng-1);
            digui((n-1)/2,ceng-1);
        }
        else
        {
            digui(n/2,ceng-1);
            digui(n/2-1,ceng-1);
        }
    }
}
void output(int m)
{
    if(m%2)
    {
        outfile<<(m-1)/2<<' '<<(m-1)/2<<endl;
    }
    else outfile<<m/2<<' '<<m/2-1<<endl;
}
int main()
{
    while(infile>>t)
    {
        for(int i=0;i<t;++i)
        {
            infile>>n>>k;
            memset(shuzu,0,sizeof(shuzu));
            outfile<<"Case #"<<i+1<<": ";
            int j;
            int cengshu;
            for(j=30;j>=0;--j)
            {
                int tmp=1;
                if((k>>j)&1)
                {
                    cengshu=j;
                    remain=k-(tmp<<j)+1;
                    break;
                }
            }
            digui(n,cengshu);
            for(int j=n;j>=1;--j)
            {
                if(shuzu[j]>=remain)
                {
                    output(j);
                    break;
                }
                else
                {
                    remain-=shuzu[j];
                }
            }
        }
    }
}
