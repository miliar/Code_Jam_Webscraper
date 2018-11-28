#include <algorithm>
#include <iomanip>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <unordered_map>
#include <vector>

#include <cassert>
using namespace std;

int n, p;
vector<int> a;
vector<int> c;

int Solve2() {
    const int result = c[0] + (c[1] >> 1);
    return result;
}

int Solve3() {
    int result = 0;
    for (int c111 = 0; c111 <= c[1] / 3; ++c111) {
        c[1] -= c111 * 3;
        for (int c12 = 0; c12 <= c[1] && c12 <= c[2]; ++c12) {
            c[1] -= c12;
            c[2] -= c12;
            for (int c222 = 0; c222 <= c[2] / 3; ++c222) {
                c[2] -= c222 * 3;
                result = max(result, c[0] + c111 + c12 + c222);
                c[2] += c222 * 3;
            }
            c[1] += c12;
            c[2] += c12;
        }
        c[1] += c111 * 3;
    }
    return result;
}

int Solve4() {
    int result = 0;
    for (int c1111 = 0; c1111 <= c[1] / 4; ++c1111) {
        c[1] -= c1111 * 4;
        for (int c13 = 0; c13 <= c[1] && c13 <= c[3]; ++c13) {
            c[1] -= c13;
            c[3] -= c13;
            for (int c112 = 0; c112 <= c[1] / 2 && c112 <= c[2]; ++c112) {
                c[1] -= c112 * 2;
                c[2] -= c112;
                for (int c22 = 0; c22 <= c[2] / 2; ++c22) {
                    c[2] -= c22 * 2;
                    for (int c233 = 0; c233 <= c[2] && c233 <= c[3] / 2; ++c233) {
                        c[2] -= c233;
                        c[3] -= c233 * 2;
                        for (int c3333 = 0; c3333 <= c[3] / 4; ++c3333) {
                            c[3] -= c3333 * 4;
                            result = max(result, c[0] + c1111 + c13 + c112 + c22 + c233 + c3333);
                            c[3] += c3333 * 4;
                        }
                        c[2] += c233;
                        c[3] += c233 * 2;
                    }
                    c[2] += c22 * 2;
                }
                c[1] += c112 * 2;
                c[2] += c112;
            }
            c[1] += c13;
            c[3] += c13;
        }
        c[1] += c1111 * 4;
    }
    return result;
}

void Solve() {
    c.assign(p, 0);
    for (int x : a) {
        ++c[x % p];
    }
    int result;
    if (p == 2) {
        result = Solve2();
    } else if (p == 3) {
        result = Solve3();
    } else if (p == 4) {
        result = Solve4();
    } else {
        assert(false);
    }
    int sum = 0;
    for (int i = 0; i < n; ++i) {
        sum += a[i];
    }
    sum %= p;
    if (sum != 0) {
        ++result;
    }
    cout << result << endl;
}

void Read() {
    cin >> n >> p;
    a.resize(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        Read();
        cout << "Case #" << test << ": ";
        Solve();
    }

    return 0;
}
