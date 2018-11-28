//Vivek Nynaru
#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef unsigned long long int ull;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef set<int> si;
typedef set<ll> sll;
typedef vector<pii> vpii;
typedef vector<pll> vpll;
typedef set<pii> spii;
typedef set<pll> spll;
typedef map<int,int> mii;
typedef map<ll,ll> mll;
typedef map<string,ll> msl;

#define fast_io std::ios::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define dtype(x,a) __typeof(a) x(a)
#define rep(i,a,b) for(int i=a;i<=b;i++)
#define rev(i,a,b) for(int i=b;i>=a;i--)
#define iterate(v,it) for(dtype(it,v.begin());it!=v.end();it++)
#define riterate(v,it) for(dtype(it,v.rbegin());it!=v.rend();it++)
#define TC() int tc;cin >> tc;rep(test,1,tc)
#define ri(a) scanf("%d",&a)
#define rll(a) scanf("%lld",&a)
#define wi(a) printf("%d",a)
#define wll(a) printf("%lld",a)
#define wl printf("\n")
#define ws printf(" ")
#define endl "\n"
#define lbound(a,x) (lower_bound(a.begin(),a.end(),x)-a.begin())
#define ubound(a,x) (upper_bound(a.begin(),a.end(),x)-a.begin())

#define DEND "\n"
#define DMAP " : "
#define DSEP " | "
#define trace1(a) cerr << #a << DMAP << a << DEND;
#define trace2(a,b) cerr << #a << DMAP << a << DSEP << #b << DMAP << b << DEND;
#define trace3(a,b,c) cerr << #a << DMAP << a << DSEP << #b << DMAP << b << DSEP << #c << DMAP << c << DEND;
#define trace4(a,b,c,d) cerr << #a << DMAP << a << DSEP << #b << DMAP << b << DSEP << #c << DMAP << c << DSEP << #d << DMAP << d << DEND;
#define trace5(a,b,c,d,e) cerr << #a << DMAP << a << DSEP << #b << DMAP << b << DSEP << #c << DMAP << c << DSEP << #d << DMAP << d << DSEP << #e << DMAP << e << DEND;
#define trace6(a,b,c,d,e,f) cerr << #a << DMAP << a << DSEP << #b << DMAP << b << DSEP << #c << DMAP << c << DSEP << #d << DMAP << d << DSEP << #e << DMAP << e << DSEP << #f << DMAP << f << DEND;
#define prmap(a) iterate(a,it){cerr << it->F << " : " << it->S << "\n";}
#define pcout(n) cout << setprecision(n)

#define MOD 1000000007
#define inf 1000000000000000000
#define pi 3.141592653589793

ll exp(ll a, ll b, ll m=0)
{
	ll res=1;
	while(b)
	{
		if(b&1)
			res=(m)?(res*a)%m:res*a;
		a=(m)?(a*a)%m:a*a;
		b>>=1;
	}
	return res;
}
ll inv(ll a,ll b,ll m)
{
	return exp(exp(a,m-2,m),b,m);
}

//FILE *fin = freopen("in","r",stdin);
//FILE *fout = freopen("out","w",stdout);

bool occ[2000];
int lidx[2000];
int ridx[2000];
int main()
{
	int tc;
	cin >> tc;
	int n,k;
	for(int i=1;i<=tc;i++)
	{
		cin >> n >> k;
		for(int iter=0;iter<n+2;iter++)
			occ[iter]=false;
		occ[0]=occ[n+1]=true;
		int bidx=0;
		lidx[0]=-2;
		ridx[0]=-2;
		int y,z;
		for(int iter=0;iter<k;iter++)
		{
			bidx = 0;
			int loc=0,roc=n+1;
			for(int j=1;j<=n;j++)
			{
				if(occ[j])
					loc = j;
				lidx[j] = j-loc-1;
			}
			for(int j=n;j>0;j--)
			{
				if(occ[j])
					roc = j;
				ridx[j] = roc-j-1;
			}
			/*
			for(int j=1;j<=n;j++)
			{
				cout << lidx[j] << " " << ridx[j] << endl;
			}
			*/
			for(int j=1;j<=n;j++)
			{
				if(!occ[j])
				{
					//cout << min(lidx[j],ridx[j]) << " " << min(lidx[bidx],ridx[bidx]) << endl;
					if(min(lidx[j],ridx[j])>min(lidx[bidx],ridx[bidx]))
					{
						//cout << "Hello " << j << endl;
						bidx=j;
					}
					else if(min(lidx[j],ridx[j])==min(lidx[bidx],ridx[bidx]))
					{
						if(max(lidx[j],ridx[j])>max(lidx[bidx],ridx[bidx]))
							bidx=j;
					}
				}
			}
			//cout << "Hello" << lidx[bidx] << " " << ridx[bidx] << endl;
			occ[bidx] = true;
		}
		y = min(lidx[bidx],ridx[bidx]);
		z = max(lidx[bidx],ridx[bidx]);
		cout << "Case #" << i << ": " << z << " " << y << endl;
	}
	return 0;
}
