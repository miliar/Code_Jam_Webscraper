#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define clr(x) memset((x), 0, sizeof(x))
#define pb push_back
#define mp make_pair
#define sz size()
#define x first
#define y second
#define forn(i, n) for(int i=0; i<(n); i++)
#define ford(i, n) for(int i=(n)-1; i>=0; i--)

typedef long double ld;

// Constants
const ld PI = 3.1415926535897932384626433832795;
const ld EPS = 1e-11;

// Types
typedef signed   long long i64;
typedef unsigned long long u64;
typedef pair < int, int > PII;

int T,n,k;
double a[55],p;

int main()
{
	#ifdef LOCAL
	freopen("z.in","rt",stdin);
	freopen("z.out","wt",stdout);	
	#endif

	//cout <<fixed<<setprecision(10);

	cin >>T;
	forn(I,T)
	{
		cin >>n>>k>>p;
		forn(i,n)
			cin >>a[i];

		while(p>0.5/50000)
		{
			sort(a,a+n);
			a[0]+=1.0/50000;
			p-=1.0/50000;
		}

		double ans=1.0;
		forn(i,n)
		{
			ans*=a[i];
		//	cout <<(double)(a[i])<<' ';
		}
		//cout <<endl;
		cout <<"Case #"<<I+1<<": "<<ans<<endl;
		//printf("%.e\n",(double)ans);
	}

	return 0;
}