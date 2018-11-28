#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
using namespace std;
typedef unsigned long long ull;
#define INF 18000000000000000

ull N, K;

ull solve() {
    map<ull, ull> W;
    W[N] = 1;
    ull k = 0;
    ull ans = 0;
    while (k < K) {
        ull z = W.rbegin()->second;
        k += z;
        ans = W.rbegin()->first;
        W.erase(ans);
        ull left = (ans - 1ull) / 2;
        ull right = ans - 1ull - left;
        W[left] += z;
        W[right] += z;
    }
    return ans;
}

int main() {
    int T;  cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> N >> K;
        ull ans = solve();
        ull left = (ans - 1ull) / 2;
        ull right = ans - 1ull - left;
        cout << "Case #" << t << ": " << right << " " << left << endl;
    }
    return 0;
}

