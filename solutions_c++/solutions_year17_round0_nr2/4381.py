#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <string>
#include <cstring>
#include <sstream>
#include <cstdio>
#include <cassert>
using namespace std;

#define REP(i, n) for (int i = 0; i < (int)(n); i++)

void openFiles() {
#ifndef ONLINE_JUDGE
	//freopen("test.in", "rt", stdin);
	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out", "wt", stdout);
#endif
}

void solve(long long val) {
	stringstream ss; ss << val;
	string num = ss.str();
	int n = num.size();
	for (int i = 0; i < n - 1; i++) {
		if (num[i + 1] < num[i]) {
			for (int j = i + 1; j < n; j++) {
				num[j] = '9';
			}
			int k = i;
			for (; k > 0; k--) {
				if (num[k - 1] < num[k]) {
					break;
				} else {
					num[k] = '9';
				}
			}
			if (k > 0 || num[k] >= '2') {
				num[k]--;
			} else {
				num = num.substr(1);
			}
			break;
		}
	}
	printf("%s\n", num.c_str());
}

void solve() {
	long long val; cin >> val;
	solve(val);
}

int main() {
    openFiles();
    int n; scanf("%d ", &n);
    for (int i = 0; i < n; i++) {
            printf("Case #%d: ", i + 1);
            solve();
    }
    return 0;
}
