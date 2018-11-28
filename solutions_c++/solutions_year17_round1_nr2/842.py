#include <bits/stdc++.h>

using namespace std;
const double pi=acos(-1.0);
const double eps=1e-9;
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define re return
#define vi vector <int> 
#define pii pair <int,int>
#define pll pair <long long , long long>
typedef long long ll;

const int N = 1005;

ll t,ans,n,p,r[N],a,d[N];

vector <pll> v[N];

ll getMin(ll le, ll ri, ll a, ll r)
{
	if(le==ri) return le;
	if(ri == le + 1)
	{
		if(10*a >= 9 * r * ri) return ri;
		return le;
	}
	ll m = (le + ri)/2;
	if(10*a >= 9 * r * m) return getMin(m,ri,a,r); else return getMin(le,m,a,r);
}

ll getMax(ll le, ll ri, ll a, ll r)
{
	if(le==ri) return le;
	if(ri == le + 1)
	{
		if(11*r*le>=10*a) return le;
		return ri;
	}
	ll m = (le+ri)/2;
	if(10*a <= 11*r*m) return getMax(le,m,a,r);else return getMax(m,ri,a,r);
}

int main()
{
	ios:: sync_with_stdio(false);
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	cin >> t;
	for(int test = 1; test <= t; test++)
	{
		cin >> n >> p;
		for(int i = 0;i<n;i++)
			cin >> r[i];
		for(int i = 0;i<n;i++)
			v[i].clear();
		ans = 0;
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<p;j++)
			{
				cin >> a;
				ll f;
				if(10*a % (11*r[i]) == 0)f = 10*a/(11*r[i]); else f = floor(((double)10*a)/(11*r[i]))+1;
				ll s;
				if((10*a)%(9*r[i]) == 0)s = 10*a/(9*r[i]); else s = floor(((double)10*a)/(9*r[i]));
				//ll s = floor(((double)10*a)/(9*r[i]));
				v[i].pb(mp(f,s));
			}
			sort(v[i].begin(),v[i].end());
		}
		//for(int i=0;i<n;i++, cout << "\n")
		//	for(int j=0;j<p;j++)
		//		cout << v[i][j].fi << " " << v[i][j].se << "   ";
		for(int i=0;i<n;i++)
			d[i] = 0;
		for(int i=0;i<n;i++)
			while(d[i] < p && v[i][d[i]].fi == 0)
				d[i]++;
		while(true)
		{
			bool canDo = true;
			for(int i = 0;i<n;i++)
				if(d[i] == p) canDo = false;
			if(!canDo)break;
			int mini = 1000000000;
			int id = 0;
			for(int i=0;i<n;i++)
			{
				if(v[i][d[i]].se < mini)
				{
					mini = v[i][d[i]].se;
					id = i;
				}
			}
			for(int i = 0; i < n;i++)
			{
				if(v[i][d[i]].fi > mini)
				{
					d[id]++;
					canDo = false;
					break;
				}
			}
			if(!canDo)continue;
			ans++;
			for(int i=0;i<n;i++)
				d[i]++;
		}
		cout << "Case #" << test << ": " << ans << "\n";
	}
	return 0;
}
