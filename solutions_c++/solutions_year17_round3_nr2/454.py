#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using ld = long double;

#define __fail() cout << "IMPOSSIBLE\n"; continue;

int n, k;
int f, t;

static constexpr int MINS = 24*60;
auto nxt = [](int x) {
    ++x;
    if (x == MINS) {
        return 0;
    }
    return x;
};

array<int, MINS> mins;
array<int, MINS> his;
array<int, MINS> her;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int TT;
    cin >> TT;
    for (int T = 0; T < TT; ++T) {
        cerr << T << endl;
        cout << "Case #" << T + 1 << ": ";
        cin >> n >> k;
        for (int& m : mins) {
            m = 0;
        }
        if (n == 0) {
            swap(n, k);
        }
        int s = -1;
        for (int i = 0; i < n; ++i) {
            cin >> f >> t;
            for (int j = f; j < t; ++j) {
                mins[j] = 1;
            }
            s = f;
        }
        for (int i = 0; i < k; ++i) {
            cin >> f >> t;
            for (int j = f; j < t; ++j) {
                mins[j] = -1;
            }
        }

        assert(s > -1);
        his.fill(100500);
        her.fill(100500);
        his[1] = 0;
//        his[0] = 0;

//        cerr << " " << s << "\n";

        for (int i = nxt(s); i != s; i = nxt(i)) {
            if (mins[i] == 1) {
                for (int j =  MINS - 100; j >= 0; --j) {
                    his[j + 1] = his[j];
                    if (his[j + 1] > her[j] + 1) {
                        his[j + 1] = her[j] + 1;
                    }
                }
                her.fill(100500);
            } else if (mins[i] == -1) {
                for (int j = 0; j < MINS - 100; ++j) {
                    if (her[j] > his[j] + 1) {
                        her[j] = his[j] + 1;
                    }
                }
                his.fill(100500);
            } else {
                for (int j = MINS - 100; j >= 0; --j) {
                    his[j + 1] = his[j];
                    if (his[j + 1] > her[j] + 1) {
                        his[j + 1] = her[j] + 1;
                    }
                    if (her[j] > his[j] + 1) {
                        her[j] = his[j] + 1;
                    }
                }
            }
        }

        cout << fixed << setprecision(10) << min(her[720] + 1, his[720]) << "\n";
    }

    return 0;
}