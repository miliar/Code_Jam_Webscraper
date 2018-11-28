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

void inc(str &s)
{
	int n = s.size();
	int ind = -1;
	ford(i,n-1,0)
		if(s[i] != '9')
		{
			ind = i;
			break;
		}
	if(ind == -1)
	{
		fori(i,0,n-1)
		{
			s[i] = '1';
		}
		s += "1";
	}
	else
	{
		char ch = s[ind]+1;
		fori(i,ind,n-1)
		{
			s[i] = ch;
		}
	}
}

lli tonum(str s)
{
    int n = s.size();
    lli num = 0;
    fori(i,0,n-1)
        num = 10*num + s[i]-'0';
    return num;
}

vector<lli> arr;

void pre()
{
	str s = "1";
	while(tonum(s) < (lli)1e18)
	{
		arr.pb(tonum(s));
		inc(s);
	}
}

int main()
{
	#ifdef fileio
	freopen("output","w",stdout);
	freopen("input","r",stdin);
	#endif

	pre();
	int n = arr.size();
	int T;
	cin>>T;
	fori(tc,1,T)
	{
		cout<<"Case #"<<tc<<": ";
		lli num;
		cin>>num;
		int ind;
		fori(i,0,n-1)
		{
			if(arr[i] > num)
			{
				ind = i-1;
				break;
			}
			if(arr[i] == num)
			{
				ind = i;
				break;
			}
		}
		cout<<arr[ind]<<endl;
		cerr<<"Case #"<<tc<<": solved\n";
	}

	return 0;
}