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
long long n;
int weishu;
int shuzu[30];
int result[30];
ifstream infile("file.in");
ofstream outfile("file.out");
void deal()
{
    weishu=0;
    while(n>0)
    {
        shuzu[weishu++]=n%10;
        n/=10;
    }
}
int mim(int a,int b)
{
    return a<=b?a:b;
}
void gouzao(int index)
{
    if(index>=weishu)
    {
        return;
    }
    else
    {
        if(index==0){result[0]=shuzu[0];gouzao(index+1);}
        else
        {
            result[index]=mim(shuzu[index],result[index-1]);
            if(result[index]<shuzu[index])
            {
                result[index]=shuzu[index]-1;
                for(int j=0;j<index;++j)result[j]=9;
            }
            gouzao(index+1);
        }
    }
}
int main()
{
    while(infile>>t)
    {
        for(int i=0;i<t;++i)
        {
            infile>>n;
            deal();
            gouzao(0);
            outfile<<"Case #"<<i+1<<": ";
            int st=0;
            if(result[weishu-1])st=weishu-1;
            else st=weishu-2;
            for(int j=st;j>-1;--j)outfile<<result[j];
            outfile<<endl;
        }
    }
}
