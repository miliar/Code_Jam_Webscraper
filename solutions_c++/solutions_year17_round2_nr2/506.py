#include <iostream>
#include <vector>

using namespace std;

void out(int test, string ans) {
    cout << "Case #" << test << ": ";
    if (ans == "-1") {
        cout << "IMPOSSIBLE";
    } else {
        cout << ans;
    }
    cout << endl;
}

int main() {
    ios_base::sync_with_stdio(false);
    freopen("input", "r", stdin);
    freopen("output", "w", stdout);
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        int n, r, o, y, g, b, v;
        cin >> n >> r >> o >> y >> g >> b >> v;
        if (o >= b && o != 0) {
            out(test, "-1");
            continue;
        }
        if (g >= r && g != 0) {
            out(test, "-1");
            continue;
        }
        if (v >= y && v != 0) {
            out(test, "-1");
            continue;
        }
        string ans = "";
        --r;
        --y;
        --b;
        if (r > y && r > b) {
            ans += "R";
            --r;
        } else if (b > y) {
            ans += "B";
            --b;
        } else {
            ans += "Y";
            --y;
        }
        n = 0;
        while (r >= 0 || y >= 0 || b >= 0) {
            if (ans[n] == 'R') {
                if (y > b) {
                    ans += "Y";
                    --y;
                } else if (b > y) {
                    ans += "B";
                    --b;
                } else if (ans[0] == 'Y') {
                    ans += "Y";
                    --y;
                } else {
                    ans += "B";
                    --b;
                }
            } else if (ans[n] == 'B') {
                if (y > r) {
                    ans += "Y";
                    --y;
                } else if (r > y) {
                    ans += "R";
                    --r;
                } else if (ans[0] == 'Y') {
                    ans += "Y";
                    --y;
                } else {
                    ans += "R";
                    --r;
                }
            } else {
                if (b > r) {
                    ans += "B";
                    --b;
                } else if (r > y) {
                    ans += "R";
                    --r;
                } else if (ans[0] == 'B') {
                    ans += "B";
                    --b;
                } else {
                    ans += "R";
                    --r;
                }
            }
            ++n;
        }
        if (b < -1 || r < -1 || y < -1 || ans[0] == ans[n]) {
            out(test, "-1");
        } else {
            out(test, ans);
        }
    }
    return 0;
}