#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int n;
        cin >> n;
        int c[6];
        char cs[] = "ROYGBV";
        vector<pair<int, char>> vc;
        for (int i = 0; i < 6; i++) {
            cin >> c[i];
            vc.push_back({c[i], cs[i]});
        }
        sort(vc.begin(), vc.end());
        reverse(vc.begin(), vc.end());
        bool impos = false;
        for (int i = 0; i < 6; i ++) {
            if (vc[i].first > n / 2) {
                impos = true;
            }
        }
        cout << "Case #" << t << ": ";
        if (impos) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            string s;
            for (int i = 0; i < vc[0].first || i < vc[1].first; i++) {
                if (i < vc[0].first) {
                    s.push_back(vc[0].second);
                }
                if (i < vc[1].first) {
                    s.push_back(vc[1].second);
                }
            }
            reverse(s.begin(), s.end());
            string s2;
            for (int i = 0; i < vc[2].first || i < s.size(); i++) {
                if (i < vc[2].first) {
                    s2.push_back(vc[2].second);
                }
                if (i < s.size()) {
                    s2.push_back(s[i]);
                }
            }
            cout << s2 << endl;
        }
    }
}
