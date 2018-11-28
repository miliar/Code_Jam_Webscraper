#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>

#define debug(x) (cerr << #x << ": " << (x) << endl)

typedef long long ll;
typedef boost::multiprecision::checked_cpp_int bigint;

using namespace std;

void solve(int)
{
    int r, c;
    cin >> r >> c;
    vector<vector<char>> grid(r, vector<char>(c));
    for (auto& v: grid) for (char& ch: v) cin >> ch;

    vector<bool> contains_initial(r, false);
    for (int i = 0; i < r; ++i) {
        for (char ch: grid[i]) if (ch != '?') contains_initial[i] = true;
    }

    int first_filled_row = 0;
    while (!contains_initial[first_filled_row]) ++first_filled_row;
    for (int i = 0; i < first_filled_row; ++i) grid[i] = grid[first_filled_row];
    for (int i = first_filled_row; i < r; ++i) {
        if (!contains_initial[i]) grid[i] = grid[i - 1];
    }

    for (int i = 0; i < r; ++i) {
        auto& v = grid[i];
        int f = 0;
        while (v[f] == '?') ++f;
        for (int j = 0; j < f; ++j) v[j] = v[f];
        for (int j = f; j < c; ++j) {
            if (v[j] == '?') v[j] = v[j - 1];
        }
    }

    cout << "\n";
    for (auto& v: grid) {
        for (char ch: v) cout << ch;
        cout << "\n";
    }
}

int32_t main()
{
    ios_base::sync_with_stdio(false);

    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        solve(i);
    }
}
