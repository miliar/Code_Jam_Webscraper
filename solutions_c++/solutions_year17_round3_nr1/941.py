#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#define sqr(a) ((a)*(a))
#define RAND(a,b) ((a)+rand()%((b)-(a)+1))
#define rsz resize
#define forr(i,a,b) for(int i=(a);i<(b);i++)
#define forn(i,n) forr(i,0,n)
#define dforn(i,n) for(int i=n-1;i>=0;i--)
#define forall(it,v) for(auto it=v.begin();it!=v.end();it++)
#define pb push_back
#define mp make_pair
#define lb lower_bound
#define ub upper_bound
#define fst first
#define snd second
#define pi 3.1415926535897932384626433832795L
using namespace std;
using namespace __gnu_pbds;

typedef tree<int,null_type,less<int>,rb_tree_tag,tree_order_statistics_node_update> ordered_set;
typedef long long ll;
typedef pair<ll,ll> ii;

vector<ii> v;
int n;
double dp[1000][1000];
const double EPS=1e-9;

double solve(int pos,int restan,ll r)
{
	if(restan>n-pos-1) return -1e18;
	if(dp[pos][restan]>-1e17) return dp[pos][restan];
	double ret=0.0;
	if(restan>0) forr(i,pos+1,n)
	{
		double aux=solve(i,restan-1,v[pos].fst);
		if(aux+EPS>ret) ret=aux;
	}
	dp[pos][restan]=ret+pi*2*v[pos].fst*v[pos].snd;
	if(r==0) dp[pos][restan]+=pi*sqr(v[pos].fst);
	return dp[pos][restan];
}

int main()
{
	freopen("input.in","r",stdin);
	freopen("A-largeOutput.txt","w",stdout);
	ios::sync_with_stdio(false);
	ll t,k,r,h;
	cin >> t;
	forn(T,t)
	{
		cin >> n >> k;
		double ans=0.0;
		forn(i,n)forn(j,n) dp[i][j]=-1e18;
		v.rsz(n);
		forn(i,n)
		{
			cin >> r >> h;
			v[i]=mp(-r,h);
		}
		sort(v.begin(),v.end());
		forn(i,n) v[i].fst=-v[i].fst;
		forn(i,n)
		{
			double aux=solve(i,k-1,0);
			if(aux+EPS>=ans) ans=aux;
		}
		cout << "Case #" << T+1 << ": " << fixed << setprecision(8) << ans << "\n";
		v.clear();
	}
	return 0;
}	



