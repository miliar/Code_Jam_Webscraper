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

lli ans;

void flip(char &ch)
{
	if(ch == '+')
		ch = '-';
	else
		ch = '+';
}

void change(str &s,int start,int k)
{
	fori(i,0,k-1)
	{
		flip(s[i+start]);
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
		ans = 0;
		cout<<"Case #"<<tc<<": ";
		str s;
		int k;
		cin>>s>>k;
		int n = s.size();
		fori(i,0,n-k)
		{
			if(s[i] == '-')
			{
				change(s,i,k);
				ans++;
			}
		}
		fori(i,0,n-1)
		{
			if(s[i] == '-')
			{
				ans = -1;
				break;
			}
		}
		if(ans == -1)
		{
			cout<<"IMPOSSIBLE\n";
		}
		else
		{
			cout<<ans<<endl;
		}
		cerr<<"Case #"<<tc<<": solved\n";
	}

	return 0;
}