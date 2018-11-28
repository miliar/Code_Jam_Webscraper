#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <string.h>
#include <string>
#include <complex>
#include <bits/stdc++.h>
using namespace std;

#define rep(i,n) for(int i = 0; i < n; ++i)
#define Rep(i,n) for(int i = 1; i <= n; ++i)
#define lowbit(x) ((x)&(-x))
//#pragma comment(linker,"/STACK:1024000000,1024000000")
#define eps 1e-8
#define sqr(x) ((x)*(x))
#define pb(x) push_back(x)
#define mp(x,y) make_pair(x,y)
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<ld, ld> pdd;
typedef complex<double>cp;
template<class T>inline void rread(T&num){
    num=0;T f=1;char ch=getchar();
    while(ch<'0'||ch>'9'){if(ch=='-')f=-1;ch=getchar();}
    while(ch>='0'&&ch<='9')num=num*10+ch-'0',ch=getchar();
    num*=f;
}
const ll inf = 1e18;
const int maxn = 1e3+10, mod = 1e9 + 7;
const int mod1 = 1e8+7,mod2 = 41;
const double pi = acos(-1);
ll gcd (ll a, ll b)
{return ( a ? gcd(b%a, a) : b );}
void exgcd(ll a,ll b,ll &d,ll& x,ll& y)
{
    if(!b){d=a;x=1;y=0;}
    else {exgcd(b,a%b,d,y,x);y-=x*(a/b);}
}
cp power(cp a, int n)
{cp p = 1;while (n > 0) {if(n%2) {p = p * a;} n >>= 1; a *= a;} return p;}
unsigned long long power(unsigned long long a, unsigned long long n)
{unsigned long long p = 1;while (n > 0) {if(n%2) {p = p * a;} n >>= 1; a *= a;} return p;}
ll power(ll a, ll n)
{ll p = 1;while (n > 0) {if(n%2) {p = p * a;} n >>= 1; a *= a;} return p;}
ll power(ll a, ll n, ll mod)
{ll p = 1;while (n > 0) {if(n%2) {p = p * a; p %= mod;} n >>= 1; a *= a; a %= mod;} return p % mod;}
//head
ll n,m;
char s[20];
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("Cl.out","w",stdout);
    int t,kase=1;
    scanf("%d",&t);
    while (t--)
    {
        scanf("%lld%lld",&n,&m);
/*
        memset(flag,0,sizeof flag);
        flag[n+1]=1;
        int id;int m1,m2;
        for(int i=1;i<=m;i++){

        int be=0;
        int maa=0;

            for(int j=1;j<=n+1;j++)
        {
            if(flag[j]==1)
            {
                if(j-be>maa)
                    id=(j-be)/2+be,maa=j-be,m1 = j-id-1,m2=id-be-1;
                be=j;
            }

        }
        flag[id]=1;
        }*/


        ll l = 1,r = n;
        ll ma = (n)/2,mi = (n-1)/2;
        ll cur1=1,cur2=0;
        ma=n,mi=n-1;
        while(1)
        {
            if(cur1>=m)
            {
                mi = (ma-1)/2;ma = ma/2;
                break;
            }
            m-=cur1;
            if(cur2>=m)
            {
                ma = mi/2;mi=(mi-1)/2;
                break;
            }
            m-=cur2;
            ll mma,mmi;
            mma = ma/2;
            mmi = (mi-1)/2;
            if((ma-1)/2==ma/2)
            {
                cur1=cur1+cur2+cur1;
            }
            else
                cur2=cur1+cur2+cur2;
            ma = mma;
            mi= mmi;
        }
        cout<<"Case #"<<kase++<<": "<<ma<<" "<<mi<<endl;



    }
    return 0;
}
