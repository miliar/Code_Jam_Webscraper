#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>
#include <cmath>
#include <list>
#include <map>
#include <set>
using namespace std;

typedef long long int LL;
typedef long double LD;
typedef vector<int> VI;
typedef vector<LL> VLL;
typedef vector<LD> VLD;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

const int INF = 1000000001;
const LD EPS = 10e-9;

#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define VAR(v, n) __typeof(n) v = (n)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define FORE(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define MP make_pair
#define PB push_back
#define ST first
#define ND second
#define abs(a) ((a)<0 ? -(a) : (a))
#define max(a, b) ((a) > (b) ? (a) : (b))
#define min(a, b) ((a) < (b) ? (a) : (b))

int T, k;
string s;

void flip(int b)
{
	FOR(i, b, b+k-1)
	{
		if(s[i] == '+')
			s[i] = '-';
		else 
			s[i] = '+';
	}
}

bool check()
{
	FORE(it, s)
		if(*it == '-')
			return false;
			
	return true;
}

int main()
{
	cin >> T;
	FOR(t, 1, T)
	{
		cin >> s >> k;
		
		bool ok = false;
		int res = 0;
		
		REP(i, s.size()-k+1)
		{
			if(s[i] == '-')
			{			
				flip(i);
				res++;
			}
				
			if(check())
			{				
				ok = true;
				break;		
			}
		}
		
		cout << "Case #" << t << ": ";
		if(ok)
			cout << res;
		else
			cout << "IMPOSSIBLE";
		cout << endl;
		
	}
	return 0;
}

