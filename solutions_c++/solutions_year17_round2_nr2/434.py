#include <bits/stdc++.h>

using namespace std;

int main() {
    ifstream in("input.txt");
    ofstream out("output.txt");
    cin.rdbuf(in.rdbuf());
    cout.rdbuf(out.rdbuf());
    int T;
    cin >> T;
    for (int test = 1; test <= T; test++) {
        cout << "Case #" << test << ": ";
        int n, r, o, y, g, b, v;
        cin >> n >> r >> o >> y >> g >> b >> v;
        vector<pair<int, char>> color{ {r,'r'},{y,'y'},{b,'b'} };
        sort(color.begin(), color.end());
        if (color[2].first > n / 2) {
            cout << "IMPOSSIBLE\n";
            continue;
        }
        string stable(n, color[0].second);
        for (int i = 0; i < color[2].first; ++i)
            stable[2 * i] = color[2].second;
        for (int i = 0; i < color[1].first; ++i)
            stable[n - 1 - n % 2 - 2 * i] = color[1].second;
        cout << stable << endl;
    }
}