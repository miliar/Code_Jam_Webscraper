#include <bits/stdc++.h>
#define ll long long
#define pb push_back
using namespace std;

ll dp[33][3][13];
vector<ll> v;

ll rec(int x, int y, int z)
{
//    printf("%d %d %d   %lld\n",x,y,z, v[x]);
    ll &rt= dp[x][y][z];
    if(rt!=-1) return rt;

    if(x==0)
    {
        if(y==0)
        {
            if(z>v[x]) return -2;
            return v[x];
        }
        return 9;
    }

    if(y==1)
    {
        rt=9;
        for(int i=0; i<x; i++)
        {
            rt*=10;
        }
        rt+= rec(x-1,1,9);
    }
    else
    {
        if(z> v[x]) return -2;
        rt= v[x];
        for(int i=0; i<x; i++)
        {
            rt*=10;
        }
        if(rec(x-1,0,v[x])==-2) rt=-2;
        else rt+= rec(x-1,0,v[x]);
        if(v[x]>z)
        {
            ll temp= v[x]-1;
            for(int i=0; i<x; i++)
            {
                temp*=10;
            }
            temp+= rec(x-1,1, v[x]-1);
//            printf("%lld %lld\n",temp, rec(x-1,1,v[x]-1));
            rt= max(rt,temp);
        }
    }
//    printf(" %d %d %d %lld\n",x,y,z,rt);
    return rt;
}

int main()
{
    freopen("B-large.in","r",  stdin);
    freopen("B-large-output.txt","w", stdout);
    int t,cs=1;
    ll n;
    scanf("%d",&t);

    while(t--)
    {
        memset(dp, -1, sizeof dp);
        scanf("%lld",&n);
        while(n)
        {
            v.pb(n%10);
            n/=10;
        }
        ll ans= rec(v.size()-1,0,0);

        printf("Case #%d: %lld\n",cs++, ans);
        v.clear();
    }
}
