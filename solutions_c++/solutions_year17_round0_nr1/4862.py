/* QA 2017  youri */
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
	char s[1024];
	
	int k;
	scanf("%s %d", s, &k);
	int n = strlen(s);

	int res = 0;
	int i;
	for (i = 0; i < n - k + 1; i++)
	{
		if(s[i] == '+')
			continue;
	
		res++;
		for (int j = i; j < i + k; j++)
		{
			if(s[j] == '-')
				s[j] = '+';
			else
				s[j] = '-';
		}
	}
	
//	printf("%s %d\n", s, n);

	for (i = n - k + 1; i < n; i++)
	{
		if (s[i] == '-')
		{
			res = -1;
			break;
		}
	} 

	//printf("%s %d\n", s, n);

	if (res == -1)
		printf("Case #%d: IMPOSSIBLE\n", _case);
	else
		printf("Case #%d: %d\n", _case, res);
}

