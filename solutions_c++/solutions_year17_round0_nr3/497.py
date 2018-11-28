#include <bits/stdc++.h>
using namespace std;
#define md int(1600)
#define inf int(1e9+100)
#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b ;i++)
#define DOW(i,b,a) for(int i=(b),_a=(a); i>=_a ;i--)
#define mp make_pair
#define fi first
#define se second
#define pb push_back
#define pii pair<int,int>
#define ll long long

int xx[4]={0,0,1,-1};
int yy[4]={1,-1,0,0};
ll n,k;

ll calc(ll x, ll sx, ll y, ll sy)
{

    if (k<=sy)
    {
        return y;
    }
    k-=sy;
    if (k<=sx)
    {
        return x;
    }
    k-=sx;

    y--;
    x--;
    ll y2=y/2;
    ll x2=x/2;
    if (y%2==0)
    {
        calc(x2,sx,y2,sy*2+sx);
    }
    else
    {
        if (x==y)
        {
            calc(x2,sx+sy,y2+1,sx+sy);
        }
        else
        calc(x2,sx*2+sy,y2+1,sy);
    }
}


int main()
{
    freopen("C-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int tcase;
    scanf("%d",&tcase);
    FOR(o,1,tcase)
    {
        scanf("%lld%lld",&n,&k);
        n--;
        k--;
        ll x=n/2;
        if (k==0)
        {
            printf("Case #%d: %lld %lld\n",o,n-x,x);
        }
        else
        {
            ll res=calc(x,1,n-x,1)-1;
            printf("Case #%d: %lld %lld\n",o,res-res/2,res/2);
        }
    }
}

