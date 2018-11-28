#include<bits/stdc++.h>
#define in freopen("input.txt","r",stdin)
#define out freopen("output.txt","w",stdout)

#define inp freopen(".in","r",stdin)
#define outp freopen(".out","w",stdout)

using namespace std;

#define pb push_back
#define pf push_front
#define p_f pop_front
#define p_b pop_back
#define LL long long int
#define LD long double
#define MP make_pair
#define sqr(x) (x*x)
#define nwl pr("\n")
#define fi first
#define dist(x,y,xx,yy) sqrt( (x-xx)*(x-xx)+(y-yy)*(y-yy) )
#define lenint int intsi(int x){ int cnt=0; while(x>0){cnt++;x/=10;} return (cnt); }
#define se second
#define all(v) v.begin(),v.end()
#define sc scanf
#define DEBUG(a) cout<<#a<<" -> "<<a<<endl;
#define pr printf
#define si size()
#define str strlen
#define time clock()/(double)CLOCKS_PER_SEC
#define gcd LL GCD(LL a,LL b){ if(b==0)return a;else return GCD(b,a%b); }
const int INF=(-1u)/2;
const long long int INF2=(-1ull)/2;
int a,b,c[100010],d[100010],i,j,k,n,m,timer=0,x,y;
int cnt=0,a2,a3=-1000000,ans=0,l,r,t;
pair<int,int>p[100010];
long long res = 0, fl;
double pi = 3.14159265359;
multiset<long long int>st;
multiset<long long int>::iterator it;
main()
{
    in;
    out;
    ios_base::sync_with_stdio(0);
	cin>>t;
	while(t-->0)
	{
		++ans;
		cin >> n >> k;
		res = 0;
		for(i = 0; i < n; ++i)
		{
			cin >> a >> b;
			p[i] = MP(a, b * -1);
		}
		for (i = 0; i < n; ++i)
		{
			st.clear();
			fl = 0;
			for (j = 0; j < n; ++j)
			{
				if (p[j].fi <= p[i].fi && j != i)
					st.insert(p[j].fi * 1ll * (-p[j].se));
			}
			if (st.size() < k - 1)
				continue;
			fl += (p[i].fi * 1ll * (-p[i].se)) * 2ll;
			for (j = 1; j < k; ++j)
			{
				it = st.end();
				--it;
				fl += (*it) * 2ll;
				st.erase(it);
			}
			fl += p[i].fi * 1ll * p[i].fi;
			res = max(res, fl);
		}
		cout << "Case #" << ans << ": ";
		cout << fixed << setprecision(8) << pi * (1.0 * res) << endl;
	}
    return 0;
}
