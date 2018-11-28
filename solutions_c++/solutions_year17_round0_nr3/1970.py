#include <bits/stdc++.h>

using namespace std;

int main() {
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    ios_base::sync_with_stdio(false);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        long long n, k;
        cin >> n >> k;
        pair<long long, long long> values[2], next_values[4];
        values[0] = make_pair(n, 1);
        int has = 1;
        int pow = 0;
        while ((1ull << (pow + 1)) - 1 < k) {
            for (int i = 0; i < has; ++i) {
                next_values[2 * i] = make_pair((values[i].first - 1) / 2, values[i].second);
                next_values[2 * i + 1] = make_pair(values[i].first / 2, values[i].second);
            }
            sort(next_values, next_values + 2 * has);
            uint8_t new_has = 0;
            long long current = 0;
            for (int i = 0; i < 2 * has; ++i) {
                if (i > 0 && next_values[i].first > next_values[i - 1].first) {
                    values[new_has] = make_pair(next_values[i - 1].first, current);
                    ++new_has;
                    current = 0;
                }
                current += next_values[i].second;
            }
            values[new_has] = make_pair(next_values[2 * has - 1].first, current);
            ++new_has;
            has = new_has;
            ++pow;
        }
        long long diff = k - (1ull << pow) + 1;
        cout << "Case #" << t << ": ";
        reverse(values, values + has);
        if (values[0].second >= diff)
            cout << values[0].first / 2 << " " << (values[0].first - 1) / 2;
        else
            cout << values[1].first / 2 << " " << (values[1].first - 1) / 2;
        cout << '\n';
    }
    return 0;
}
