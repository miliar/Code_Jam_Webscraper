#include <bits/stdc++.h>

using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    ios_base::sync_with_stdio(false);

    int T;
    cin >> T;

    for (int t = 1; t <= T; ++t) {
        int n, r, o, y, g, b, v;
        cin >> n >> r >> o >> y >> g >> b >> v;
        bool res = true;
        int new_r = 0, new_y = 0, new_b = 0;
        if (b <= o && o != 0) {
            res = false;
            if (b + o == n && b == o) {
                cout << "Case #" << t << ": ";
                for (int i = 0; i < b; ++i)
                    cout << "OB";
                cout << "\n";
                continue;
            }
        }
        else
            new_b = b - o;
        if (r <= g && g != 0) {
            res = false;
            if (r + g == n && r == g) {
                cout << "Case #" << t << ": ";
                for (int i = 0; i < r; ++i)
                    cout << "RG";
                cout << "\n";
                continue;
            }
        }
        else
            new_r = r - g;
        if (y <= v && v != 0) {
            res = false;
            if (y + v == n && y == v) {
                cout << "Case #" << t << ": ";
                for (int i = 0; i < y; ++i)
                    cout << "YV";
                cout << "\n";
                continue;
            }
        }
        else
            new_y = y - v;
        if (!res) {
            cout << "Case #" << t << ": " << "IMPOSSIBLE" << "\n";
            continue;
        }

        vector<pair<int, char>> values = {{new_r, 'R'}, {new_y, 'Y'}, {new_b, 'B'}};
        sort(values.begin(), values.end());
        if (values[0].first + values[1].first < values[2].first) {
            cout << "Case #" << t << ": " << "IMPOSSIBLE" << "\n";
            continue;
        }

        vector<char> smalls;
        for (int i = 0; i < values[1].first; ++i)
            smalls.push_back(values[1].second);
        for (int i = 0; i < values[0].first; ++i)
            smalls.push_back(values[0].second);

        vector<char> ans;
        int diff = values[0].first + values[1].first - values[2].first;
        for (int i = 0; i < values[2].first; ++i) {
            ans.push_back(values[2].second);
            ans.push_back(smalls[i]);
            if (i < diff)
                ans.push_back(smalls[values[0].first + values[1].first - 1 - i]);
        }

        cout << "Case #" << t << ": ";
        bool first_r = true, first_y = true, first_b = true;
        for (char c: ans) {
            cout << c;
            if (c == 'R' && first_r) {
                for (int i = 0; i < g; ++i)
                    cout << "GR";
                first_r = false;
            }
            if (c == 'B' && first_b) {
                for (int i = 0; i < o; ++i)
                    cout << "OB";
                first_b = false;
            }
            if (c == 'Y' && first_y) {
                for (int i = 0; i < v; ++i)
                    cout << "VY";
                first_y = false;
            }
        }
        cout << "\n";
    }

    return 0;
}
