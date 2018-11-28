/**
	site
	2 name (Code: Tidy_numbers)
	Source: GCJ.Qual 2017
*/

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

#include <iostream>
#include <iterator>
#include <algorithm>
#include <functional>
#include <string>
#include <map>
#include <vector>
#include <set>

typedef long long ll;
typedef long long unsigned llu;

#define	_min(a,b)	((a)<(b)?(a):(b))
#define _max(a,b)	((a)>(b)?(a):(b))

#define GI ({int t;scanf("%d",&t);t;})
#define GL ({ll t;scanf("%lld",&t);t;})
#define GD ({double t;scanf("%lf",&t);t;})

#define FOR(i,a,b) for(int i = a; i < b; i++)
#define ROF(i,a,b) for(int i=a;i>b;i--)
#define REP(i,n) FOR(i,0,n)

#define MOD 1000000007
#define INF (int)1e9
#define EPS 1e-9

#define IT(a,it) for (typeof((a).begin()) it = (a).begin(); it != (a).end(); ++it)
#define pb push_back
#define mp make_pair

#ifdef DEBUG
	std::string tabs;
	#define INDENT		tabs+="\t"
	#define _EXIT(val)	{ UNINDENT; return val; }
	#define UNINDENT	tabs.erase(tabs.length()-1)
	#define SHOW(x)		cout << tabs << x
	#define	ENDL		SHOW(endl)
	#include <time.h>
	#define STARTTIME	clock_t start = clock();
	#define GETTIME		printf("Time elapsed: %f\n", ((double)clock() - start) / CLOCKS_PER_SEC);
	#define _DEBUG(x)	x
#else
	#define INDENT
	#define _EXIT(val)	return val
	#define UNINDENT
	#define SHOW(x)
	#define ENDL
	#define STARTTIME
	#define GETTIME
	#define _DEBUG(x)
#endif

using namespace std;

void solve_saving()
{
	int t = GI;
	REP(i, t)
	{
		ll n = GL;
		char str[20] = {0};
		sprintf(str, "%lld", n);
		
		int len = strlen(str);
		for (int j = 0; j < len - 1; j++)
		{
			if (str[j] > str[j+1])
			{
				str[j]--;
				for (int k = j+1; k < len; k++)
					str[k] = '9';
				
				for (int k = j-1; k >= 0; k--)
				{
					if (str[k] > str[k+1])
					{
						str[k]--; str[k+1] = '9';
					}
					else
						break;
				}
				break;
			}
		}
		sscanf(str, "%lld", &n);
		cout << "Case #" << i+1 << ": " << n << endl;
	}
}

int main()
{
	STARTTIME;
	solve_saving();
	GETTIME;
	return 0;
}
