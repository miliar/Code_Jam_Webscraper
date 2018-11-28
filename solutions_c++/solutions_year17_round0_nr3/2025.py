#include <iostream>
#include <queue>

using namespace std;

int64_t solve(int64_t n, int64_t k) {
    priority_queue<pair<int64_t, int64_t>> q;
    q.push({n, 1});
    while (k > q.top().second) {
        int64_t l = q.top().first;
        int64_t count = 0;
        while (!q.empty() && q.top().first == l) {
            count += q.top().second;
            q.pop();
        }
        if (k <= count) {
            return l;
        }
        k -= count;
        q.push({l / 2, count});
        q.push({(l - 1) / 2, count});
    }
    return q.top().first;
}

int main() {
    int T = 10000;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        int64_t n, k;
        cin >> n >> k;
        int64_t l = solve(n, k);
        cout << "Case #" << t << ": " << l / 2 << ' ' << (l - 1) / 2 << endl;
    }
}