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
string s;

int main()
{
	#ifdef LOCAL
	freopen("z.in","rt",stdin);
	freopen("z.out","wt",stdout);	
	#endif

	cin >>T;
	forn(I,T)
	{
		cin >>s;
		
		bool ok=0;
		while(!ok)
		{
			ok=1;
			forn(i,s.size()-1)
				if(s[i]>s[i+1])
				{
					ok=0;
					s[i]--;
					for(int j=i+1; j<s.size(); j++)
						s[j]='9';
					break;
				}
		}
		cout <<"Case #"<<I+1<<": ";
		
		bool start=0;
		forn(i,s.size())
		{
			if(s[i]!='0')
				start=1;
			if(start)
				cout <<s[i];
		}
		cout <<endl;

	}

	return 0;
}