#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <deque>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
using namespace std;

#ifdef OLYMP_HXLOCAL
	#define P(expr) (cerr << "[line " << __LINE__ << "] " << #expr << ": " << expr << '\n')
#else
	#define P(expr)
#endif

#define For(i, n) for (int (i) = 0; (i) < (int)(n); (i)++)
#define len(arr) ((int)(arr).size())

typedef long long ll;

const int INT_INF = 1e9;

void solve() {
    int N, C, M;
    cin >> N >> C >> M;
    vector<vector<int>> seats(C);
    vector<int> one_counts(C);
    For (i, M) {
	int P, B;
	cin >> P >> B;
	B--;

	seats[B].push_back(P);
	if (P == 1)
	    one_counts[B]++;
    }

    int height = max(seats[0].size(), seats[1].size());
    P(height);
    P(one_counts[0]);
    P(one_counts[1]);
    int rides = height + max(0, one_counts[0] + one_counts[1] - height);

    for (auto &item : seats)
	sort(item.begin(), item.end());
    if (seats[0].size() < seats[1].size())
	swap(seats[0], seats[1]);
    for (int i = len(seats[1]); i < rides; i++)
	seats[1].push_back(INT_INF + i);

    int best_promotes = INT_INF;
    For (t, 1000) {
	auto order = seats[1];
	random_shuffle(seats[0].begin(), seats[0].end());
	random_shuffle(order.begin(), order.end());

	int promotes = 0;
	For (i, seats[0].size()) {
	    bool found = false;
	    For (j, order.size())
		if (seats[0][i] != order[j]) {
		    order.erase(order.begin() + j);
		    found = true;
		    break;
		}
	    if (!found) {
		promotes++;
		order.pop_back();
	    }
	}

	best_promotes = min(best_promotes, promotes);
    }

    cout << rides << ' ' << best_promotes << '\n';
}

int main() {
#ifndef OLYMP_HXLOCAL
	cin.tie(0);
	ios_base::sync_with_stdio(false);
#endif

	int T;
    cin >> T;
    for (int no = 1; no <= T; no++) {
		cout << "Case #" << no << ": ";
		solve();
	}
	return 0;
}
