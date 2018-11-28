#pragma warning (disable:4996)

#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <climits>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <string>
#include <set>
#include <map>
#include <unordered_map>

using namespace std;

typedef long long ll;
typedef vector<int> vi;

////

#pragma warning (disable:4996)

// A
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("a-l.out", "w", stdout);
	int t, cas = 1;
	cin >> t;
	while (t--) {
		int d, n;
		cin >> d >> n;
		double ans = 0;
		for (int i = 0; i < n; i++) {
			int k, s;
			cin >> k >> s;
			double tm = (d - k) / 1.0 / s;
			ans = max(ans, tm);
		}
		//cout << "Case #" << cas++ << ": " << d / 1.0 / ans << endl;
		printf("Case #%d: %.7lf\n", cas++, d / 1.0 / ans);
	}
	return 0;
}

