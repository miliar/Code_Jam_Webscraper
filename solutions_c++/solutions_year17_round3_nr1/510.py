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
typedef pair < i64, i64 > PII;

i64 T;
i64 n,k;
PII a[1010];
ld ans;

ld calc(int ind)
{
	ld res=0.0;
	i64 tk=0;
	for(int i=0; tk<k-1; i++)
	{
		if(i==ind)
			continue;
		tk++;
		res+=2*PI*a[i].x*a[i].y;		
	}
	return res;
}

int main()
{
	#ifdef LOCAL
	freopen("z.in","rt",stdin);
	freopen("z.out","wt",stdout);	
	#endif

	cout <<fixed<<setprecision(10);

	cin >>T;
	forn(I,T)
	{
		cin >>n>>k;
		forn(i,n)
			cin >>a[i].x>>a[i].y;

		forn(i,n)
			for(int j=i+1; j<n; j++)
				if(a[i].x*a[i].y<a[j].x*a[j].y)
					swap(a[i],a[j]);

		ans=0.0;
		forn(i,n)
			ans=max(ans,PI*a[i].x*a[i].x+2*PI*a[i].x*a[i].y+calc(i));
		cout <<"Case #"<<I+1<<": "<<(double)ans<<endl;
	}



	return 0;
}