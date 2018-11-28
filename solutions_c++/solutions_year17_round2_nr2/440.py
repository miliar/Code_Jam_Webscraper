#include <iostream>
#include <iomanip>
#include <utility>
#include <vector>

using namespace std;

string try_fill(int a, int b, int c, int n, const string colours) {
    string res(n, '~');
    int cur = 0;
    for (; a > 0; --a) {
        res[cur] = colours[0];
        cur += 2;
        if (cur >= n) {
            cur = 1;
        }
    }
    for(; b > 0; --b) {
        res[cur] = colours[1];
        cur += 2;
        if (cur >= n) {
            cur = 1;
        }
    }
    for (; c > 0; --c) {
        res[cur] = colours[2];
        cur += 2;
        if (cur >= n) {
            cur = 1;
        }
    }
    for (int i = 1; i < n; ++i) {
        if (res[i] == res[i - 1]) {
            return "IMPOSSIBLE";
        }
    }
    if (res[0] == res[n - 1]) {
        return "IMPOSSIBLE";
    }
    return res;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    cin >> T;
    for (int testCase = 0; testCase < T; ++testCase) {
        int n;
        cin >> n;
        int r, y, b, temp;
        cin >> r >> temp;
        cin >> y >> temp;
        cin >> b >> temp;
        cout << "Case #" << testCase + 1 << ": ";
        string ans = try_fill(r, y, b, n, "RYB");
        if (ans != "IMPOSSIBLE") {
            cout << ans << endl;
            continue;
        }
        ans = try_fill(r, b, y, n, "RBY");
        if (ans != "IMPOSSIBLE") {
            cout << ans << endl;
            continue;
        }
        ans = try_fill(y, r, b, n, "YRB");
        if (ans != "IMPOSSIBLE") {
            cout << ans << endl;
            continue;
        }
        ans = try_fill(y, b, r, n, "YBR");
        if (ans != "IMPOSSIBLE") {
            cout << ans << endl;
            continue;
        }
        ans = try_fill(b, r, y, n, "BRY");
        if (ans != "IMPOSSIBLE") {
            cout << ans << endl;
            continue;
        }
        ans = try_fill(b, y, r, n, "BYR");
        cout << ans << endl;
    }
    return 0;
}
