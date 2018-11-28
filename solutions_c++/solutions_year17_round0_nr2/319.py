#include <algorithm>
#include <iomanip>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

long long n;

void Solve() {
    string sn = to_string(n);
    const int m = sn.length();

    vector<int> a(m);
    for (int i = 0; i < m; ++i) {
        a[i] = sn[i] - '0';
    }

    vector<long long> d(m);
    for (int i = m - 1; i >= 0; --i) {
        d[i] = 0;
        for (int j = i; j < m; ++j) {
            d[i] *= 10;
            d[i] += a[j];
        }
    }

    bool allNines = false;
    long long result = 0;
    for (int i = 0; i < m; ++i) {
        result *= 10;
        if (allNines) {
            result += 9;
            continue;
        }

        long long curValue = 0;
        for (int j = i; j < m; ++j) {
            curValue *= 10;
            curValue += a[i];
        }

        if (curValue <= d[i]) {
            result += a[i];
        } else {
            result += a[i] - 1;
            allNines = true;
        }
    }
    cout << result << endl;
}

void Read() {
    cin >> n;
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
