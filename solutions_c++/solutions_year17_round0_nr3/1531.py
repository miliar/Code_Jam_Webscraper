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
i64 n,k,cur;
map <i64,i64> mapp;

int main()
{
	#ifdef LOCAL
	freopen("z.in","rt",stdin);
	freopen("z.out","wt",stdout);	
	#endif

	cin >>T;
	forn(I,T)
	{
		cout <<"Case #"<<I+1<<": ";
		cin >>n>>k;
		
		cur=0;
		mapp.clear();
		
		mapp[-1*n]=1;
		while(1)
		{
			pair<i64,i64> d=(*mapp.begin());
            d.x*=-1;
            if(d.x==0)
            {
            	cout <<"0 0"<<endl;
            	break;
            }
            mapp.erase(mapp.begin());
			
            i64 d1=(d.x)/2;
			i64 d2=(d.x-1)/2;
			
			cur+=d.y;
			if(cur>=k)
			{
				cout <<d1<<' '<<d2<<endl;
				break;
			}

			mapp[-1*d1]+=d.y;
			mapp[-1*d2]+=d.y;
		}
	}

	return 0;
}