#include <iostream>
#include <cmath>

typedef long long ll;

using namespace std;

int main() {
    int T;

    cin >> T;

    for (int t = 1; t <= T; t++) {
        ll N, K;

        cin >> N >> K;

        ll power_2 = 1;

        while (power_2 - 1 < K) {
            power_2 *= 2;
        }

        ll leafs = power_2 / 2;
        ll nodes = power_2 - 1;
        ll actual_leafs = leafs - (nodes - K);


        ll base = (N - nodes) / (2 * leafs);
        ll min_stalls, max_stalls;

        max_stalls = base + ((2 * leafs) * base + actual_leafs <= N - nodes);
        min_stalls = base + ((2 * leafs) * base + leafs + actual_leafs <= N - nodes);
            
        cout << "Case #" << t << ": " << max_stalls << " " << min_stalls << endl;
    }

    return 0;
}
