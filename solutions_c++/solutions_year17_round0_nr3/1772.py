#include <cstdio>
#include <iostream>
#include <map>
#include <functional>
using namespace std;

map<long long,long long,greater<long long> > M[2];
long long n,k;

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int c,t,i,a,b;
    long long x,y,z;
    scanf("%d",&t);
    for(c=0;c<t;c++)
    {
        scanf("%I64d %I64d",&n,&k);
        M[0].clear();
        M[0][n]=1;
        a=0;
        b=1;
        while(k>0)
        {
            M[b].clear();
            for(map<long long,long long,greater<long long> >::iterator it=M[a].begin();it!=M[a].end();it++)
            {
                x=it->first;
                k=k-it->second;
                y=(x-0)/2;
                z=(x-1)/2;
                M[b][y]=M[b][y]+it->second;
                M[b][z]=M[b][z]+it->second;
                if(k<=0)
                {
                    break;
                }
            }
            a=a^1;
            b=b^1;
        }
        printf("Case #%d: %I64d %I64d\n",c+1,y,z);
    }
    return 0;
}
