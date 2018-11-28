    #include <bits/stdc++.h>
using namespace std;

typedef pair<long long,long long> ii;
typedef pair<ii,long long> pii;
typedef vector<long long> vi;
typedef vector<ii> vii;
typedef vector<pii> vpii;
typedef long long ll;
typedef unsigned long long ull;

    #define mi 1000000007
    #define rep(i,a,b) for(i=a;i<b;i++)
    #define repv(i,a,b) for(i=a;i>b;i--)
    #define inf INT_MAX
    #define pb push_back
    #define mp make_pair
    #define fi first
    #define se second
    #define let(x,a) __typeof(a) x(a)
    #define all(a) (a).begin(),(a).end() 
    #define endl '\n'
    #define present(c,x) ((c).find(x) != (c).end()) 
    #define tr(v,it) for(let(it,v.begin()); it != v.end(); it++)
    #define rtr(v,it) for(let(it,v.rbegin()); it != v.rend(); it++)
    #define SET(a,b) memset(a,b,sizeof(a))
    #define si(n) scanf("%d",&n)
    #define dout(n) printf("%d\n",n)
    #define sll(n) scanf("%lld",&n)
    #define lldout(n) printf("%lld\n",n)

    #define trace1(x)                cerr << #x << ": " << x << endl;
    #define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
    #define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
    #define trace4(a, b, c, d)       cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
    #define trace5(a, b, c, d, e)    cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << endl;
    #define trace6(a, b, c, d, e, f) cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;

long long mult(long long x,long long y)
{
	ll ans,x1=(ll)x,y1=(ll)y;
	ans=(x1*y1)%mi;
	return (long long)ans;
}
long long gcd(long long a,long long b) { return b==0 ? a : gcd (b,a%b);}
long long lcm(long long a,long long b) { return a*(b/gcd(a,b));}

long long pow1(long long a,long long b)
{
	long long ans=1;
	while(b>0)
	{
		if(b&1) ans=mult(ans,a);  
		a=mult(a,a); b>>=1;
	} 
	return ans;
}
long long mina(long long arr[],long long n)
{
	long long x=arr[0],i,pos=0;
	rep(i,1,n){ if(arr[i]<x) { x=arr[i]; pos=i; } }
	return x;
}
long long maxa(long long arr[],long long n)
{
	long long x=arr[0],i,pos=0;
	rep(i,1,n){ if(arr[i]>x) { x=arr[i]; pos=i; } }
	return x;
}

int main()
{
	long long t;
	cin >> t;
	for(long long i=1; i<=t ; i++)
	{
		long long count = 0;
		long long minus = 0;
		string s;
		s.clear();
		cin >> s;
		long long k;
		cin >> k;
		long long n = s.size();
		for(long long j=0 ; j<=n-k ; j++)
		{

			if(s[j] == '-')
			{
				count++;
				for(long long l = 0 ; l<k ; l++)
				{
					if(s[j+l] == '+') s[j+l] = '-';
					else s[j+l] = '+';
				}
			}
		}

		for(long long j=0 ; j<n ;j++)
		{
			if(s[j] == '-')
			{
				minus = 1;
			}
		}
		cout<<"Case #"<<i<<": ";
		if(minus == 0)
		{
			cout<<count<<endl;
		}
		else 
		{
			cout<<"IMPOSSIBLE"<<endl;
		}
	}
	return 0;
}
