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

int T;
int n,p;
int a[110];
int d[3];

int main()
{
	freopen("z.in", "rt", stdin);
	freopen("z.out", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);

	cin >>T;
	forn(I,T)
	{
		cin >>n>>p;
		forn(i,n)
			cin >>a[i];

		forn(i,3)
			d[i]=0;
		forn(i,n)
			d[a[i]%p]++;

		
		int ans=0;
		if(p==2)
		{
			ans+=d[0];
			ans+=(d[1]+1)/2;	
		}
		if(p==3)
		{
			ans+=d[0];
			int t=min(d[1],d[2]);
			ans+=t;
			d[1]-=t;
			d[2]-=t;
			ans+=(d[1]+2)/3;
			ans+=(d[2]+2)/3;
		}
		cout <<"Case #"<<I+1<<": "<<ans<<endl;
	}

	return 0;
}
