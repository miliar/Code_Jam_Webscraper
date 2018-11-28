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

#define For(i, n) for (int (i) = 0; (i) < (n); (i)++)
#define len(arr) ((int)(arr).size())

typedef long long ll;

const int MAX_N = 102;
const int MAX_P = 4;

int P;

const int MAX_HASH = MAX_N * MAX_N * MAX_N * MAX_N;
int dp[MAX_P][MAX_HASH];

int f(int rem, vector<int> mods) {
    int mods_hash = 0;
    for (int count : mods)
        mods_hash = mods_hash * MAX_N + count;
    int *record = &dp[rem][mods_hash];
    if (*record != -1)
        return *record;

    int result = 0;
    For(i, P) {
        if (mods[i] == 0)
            continue;
        mods[i]--;
        result = max(result, f((rem + i) % P, mods) + (rem == 0));
        mods[i]++;
    }
    return *record = result;
}

void solve() {
    int N;
    cin >> N >> P;
    vector<int> mods(P);
    For(i, N) {
        ll group_size;
        cin >> group_size;
        mods[group_size % P]++;
    }

    int cur_max_hash = (N + 1) * MAX_N * MAX_N * MAX_N;
    For(rem, P)
        For(mods_hash, cur_max_hash)
            dp[rem][mods_hash] = -1;
    cout << f(0, mods) << '\n';
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

