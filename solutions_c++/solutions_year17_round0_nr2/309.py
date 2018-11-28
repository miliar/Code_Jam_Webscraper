#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef complex<double> cplx;

#define sqr(x) ((x)*(x))
#define pb push_back
#define X first
#define Y second
#define sit(a) set<a>::iterator
#define mit(a,b) map<a,b>::iterator

const ll mod=1000000007LL;
const int maxn=100005,maxm=605;
const double eps=1e-16;
const double pi=acos(-1.0);

typedef pair<ll,ll> pa;

ll cf[19]={1};

ll solve(ll n,int fir=1)
{
    int i,j,k,l;
    if(n<10) return n;
    if(n==cf[18]) return n-1;
    for(i=0;i<18;i++) if(cf[i+1]>n) break;
    ll s=(cf[i+1]-1)/9*(n/cf[i]);
    if(s<=n) return (n/cf[i])*cf[i]+solve(n%cf[i],n/cf[i]);
    else return (n/cf[i])*cf[i]-1;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T,I,i,j;
	for(i=1;i<19;i++) cf[i]=10*cf[i-1];
	scanf("%d",&T);
	for(I=1;I<=T;I++)
	{
	    ll n;
		scanf("%lld",&n);
		printf("Case #%d: %lld\n",I,solve(n));
		cerr<<"Case #"<<I<<" done\n";
	}
	return 0;
}
