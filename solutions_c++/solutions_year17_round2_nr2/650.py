#include <bits/stdc++.h>
#define ff first
#define ss second
#define pb push_back
#define MOD (1000000007LL)
#define LEFT(n) (2*(n))
#define RIGHT(n) (2*(n)+1)
 
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> ii;
typedef pair<int, ii> iii;
 
ll pwr(ll base, ll p, ll mod = MOD){
ll ans = 1;while(p){if(p&1)ans=(ans*base)%mod;base=(base*base)%mod;p/=2;}return ans;
}
 
ll gcd(ll a, ll b){
    if(b == 0)  return a;
    return gcd(b, a%b);
}

typedef vector<double> VD;
typedef vector<VD> VVD;
typedef vector<int> VI;

int t,n;
int r,o,y,g,b,v;
vector<pair<int,char> > a;
int main()
{
	scanf("%d",&t);
	int cnt = 1;
	while(t--)
	{
		scanf("%d",&n);
		scanf("%d%d%d%d%d%d",&r,&o,&y,&g,&b,&v);
		printf("Case #%d: ",cnt);
		cnt++;
		if(r > (n)/2 || y > (n)/2 || b > (n)/2)
		{
			printf("IMPOSSIBLE\n");
			continue;
		}
		a.clear();
		a.push_back(make_pair(r,'R'));
		a.push_back(make_pair(y,'Y'));
		a.push_back(make_pair(b,'B'));
		sort(a.begin(),a.end());
		int y = a[2].ff-a[0].ff;
		int z = a[0].ff+a[1].ff-a[2].ff;
		int x = a[2].ff-a[1].ff;
		string s = "";
		for(int i=0;i<z;i++)
			s += "210";
		for(int i=0;i<y;i++)
			s += "21";
		for(int i=0;i<x;i++)
			s += "20";

		for(int i=0;i<s.length();i++)
			printf("%c",a[s[i]-'0'].ss);
		printf("\n");

	}
	return 0;
}