/* QB 2017  youri */
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

typedef long long LL;

#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define ABS(val) ((val) < 0 ? -(val) : (val))

#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define VAR(v, n) __typeof(n) v = (n)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define FOREACH(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define PB push_back
#define ST first
#define ND second

void solve(int c);
int main() {

	int cases;
	scanf("%d", &cases);
	REP(i, cases)
	{
		solve(i + 1);
	}

	return 0;
}


void solve(int _case)
{
	char s[32] = {0};
	char * res = s;
	
	scanf("%s", s);
	int n = strlen(s);

	for (int i = 1; i < n; i++)
	{
		if(s[i] < s[i - 1])
		{
			int t = i - 1;
		
			while (t > 0 && (s[t] - 1 < s[t-1]))
			{
				t--;
			} 
		
			// modifications

			s[t]--;
	
			for (int q = t + 1; q < n; q++)
			{
				s[q] = '9';
			}

			if(s[t] == '0')
				res++;

			break;
		}
	}

	printf("Case #%d: %s\n", _case, res);
}

