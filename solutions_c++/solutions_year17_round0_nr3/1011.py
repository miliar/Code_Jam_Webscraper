#include<cstdio>
#include<iostream>
#include<vector>
#include<map>
#include<algorithm>
#include<cstring>
using namespace std;
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int T, cas=0;
    scanf("%d",&T);
    long long n,k;
    while(T--)
    {
        scanf("%lld%lld",&n,&k);
        map<long long, long long> nn;
        map<long long, long long>::iterator it;
        nn[-n] = 1LL;
        long long ans=0;
        while(k>0)
        {
            map<long long, long long> m;
            for(it=nn.begin();it!=nn.end();it++)
            {
                long long num = -((*it).first);
                long long tot = (*it).second;
                ans = num;
                k -= tot;
                m[-((num-1)/2)] += tot;
                m[-(num/2)] += tot;
                if(k<=0)
                break;
            }
            nn = m;
        }
        long long a1=(ans-1)/2, a2=(ans)/2;
        printf("Case #%d: %lld %lld\n", ++cas, a2, a1);
    }


}

