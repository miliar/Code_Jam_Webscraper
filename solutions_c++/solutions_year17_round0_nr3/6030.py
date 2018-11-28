#include <bits/stdc++.h>

using namespace std;

//data_types 
#define lli 		long long int
#define vi			vector<int>
#define str  		string
#define ii 			pair<int,int>
#define crd			pair<int,int>
#define vii 		vector<ii>
#define vb			vector<bool>
#define mp			make_pair
#define xx 			first
#define yy			second
#define all(a)		a.begin(),a.end()
#define ins			insert
#define pb			push_back
#define sq(x)		((x)*(x))
//input/output and loops
#define gi(n)		scanf("%d",&n)
#define puti(n) 	printf("%d\n",n)
#define fori(i,m,n) for(int i=m;i<=n;i++)
#define ford(i,m,n)	for(int i=m;i>=n;i--)

//max,mod and inf
#define N 			((int)1e5)
#define mod			((lli)1e9+7)
#define	inf			INT_MAX
#define t 			true;
#define f 			false;

//functions
template <typename T>
T prod(const T &a,const T &b)
{
	return ((a%mod)*(b%mod))%mod;
}
template <typename T>
T pow(const T &a,const T &b)
{
	if(!b) return 1;
	T p = pow(a,b/2);
	p*=p;
	return (b%2)?(p*a):p;
}
template <typename T>
T modpow(const T &a,const T &b)
{
	if(!b) return 1;
	T p = modpow(a,b/2);
	p = prod(p,p);
	return (b%2)?(prod(p,a)):p;
}
template <typename T>
T gcd(const T &a,const T &b)
{
	if(!b)	return a;
	return gcd(b,a%b);
}
template <typename T>
T lcm(const T &a,const T &b)
{
	return (a*b)/gcd(a,b);
}

#define fileio

lli solve(lli n,lli k)
{
	if(k == n)
		return 0;
	if(k <= 1)
	{
		return n;
	}
	if(n%2)
	{
		return solve((n-1)/2,k/2);
	}
	else
	{
		return max(solve(n/2,(k+1)/2),solve((n/2)-1,k/2));
	}
}

int main()
{
	#ifdef fileio
	freopen("output","w",stdout);
	freopen("input","r",stdin);
	#endif

	int T;
	cin>>T;
	fori(tc,1,T)
	{
		cout<<"Case #"<<tc<<": ";
		lli n,k;
		cin>>n>>k;
		lli ans = solve(n,k);
		lli ls,rs;
		if(ans%2)
			ls = rs = (ans-1)/2;
		else
		{
			rs = ans/2;
			ls = rs-1;
		}
		if(ls < 0) ls = 0;
		if(rs < 0) rs = 0;
		cout<<rs<<" "<<ls<<endl;
		cerr<<"Case #"<<tc<<": solved\n";
	}

	return 0;
}