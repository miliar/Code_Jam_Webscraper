#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>
using namespace std;


typedef long long i64;
const i64 inf = 1.05e9;

int toidx(int x, int y, int z, int t, int n)
{
	return ((x * (n+1) + y) * (n+1) + z) * 4 + t;
}

void solve(int casenum)
{
	int n, p;
	vector<int> groups;

	scanf("%d%d", &n, &p);
	groups.resize(4);
	for(int i = 0; i < n; ++i) {
		int x;
		scanf("%d", &x);
		groups[x % p] += 1;
	}

	vector<int> dp((n+1) * (n+1) * (n+1) * 4, -inf);
	dp[0] = 0;

	for(int x = 0; x <= groups[1]; ++x) {
		for(int y = 0; y <= groups[2]; ++y) {
			for(int z = 0; z <= groups[3]; ++z) {
				for(int t = 0; t < p; ++t) {

					int& val = dp[toidx(x, y, z, t, n)];

					if(x < groups[1]) {
						int r = (1 + t) % p;
						int& v = dp[toidx(x+1, y, z, r, n)];
						v = max(v, val + (t == 0));
					}

					if(y < groups[2]) {
						int r = (2 + t) % p;
						int& v = dp[toidx(x, y+1, z, r, n)];
						v = max(v, val + (t == 0));
					}

					if(z < groups[3]) {
						int r = (3 + t) % p;
						int& v = dp[toidx(x, y, z+1, r, n)];
						v = max(v, val + (t == 0));
					}
				}
			}
		}
	}

	int ans = 0;
	for(int i = 0; i < p; ++i) {
		int a = groups[0] + dp[toidx(groups[1], groups[2], groups[3], i, n)];
		ans = max(ans, a);
	}

	printf("Case #%d: %d\n", casenum, ans);
}

int main()
{
	int testcase;

	scanf("%d", &testcase);
	for(int i = 1; i <= testcase; ++i)
		solve(i);

	return 0;
}
