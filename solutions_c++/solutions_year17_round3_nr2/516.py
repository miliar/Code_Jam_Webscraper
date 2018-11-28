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
int a,b,l,r;
int ta[1500],tb[1500];
int d[730][730][2];

int main()
{
	#ifdef LOCAL
	freopen("z.in","rt",stdin);
	freopen("z.out","wt",stdout);	
	#endif

	cin >>T;
	forn(I,T)
	{
		forn(i,1500)
		{
			ta[i]=0;
			tb[i]=0;
		}
		forn(i,730)
			forn(j,730)
				forn(k,2)
					d[i][j][k]=999999;
		d[0][0][0]=0;
		d[0][0][1]=0;

		cin >>a>>b;

		forn(i,a)
		{
			cin >>l>>r;
			for(int j=l; j<r; j++)
				ta[j]=1;
		}
		forn(i,b)
		{
			cin >>l>>r;
			for(int j=l; j<r; j++)
				tb[j]=1;
		}

		forn(t,24*60)
		{
			forn(i,24*60+1)
			{
				int j=t-i;
				if(i>=0 && i<=720 && j>=0 && j<=720)
				{
					if(ta[t]==0)
					{
						d[i+1][j][0]=min(d[i+1][j][0],d[i][j][0]);
						d[i+1][j][0]=min(d[i+1][j][0],d[i][j][1]+1);
					}
					if(tb[t]==0)
					{
						d[i][j+1][1]=min(d[i][j+1][1],d[i][j][1]);
						d[i][j+1][1]=min(d[i][j+1][1],d[i][j][0]+1);
					}
				}
			}
		}
		forn(i,2)
			d[720][720][i]+=d[720][720][i]%2;
		cout <<"Case #"<<I+1<<": "<<min(d[720][720][0],d[720][720][1])<<endl;
	}

	return 0;
}