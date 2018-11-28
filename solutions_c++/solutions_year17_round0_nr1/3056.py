#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <unordered_map>
#include <set>
#include <stack>
#include <bitset>
#include <queue>
#include <numeric>
#include <map>
#include <list>
#include <errno.h>
#include <algorithm>
#include <memory>

#include <iterator>
#include <assert.h>
#include <unordered_set>
#include <sstream>

#define pb push_back
#define mp make_pair

//#define x first
//#define y second

using big = long long;

using namespace std;

string a;

void flip(int x, int y) {
	for (int i = x; i <= y; ++i) {
		a[i] = '+' + '-' - a[i];
	}
}

void solve(int k) {
	int ans = 0;
	int i;
	for (i = 0; i + k - 1 < a.size(); ++i) {
		if (a[i] == '-') {
			++ans;
			flip(i, i + k - 1);
		}
	}
	for (; i < a.size(); ++i) {
		if (a[i] == '-') {
			puts("IMPOSSIBLE");
			return;
		}
	}
	cout << ans << endl;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int cas;
	scanf("%d", &cas);
	for (int cass = 1; cass <= cas; ++cass) {
		int k;
		cin >> a >> k;
		printf("Case #%d: ", cass);
		solve(k);
	}
}

