//#pragma comment(linker, "/STACK:134217728")

#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
using namespace std;

typedef long long Int;
typedef pair<int,int> PII;
typedef vector<int> VInt;

#define FOR(i, a, b) for(i = (a); i < (b); ++i)
#define RFOR(i, a, b) for(i = (a) - 1; i >= (b); --i)
#define CLEAR(a, b) memset(a, b, sizeof(a))
#define SIZE(a) int((a).size())
#define ALL(a) (a).begin(),(a).end()
#define PB push_back
#define MP make_pair

int R[1 << 10];
int H[1 << 10];

int SolveTest(int test)
{
	int N, K;
	scanf("%d%d", &N, &K);

	int i, j;
	FOR(i, 0, N)
		scanf("%d%d", &R[i], &H[i]);


	double res = 0;
	FOR(i, 0, N)
	{
		vector<Int> v;
		FOR(j, 0, N)
			if (i != j && R[j] <= R[i])
				v.push_back(Int(H[j])*R[j]);

		if (SIZE(v) < K - 1) continue;
		sort(ALL(v));
		v.push_back(Int(H[i])*R[i]);
		reverse(ALL(v));
		Int sum = accumulate(v.begin(), v.begin() + K, 0LL);
		res = max(res, (2 * acos(0.0))*(2*sum + Int(R[i])*R[i]));
	}

	printf("Case #%d: %.11lf\n", test + 1, res);
	return 0;
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int T, t;
	char buf[1 << 7];
	fgets(buf, 1 << 7, stdin);
	sscanf(buf, "%d", &T);
	FOR(t, 0, T)
	{
		fprintf(stderr, "Solving %d/%d\n", t + 1, T);
		SolveTest(t);
	}

	return 0;
};
