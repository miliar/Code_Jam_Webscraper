#include <bits/stdc++.h>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int N, R, O, Y, G, B, V;
        cin >> N >> R >> O >> Y >> G >> B >> V;
        vector<string> ans(max(max(R, Y), B));
        int pos = 0;
        vector<pair<int, char>> v = {{R, 'R'}, {Y, 'Y'}, {B, 'B'}};
        sort(v.begin(), v.end());
        for (auto &pr : v) {
            for (int j = 0; j < pr.first; j++) {
                ans[pos].push_back(pr.second);
                pos++;
                if (pos == ans.size()) {
                    pos = 0;
                }
            }
        }
        string res = "";
        bool ok = true;
        for (auto &b : ans) {
            if (b.length() < 2) {
                ok = false;
            }
            res += b;
        }
        if (!ok) {
            res = "IMPOSSIBLE";
        }
        
        cout << "Case #" << t << ": " << res << endl;
    }
}



