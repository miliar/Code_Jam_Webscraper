#include <algorithm>
#include <cassert>
#include <iomanip>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;

// int tbl[1001][1001][1001];

// void solve(int i, int r, int y, int b)
// {
// }

void solve()
{
    int n, r, o, y, g, b, v;
    cin >> n >> r >> o >> y >> g >> b >> v;

    if (r > y + b || y > r + b || b > r + y) {
        cout << "IMPOSSIBLE" << endl;
        return;
    }

    char ix[] = "RYB";
    if (r < y) {
        swap(r, y);
        swap(ix[0], ix[1]);
    }
    if (y < b) {
        swap(y, b);
        swap(ix[1], ix[2]);
    }
    if (r < y) {
        swap(r, y);
        swap(ix[0], ix[1]);
    }

    string ans;
    int prev = 0;
    for (int i = 0; i < n; i++) {
        if (r >= y && r >= b && prev != 1) {
            r--;
            ans += ix[0];
            prev = 1;
        } else if (y >= b && prev != 2) {
            y--;
            ans += ix[1];
            prev = 2;
        } else if (prev != 3) {
            b--;
            ans += ix[2];
            prev = 3;
        } else {
            cerr << prev << ", " << r << ", " << y << ", " << b << endl;
            abort();
        }
    }

    assert(ans[0] != ans[n - 1]);

    cout << ans << endl;
}

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    return 0;
}