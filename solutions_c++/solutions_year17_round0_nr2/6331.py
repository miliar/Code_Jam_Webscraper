/* O Beautiful program,
Please run for me.
I've tried you in BASIC,
FORTRAN and C.
Beautiful program,
You've errors galore.
And each time I run you,
You're swapped out of core.*/
#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <string>
#include <queue>
#include <numeric>
#include <cassert>
using namespace std;
#define pb push_back
#define epb emplace_back
#define mp make_pair
#define pr pair<int,int>
#define all(x) x.begin(),x.end()
#define in(x) scanf("%d",&x)
#define in2(x) scanf("%lld",&x)
#define pf2(x) printf("%lld\n",x)
#define FOR(x,y,z) for(x=y;x<z;++x)
#define rev(x,y,z) for(x=z-1;x>=y;--x)
#define pf(x) printf("%d\n",x)
#define pfs(s) printf("%s\n",s)
#define out(s) cout<<s
#define inp(s) cin>>s
#define st string
#define X first
#define Y second
typedef long long ll;typedef vector<int> vi;typedef vector<ll> vl;typedef vector<bool> vb;
ll todec(string& num, int b){ll dec=num[0]-(isupper(num[0])? 'A'-10: '0');for(int i=1;num[i];i++){if(num[i]>='A'&& num[i]<='Z')num[i]-='A'-10;else num[i]-='0';dec*= b;dec+= num[i];}return dec;}
ll bigMod(ll x, ll y, ll m){if(y == 0) return 1;ll p= bigMod(x, y/2, m)%m;p= (p*p)%m;return ((y&1)? (x*p)%m :p);}
ll ncr(int n, int k){ll res= 1;if(k>n-k)k= n-k;for(int i=0; i<k; i++){res *= n-i;res /= i+1;}return res;}
int phi(int n){int ret= n;for(int i= 2; i*i <= n; i++){if(n % i == 0){while(n%i == 0){n /= i;}ret -= ret/i;}}if(n > 1) ret -= ret/n;return ret;}
int egcd(int a, int b, int& x, int& y){if(a == 0){x= 0;y= 1;return b;}int x1, y1;int gcd= egcd(b%a, a, x1, y1);x= y1 - (b/a) * x1;y= x1;return gcd;}
st z[2]={"YES","NO"};
ll m,prev;bool f=0;
void generate(ll prefix, int start, int n)
{
    if (!n)
    {
        if(prefix<=m)
        {	
           	prev=prefix;return;
        }
    }
    else
    {
        for(int i=start;i<10;i++)
        generate(10*prefix+i, i, n-1);
    }
}

int main()
{
	int z,t;in(t);
	FOR(z,0,t)
	{
		in2(m);prev=-1;
		printf("Case #%d: ",z+1);
		if(m==1){pf(1);continue;}
		for(int i=1;i<=ceil(log10(m));++i)
		generate(0ll,1,i);
		pf2(prev);
	}
	return 0;
}