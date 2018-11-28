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
#define pi			3.1415926535897932384626433

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

//#define fileio

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
		int n,k;
		cin>>n>>k;
		vii pa(n);
		fori(i,0,n-1)
			cin>>pa[i].yy>>pa[i].xx;
		sort(all(pa));
		double ans = 0;
		vii se(k);
		do
		{
			double temp = 0;
			int maxR = 0,ind;
			fori(i,0,k-1)
			{
				if(maxR < pa[i].yy)
				{
					maxR = pa[i].yy;
					ind = i;
				}
			}
			fori(i,0,k-1)
			{
				if(ind == i)
				{
					temp += pi*(double)pa[i].yy*(double)pa[i].yy;
				}
				temp += 2*pi*(double)pa[i].yy*(double)pa[i].xx;
			}
			if(temp > ans)
			{
				fori(i,0,k-1)
					se[i] = pa[i];
				ans = temp;
			}

		}while(next_permutation(all(pa)));		
		//fori(i,0,k-1)
		//	cout<<se[i].xx<<" "<<se[i].yy<<endl;
		printf("%.8lf\n",ans);
		cerr<<"Case #"<<tc<<": solved\n";
	}

	return 0;
}