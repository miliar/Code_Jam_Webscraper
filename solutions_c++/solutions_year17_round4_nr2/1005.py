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
int n,c,m;
int pl,ind;

int a[2][1010];

int ans,prom;

int fmax(int ind, int cant)
{
	int res=-1;
	forn(i,n)
		if(a[ind][i]>0 && i!=cant && (res==-1 || min(a[ind][res],a[!ind][res])<min(a[ind][i],a[!ind][i])))
			res=i;

	if(res==-1 && a[ind][cant]>0)
		res=cant;		
	return res;
}

bool solve_step()
{
	int p0=-1,p1=-2;

	//first need pl1
	if(a[0][0]>0)
	{
		p0=0;
		p1=fmax(1,0);
	}
	//second need pl1
	else if(a[1][0]>0)
	{ 
		p1=0;
		p0=fmax(0,0);
	}
	else
	{
		p0=fmax(0,-1);
		p1=fmax(1,p0);
	}
	//cout <<p0<<' '<<p1<<endl;

	//no
	if(p0==-1 && p1==-1)
		return 0;
	//only sec
	if(p0==-1)
	{
		a[1][p1]--;
		ans++;
		return 1;
	}
	//only first
	if(p1==-1)
	{
		a[0][p0]--;
		ans++;
		return 1;
	}
	
	if(p0==p1 && p0==0)
	{
		ans++;
		a[0][p0]--;
		return 1;
	}
	if(p0==p1 && p0!=0)
	{
		ans++;
		prom++;
		a[0][p0]--;
		a[1][p1]--;
		return 1;
	}

	ans++;
	a[0][p0]--;
	a[1][p1]--;
	return 1;
}

int main()
{
	freopen("z.in", "rt", stdin);
	freopen("z.out", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);

	cin >>T;
	forn(I,T)
	{
		forn(i,1010)
			forn(j,2)
				a[j][i]=0;
		ans=0,prom=0;
		
		cin >>n>>c>>m;
		forn(i,m)
		{
			cin >>pl>>ind;
			pl--,ind--;
			a[ind][pl]++;
		}

		while(solve_step());

		cout <<"Case #"<<I+1<<": "<<ans<<' '<<prom<<endl;
	}


	return 0;
}
