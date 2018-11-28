#include <iostream>
#include <cstdio>
#include <queue>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#define maxn 1000100
#define maxm 10010
#define inf 0x3f3f3f3f

using namespace std;

int T;
long long n,m,k,lm,ct,at,st;
int p1,q1,size1,kase = 1;
vector<long long> deal[2],num[2],cd,cn;

inline long long max(long long a,long long b) {
    return a>b?a:b;
}

inline long long min(long long a,long long b) {
    return a<b?a:b;
}

long long log2(long long a) {
    long long ans=-1;
    while(a)
    {
        a/=2;
        ans++;
    }
    return ans;
}

long long pow2(long long a) {
    long long ans=1;
    while(a--)
    {
        ans*=2;
    }
    return ans;
}


int main() {
    scanf("%d",&T);
    while(T--) {
        int i;
        scanf("%lld%lld",&n,&k);
        lm = log2(k+1);
        num[lm%2].erase(num[lm%2].begin(),num[lm%2].end());
        deal[lm%2].erase(deal[lm%2].begin(),deal[lm%2].end());
        deal[lm%2].push_back(n);
        num[lm%2].push_back(1);
        ct = k+1-pow2(lm);
        at = 0;
        st = n;
        while(lm)
        {
            p1 = lm % 2;
            q1 = 1 - p1;
            deal[q1].erase(deal[q1].begin(),deal[q1].end());
            num[q1].erase(num[q1].begin(),num[q1].end());
            cd.erase(cd.begin(),cd.end());
            cn.erase(cn.begin(),cn.end());
            for(i=0;i < deal[p1].size();++i )
            {
                if(deal[p1][i]%2 == 0)
                {
                    cd.push_back(deal[p1][i]/2-1);
                    cd.push_back(deal[p1][i]/2);
                    cn.push_back(num[p1][i]);
                    cn.push_back(num[p1][i]);
                }
                else
                {
                    cd.push_back(deal[p1][i]/2);
                    cn.push_back(2*num[p1][i]);
                }
            }
            size1=1;
            deal[q1].push_back(cd[0]);
            num[q1].push_back(cn[0]);
            for(i=1;i < cd.size();++ i)
                if(cd[i]!=cd[i-1])
                {
                    deal[q1].push_back(cd[i]);
                    num[q1].push_back(cn[i]);
                    size1++;
                }
                else
                {
                    num[q1][size1-1]+=cn[i];
                }
            lm--;
        }
        if(ct > 0)
            for(i=deal[0].size()-1;i>=0;--i )
            {
                ct = ct-num[0][i];
                if(ct<=0)
                {
                    if(deal[0][i]%2==0)
                    {
                        at = deal[0][i]/2;
                        st = deal[0][i]/2-1;
                    }
                    else
                    {
                        at = st = deal[0][i]/2;
                    }
                    break;
                }
            }
        else
        {
            if(deal[1][0]%2==0)
            {
                at = deal[1][0]/2;
                st = deal[1][0]/2-1;
            }
            else
            {
                at = st = deal[1][0]/2;
            }
        }
        printf("Case #%d: %lld %lld\n",kase,at,st);
        kase++;
    }
    return 0;
}
