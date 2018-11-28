#include <iostream>
#include <algorithm>
#include <bitset>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <iomanip>
#include <queue>
#include <utility>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<int, char> pci;

bool Check(const vector<string>& a) {
    int n = a.size(), m = a.begin()->size();
    for (char c = 'A'; c <= 'Z'; ++c) {
        int min_row = n, min_col = m, max_row = -1, max_col = -1;
        for (int row = 0; row < n; ++row) {
            for (int col = 0; col < m; ++col) {
                if (a[row][col] == c) {
                    min_row = min(min_row, row);
                    max_row = max(max_row, row);
                    min_col = min(min_col, col);
                    max_col = max(max_col, col);
                }
            }
        }
        int cnt = 0;
        for (int row = min_row; row <= max_row; ++row) {
            for (int col = min_col; col <= max_col; ++col) {
                cnt += a[row][col] != '?' && a[row][col] != c;
            }
        }
        if (cnt > 0) {
            return false;
        }
    }
    return true;
}

void Solve(int test_index) {
    int n, m;
    cin >> n >> m;
    vector<string> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    set<char> names;
    for (int row = 0; row < n; ++row) {
        for (int col = 0; col < m; ++col) {
            if (a[row][col] == '?') { continue; }
            names.insert(a[row][col]);
        }
    }
    for (int row = 0; row < n; ++row) {
        for (int col = 0; col < m; ++col) {
            if (a[row][col] != '?') { continue; }
            for (char name : names) {
                a[row][col] = name;
                if (Check(a)) { break; }
            }
        }
    }
    cout << "Case #" << test_index + 1 << ":\n";
    for (int row = 0; row < n; ++row) {
        cout << a[row] << '\n';
    }
}

int main() {
    std::ios_base::sync_with_stdio(false);
    int tests_count;
    cin >> tests_count;
    for (int test_index = 0; test_index < tests_count; ++test_index) {
        Solve(test_index);
    }
    return 0;
}
