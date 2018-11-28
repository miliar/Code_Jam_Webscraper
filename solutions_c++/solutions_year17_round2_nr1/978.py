#include<bits/stdc++.h>
#define ll long long
#define pii pair<int,int>
#define piii pair<int,pair<int,int>>
#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define MOD 1000000007LL
#define ld long double
using namespace std;

inline ll getnum()
{
    char c = getchar();
    ll num,sign=1;
    for(; c<'0'||c>'9'; c=getchar())if(c=='-')sign=-1;
    for(num=0; c>='0'&&c<='9';)
    {
        c-='0';
        num = num*10+c;
        c=getchar();
    }
    return num*sign;
}

int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);

    int tests=getnum();

    for(int cases=1;cases<=tests;cases++)
    {
        double d=getnum();
        int n=getnum();
        double mx=0;

        for(int i=1;i<=n;i++)
        {
            double x=getnum(),y=getnum();
            mx=max(mx,(d-x)/y);
        }

        double ans=d/mx;

        printf("Case #%d: %0.8f\n",cases,ans);
    }
}
