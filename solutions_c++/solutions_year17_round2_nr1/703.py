#include "bits/stdc++.h"
using namespace std;
using ll = long long;
using P = pair<ll, ll>;
const ll MOD = 1000000007;

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int D, N;
        cin >> D >> N;
        double max_time = 0;
        for (int i = 0; i < N; i++) {
            int K, S;
            cin >> K >> S;
            max_time = max(max_time, double(D - K) / S);
        }
        printf("Case #%d: %.8f\n", t, D / max_time);
    }
    return 0;
}
