#include <iostream>
#include <vector>
#include <map>

using namespace std;

pair<long long, long long> solve(long long n, long long k) {
    map<long long, long long> segs;
    segs[n] = 1;
    long long passed = 0;
    while (true) {
        auto it = segs.end();
        --it;
        auto p = *it;
        segs.erase(it);
        long long len1 = (p.first - 1) / 2;
        long long len2 = p.first / 2;

        passed += p.second;
        if (passed >= k) {
            return {len1, len2};
        } else {
            segs[len1] += p.second;
            segs[len2] += p.second;
        }
    }
}

int main() {

    freopen("c2.in", "r", stdin);
    freopen("c2.out", "w", stdout);

    int t;
    cin >> t;
    for (int tt = 1; tt <= t; tt++) {
        cerr << tt << endl;
        long long n, k;
        cin >> n >> k;
        cerr << n << " " << k << endl;
        auto p = solve(n, k);
        cout << "Case #" << tt << ": " << p.second << " " << p.first << endl;
    }

    return 0;
}