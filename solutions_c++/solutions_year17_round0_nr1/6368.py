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
int main()
{
	int z,t;in(t);
	FOR(z,0,t)
	{
		int i,j,n,k,ans=0;
		string s;inp(s);in(k);n=s.length();
		FOR(i,0,n-k+1)
		{
			if(s[i]=='+')continue;
			FOR(j,i,i+k)
			s[j]='+'+'-'-s[j];
			++ans;
		}
		printf("Case #%d: ",z+1);
		bool f=1;
		FOR(i,0,n)
		if(s[i]=='-'){f=0;break;}
		if(!f)pfs("IMPOSSIBLE");
		else pf(ans);
	}
	return 0;
}