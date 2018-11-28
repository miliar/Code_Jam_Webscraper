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
#include <cstdio>
#include <cassert>
using namespace std;

void openFiles() {
#ifndef ONLINE_JUDGE
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);
#endif
}

void solve() {
	string line; int n;
	cin >> line >> n;
	int flips = 0;
	for (int i = 0; i <= (line.size() - n); i++) {
		if (line[i] == '-') {
			flips++;
			for (int j = 0; j < n; j++) {
				line[i + j] = (line[i + j] == '+' ? '-' : '+');
			}
		}
	}
	for (int i = 0; i < line.size(); i++) {
		if (line[i] == '-') {
			printf("IMPOSSIBLE\n");
			return;
		}
	}
	printf("%d\n", flips);
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
