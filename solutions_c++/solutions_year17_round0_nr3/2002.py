#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <cstring>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <set>
#include <limits.h>
#include <assert.h>
using namespace std;

#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define null NULL
#define ll long long

#define fast cin.sync_with_stdio(0);cin.tie(0);
#define tr(c, itr) for(itr = (c).begin(); itr != (c).end(); itr++)
#define present(container, element) (container.find(element) != container.end()) //for set,map,etc
#define cpresent(container, element) (find(all(container),element) != container.end()) //for vectors
#define all(c) c.begin(),c.end() //eg sort(all(v));
//Initialization
#define clr(a) memset(a,0,sizeof(a))
#define ini(a) memset(a,-1,sizeof(a))

//Input Output
#define inp(n) scanf("%d",&n)
#define inp2(n,m) inp(n), inp(m)
#define inps(s) scanf("%s",s)
#define inpc(n) scanf("%c",&n)
#define inplf(n) scanf("%lf",&n)
#define inpll(n) scanf("%lld",&n)
#define inpll2(n,m) scanf("%lld%lld",&n,&m)

#define out(n) printf("%d\n",n)
#define out2(n,m) printf("%d %d\n",n,m)
#define outs(d) printf("%s\n",d)
#define sout(n) printf("%d ",n)
#define outll(n) printf("%lld\n",n)
#define soutll(n) printf("%lld ",n)
#define outll2(n,m) printf("%lld %lld\n",n,m)
#define nl printf("\n");

//loops
#define rep(i,n) for(long long i=0;i<n;i++)
#define REP(i,a,b) for(long long i=a;i<=b;i++)
#define PER(i,a,b) for(long long i=b;i>=a;i--)

//const
#define MOD 1000000007
#define MOD_INV 1000000006
#define MAX 1000000009
#define INF 1000000000000
#define PI 3.14159265358979323846264338327

//cases
#define aaa ll t;cin>>t;while(t--)

ll modpow(ll base, ll exp, ll modulus) {base %= modulus;ll result = 1;while (exp > 0){if (exp & 1) result = (result * base) % modulus;
base = (base * base) % modulus;exp >>= 1;}return result;}
bool tidy(ll num)
{
	ll last = 9;
	while(num)
	{
		ll p = num%10;
		if(p<last)
		{
			last = p;
		}
		else
		{
			if(p>last)
			{
				return 0;
			}
		}
		num/=10;
	}
	return 1;
}
bool hasLeading(ll n)
{
	while(n)
	{
		ll p = n%10;
		if(p == 0)
		{
			return 1;
		}
		else
		{
			return 0;
		}
	}
}
ll find(ll n)
{
	ll tot = 0,pp = n;
	while(pp)
	{
		tot++;
		pp/=10;
	}
	if(tidy(n))
	{
		return n;
	}
	n--;
	if(tidy(n))
	{
		return n;
	}
	if(hasLeading(n))
	{
		n--;
	}
	if(tidy(n))
	{
		return n;
	}
	ll p = n;
	ll tot1= 0 ;
	while(p)
	{
		tot1++;
		p/=10;
	}
	if(tot == tot1)
	{
		vector<ll> ans;
		vector<ll> dig;
		ll ppp = n;
		while(ppp)
		{
			dig.pb(ppp%10);
			ppp/=10;
		}
		reverse(all(dig));
		for(int i=1;i<tot;i++)
		{
			if(dig[i]>=dig[i-1])
			{
				
			}
			else
			{
				ll sw = 0;
				ll poss ;
				for(ll j=i-1;j>0;j--)
				{
					if(dig[j]>dig[j-1])
					{
						dig[j]--;
						poss = j;
						sw = 1;
						break;
					}
				}
				if(sw == 0)
				{
					dig[0]--;
					poss=0;
				}
				for(ll k=poss+1;k<tot;k++)
				{
					dig[k]=9;
				}
				ll anss = 0;
				for(ll k=0;k<tot;k++)
				{
					anss = anss*10+dig[k];
				}
				return anss;
			}
		}
		return 0;
	}
	else
	{
		ll ans = 0;
		while(tot1--)
		{
			ans = ans*10+9;
		}
		return ans;
	}
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	int test = 1;
	while(test<=t)
	{
		ll n,k;
		cin>>n>>k;
		ll p = k;
		vector<bool> path;
		while(p)
		{
			path.pb(p%2);
			p/=2;
		}
		ll lo = 1;
		ll hi = n;
		for(ll i=0;i<path.size()-1;i++)
		{
			ll mid = lo+hi;
			mid/=2;
			if(path[i])
			{
				hi = mid-1;
			}
			else
			{
				lo = mid+1;
			}
		}
		ll mid = lo+hi;
		mid/=2;
		ll ans1 = mid-lo;
		ll ans2 = hi-mid;
		cout<<"Case #"<<test<<": "<<max(ans1,ans2)<<" "<<min(ans1,ans2)<<endl;
		test++;
	}
	return 0;
}

