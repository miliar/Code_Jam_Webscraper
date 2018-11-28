/* QC 2017  youri */
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
	int n, k;
	scanf("%d %d", &n, &k);

	priority_queue<int> q;

	q.push(n);

	int el1, el2;
	do 
	{
		int el = q.top() - 1;
		q.pop();

		el1 = el / 2;
		el2 = el - el1;

		if (el1 > 0)
			q.push(el1);
		if (el2 > 0)
			q.push(el2);
	} while(--k);



	printf("Case #%d: %d %d\n", _case, el2, el1);
}

