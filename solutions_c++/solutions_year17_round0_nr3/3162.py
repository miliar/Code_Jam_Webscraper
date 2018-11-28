// Copyright 2017 Parallelc
#include <bits/stdc++.h>
#include <ext/numeric>
using namespace std;  // NOLINT
using namespace __gnu_cxx;
using LL = int64_t;
const int INF = 0x3f3f3f3f;
const LL mod = 1000000007;

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin >> t;
    int k = t;
    while (t--) {
        cout << "Case #" << k - t << ": ";
        LL n, k;
        cin >> n >> k;
        deque<pair<LL, LL>> q;
        q.emplace_back(n, 1);
        while (k > q.front().second) {
            k -= q.front().second;
            if (q.front().first % 2 == 0) {
                if (q.back().first == q.front().first / 2) {
                    q.back().second += q.front().second;
                } else {
                    q.emplace_back(q.front().first / 2, q.front().second);
                }
                q.emplace_back(q.front().first / 2 - 1, q.front().second);
            } else {
                if (q.back().first == q.front().first / 2) {
                    q.back().second += q.front().second * 2;
                } else {
                    q.emplace_back(q.front().first / 2, q.front().second * 2);
                }
            }
            q.pop_front();
        }
        if (q.front().first % 2 == 0) cout << q.front().first / 2 << ' ' << q.front().first / 2 - 1 << endl;
        else cout << q.front().first / 2 << ' ' << q.front().first / 2 << endl;
    }
}
