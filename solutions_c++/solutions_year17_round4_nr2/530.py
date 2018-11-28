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

#define REP(i, n) for (int i = 0; i < (int)(n); i++)

void openFiles() {
#ifndef ONLINE_JUDGE
	//freopen("test.in", "rt", stdin);
	//freopen("test.out", "wt", stdout);
	// freopen("B-small-attempt0.in", "rt", stdin);
	// freopen("B-small-attempt0.out", "wt", stdout);
	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out", "wt", stdout);
#endif
}

void solve() {
	int n, c, m; scanf("%d %d %d ", &n, &c, &m);
	vector<int> ridesRemaining(c);

	vector<vector<int> > seatToCustomer(n);
	REP(i, m) {
		int pi, bi; scanf("%d %d ", &pi, &bi);
		bi--, pi--;
		ridesRemaining[bi]++;
		seatToCustomer[pi].push_back(bi);
	}

	int rollers = 0;
	int trains = 0;
	int seats = 0;
	vector<int> customerToNumTrains(c);
	REP(i, n) {
		seats += trains;
		// i - seat number
		REP(j, seatToCustomer[i].size()) {
			int customerIdx = seatToCustomer[i][j];
			if (customerToNumTrains[customerIdx] >= trains || seats <= 0) {
				trains++;
				seats += (1 + i);
			}
			customerToNumTrains[customerIdx]++;
			seats--;
		}
	}

	int swaps = 0;
	REP(i, n) {
		if (seatToCustomer[i].size() > trains) {
			swaps += seatToCustomer[i].size() - trains;
		}
	}
	printf("%d %d\n", trains, swaps);
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
