#include <iostream>
#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <string>

using namespace std;

#define DEBUG

int T;
int n, k;

void solve() {
    cin >> n >> k;

    multiset <int> q;
    q.insert(-n);

    for (int i = 0; i < k - 1; ++i) {
        n = -(*q.begin());
        q.erase(q.begin());

        q.insert(-(n - 1) / 2);
        q.insert(-n / 2);
    }

    n = -(*q.begin());
    cout << n / 2 << " " << (n - 1) / 2;
}

int main() {
    ios::sync_with_stdio(false);

    #ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif

    cin >> T;

    for (int t = 1; t <= T; ++t) {
        cout << "Case #" << t << ": ";
        solve();
        cout << endl;
    }

    return 0;
}