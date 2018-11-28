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
int n,m;
char s[20];
int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,kase=1;
    scanf("%d",&t);
    while (t--)
    {
        scanf("%s",s);
        ll ans=0;
        int f=0;
        ll gg=1;
        for(int i=0;i<strlen(s);i++)
            gg*=10;
        int be=0;
        int ff=1;
        ll g=gg;
        for(int i=0;i<strlen(s);i++){
            g/=10,ans+=g*(s[i]-'0');
            if(i!=strlen(s)-1&&s[i]>s[i+1])ff=0;
        }
        if(ff==0)ans=0;
        for(int i=0;i<strlen(s);i++)
        {
            if(s[i]!='0')
            {
                int f=1;
                ll sum=0;
                ll g = gg;
                s[i]--;
                for(int j=0;j<i;j++){
                    g/=10;
                    sum+=g*(s[j]-'0');
                    if(s[j]>s[j+1])f=0;
                }
                s[i]++;
                if(f==0)break;
                if(i!=strlen(s)){
                g/=10;
                sum+=g*(s[i]-'0'-1);
                for(int j=i+1;j<strlen(s);j++)
                    g/=10,
                    sum+=9*g;
                ans=max(ans,sum);
                }
            }

        }
        cout<<"Case #"<<kase++<<": "<<ans<<endl;


    }
    return 0;
}
