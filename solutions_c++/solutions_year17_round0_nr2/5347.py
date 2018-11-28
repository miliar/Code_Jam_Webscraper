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
ll dp[20][10]; // dp[i][j] stores number of tidy numbers with i digits and starting with j
ll cum[20][10]; // cum[i][j] stores number of tidy numbers with less than i digits + number of tidy numbers with i digits and first digit <=j

ll nthtidy(ll n)
{
	ll res = 0;
	int digits = 1,digit=1,prev=1;
	while(n>cum[digits][9])
		digits++;
	n -= cum[digits-1][9]; 
	for(int i=digits;i>0;i--)
	{
		ll cur1 = 0,cur2 = dp[i][digit];
		while(cur2<n)
		{
			cur1 += dp[i][digit];
			cur2 += dp[i][digit+1];
			digit+=1;
		}
		res = res*10 + digit;
		prev = digit;
		n-=cur1;
	}
	return res;
}

int main()
{
	for(int i=1;i<=9;i++)
	{
		dp[1][i] = 1;
		cum[1][i] = cum[1][i-1]+dp[1][i];
	}
	for(int i=2;i<20;i++)
	{
		cum[i][1] = cum[i-1][9];
		for(int j=1;j<=9;j++)
		{
			cum[i][j] += cum[i][j-1];
			for(int k=j;k<=9;k++)
			{
				dp[i][j] += dp[i-1][k];
			}
			cum[i][j] += dp[i][j];
		}
	}
	int tc;
	ll n;
	cin >> tc;
	for(int i=1;i<=tc;i++)
	{
		cin >> n;
		ll left=1,right=4686825,mid,val;
		while(left<right)
		{
			mid = (left+right+1)/2;
			val = nthtidy(mid);
			if(val<=n)
				left = mid;
			else
				right = mid-1;
		}
		cout << "Case #" << i << ": " << nthtidy(left) << endl;
	}
	return 0;
}
