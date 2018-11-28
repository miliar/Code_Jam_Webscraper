#include <bits/stdc++.h>

using namespace std;

using ld = long double;
using ll = long long;

const ld PI = acos(-1.0);

#define gcj cout << "Case #" << Test << ": "

void print(const vector<ld>& a) {
    for (auto el : a) {
        cout << el << ' ';
    }
    cout << '\n';
}

int main() {
    
    ll tests;
    cin >> tests;
    cout << fixed;
    cout.precision(15);
    for (ll Test = 1; Test <= tests; ++Test) {

        int n, k;
        cin >> n >> k;
        ld train;
        cin >> train;
        vector <ld> probs(n);
        for (int i = 0; i < n; ++i) {
            cin >> probs[i];
        }
        sort(probs.begin(), probs.end());
        probs.push_back(1.0);
        for (int i = 0; i < n; ++i) {
            ld diff = probs[i + 1] - probs[i];
            if (diff * (i + 1) <= train) {
                for (int j = 0; j <= i; ++j) {
                    probs[j] += diff;
                }
                train -= diff * (i + 1);
            } else {
                for (int j = 0; j <= i; ++j) {
                    probs[j] += train / (i + 1);
                }
                break;
            }
            // print(probs);
        }

        ld ans = 1;
        for (size_t i = 0; i < probs.size(); ++i) {
            ans *= probs[i];
        }

        gcj;
        cout << ans << '\n';
    }
}