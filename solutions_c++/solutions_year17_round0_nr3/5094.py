#include <bits/stdc++.h>
using namespace std;

typedef unsigned long long ll;

int T;
ll N, K, crt;

class Comparator {
public:
    bool operator()(const ll &a, const ll &b) {
        return a > b;
    }
};

int main() {
    #ifndef ONLINE_JUDGE
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    #endif // ONLINE_JUDGE

    cin >> T;
    for (int q = 1; q <= T; ++q) {
        cin >> N >> K;
        map < ll, ll, Comparator > H1, H2;

        H1[N] = 1;

        while (K) {
            H2.clear();

            for (auto tmp : H1) {
                crt = tmp.first;

                if (K < tmp.second + 1LL) {
                    K = 0;
                    break;
                } else {
                    K -= tmp.second;
                }

                --crt;
                if (crt % 2 == 0) {
                    H2[crt >> 1] += 2LL * tmp.second;
                } else {
                    H2[crt >> 1] += tmp.second;
                    H2[(crt + 1) / 2] += tmp.second;
                }
            }

            H1 = H2;
        }

        cout << "Case #" << q << ": " << (crt >> 1LL) << ' ' << (crt - 1LL) / 2LL << '\n';
    }
    return 0;
}
