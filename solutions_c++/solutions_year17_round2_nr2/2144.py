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

bool min(int a,int b,int c)
{
	return min(min(a,b),c);
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
		int n,r,o,y,g,b,v;
		cin>>n>>r>>o>>y>>g>>b>>v;
		if(r == y && y == b)
		{
			fori(i,0,r-1)
				cout<<"RYB";
			cout<<endl;
			continue;
		}
		vi a(3);
		a[0] = r,a[1] = y,a[2] = b;
		sort(all(a));
		if(a[0] + a[1] < a[2])
		{
			cout<<"IMPOSSIBLE\n";
			continue;
		}
		str ans;
		if(a[0] + a[1] >= a[2])
		{
			int m = a[0] + a[1] - a[2];
			fori(i,1,m)
			{
				ans += "RYB";
			}
			if(a[2] == r)
			{
				fori(i,1,b-m)
				{
					ans += "RB";
				}
				fori(i,1,y-m)
				{
					ans += "RY";
				}
			}
			else if(a[2] == y)
			{
				str add;
				if(ans.size() == 0)
					add = "BY";
				else
					add = "YB";
				fori(i,1,b-m)
				{
					ans += add;
				}
				fori(i,1,r-m)
				{
					ans += "RY";
				}
			}
			else if(a[2] == b)
			{
				fori(i,1,r-m)
				{
					ans += "RB";
				}
				fori(i,1,y-m)
				{
					ans += "YB";
				}
			}
		}
		if(ans.size() == n)
			cout<<ans<<endl;
		else
			cout<<"IMPOSSIBLE"<<endl;
		cerr<<"Case #"<<tc<<": solved\n";
	}

	return 0;
}