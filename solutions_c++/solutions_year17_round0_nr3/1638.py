//always go for large or go home :P
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define sci(fd) scanf("%d",&fd)
#define scll(fd) scanf("%lld",&fd)
#define pb push_back
#define mp make_pair
#define MOD 1000000007
#define PI 3.1415926535897932
#define pii pair < int,int > 
#define pll pair < ll,ll >
#define fi first
#define se second
#define LOGN 20
const ll infi=1000000000000000009;
void doit(ll n,ll a,ll b,ll k)
{
    ll m;
    //printf("%lld\n",n);
    if(b>=k)
    {
        m=n+1;
        printf("%lld %lld\n",m/2,(m-1)/2);
        return;
    }
    if((a+b)>=k)
    {
        m=n;
        printf("%lld %lld\n",m/2,(m-1)/2);
        return;
    }
    ll aa,bb;
    if(n%2==1)
    {
        aa=2*a+b;
        bb=b;
    }
    else
    {
        aa=a;
        bb=2*b+a;
    }
    doit((n-1)/2,aa,bb,k-a-b);
}
int main()
{
    ll t,y=0;
    scll(t);
    while(t--)
    {
        ll n,k;
        y++;
        scll(n);
        scll(k);
        printf("Case #%lld: ",y);
        doit(n,1,0,k);
    }
    return 0;
}