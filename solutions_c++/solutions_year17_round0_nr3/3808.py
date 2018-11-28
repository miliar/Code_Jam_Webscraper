#include<bits/stdc++.h>
#define ll long long
#define pii pair<ll,ll>
#define piii pair<int,pair<int,int> >
#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define SIZE 10000002
using namespace std;

inline ll getnum()
{
    char c = getchar();
    ll num,sign=1;
    for(;c<'0'||c>'9';c=getchar())if(c=='-')sign=-1;
    for(num=0;c>='0'&&c<='9';)
    {
        c-='0';
        num = num*10+c;
        c=getchar();
    }
    return num*sign;
}

map<pii,pii> Map;

pii doit(ll n,ll k)
{
    if(k==1)
    {
        if(n%2)return {n/2,n/2};
        else return {n/2-1,n/2};
    }
    if(k==2)return doit(n/2,1);

    pii x=Map[{n,k}];
    if(x!=mp(0ll,0ll))return x;

    if(k%2==0&&n%2==0)return Map[{n,k}]=min(doit(n/2-1,k/2-1),doit(n/2,k/2));
    if(k%2==0&&n%2==1)return Map[{n,k}]=min(doit(n/2,k/2),doit(n/2,k/2-1));
    if(k%2==1&&n%2==0)return Map[{n,k}]=min(doit(n/2,k/2),doit(n/2-1,k/2));
    if(k%2==1&&n%2==1)return Map[{n,k}]=doit(n/2,k/2);
}


int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);

    int tests=getnum();

    for(int cases=1;cases<=tests;cases++)
    {
        ll n=getnum(),k=getnum();

        Map.clear();
        pii ans=doit(n,k);

        printf("Case #%d: %lld %lld\n",cases,ans.ss,ans.ff);
    }
}
