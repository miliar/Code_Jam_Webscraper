#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("a-large.in","r",stdin);
    freopen("a-large.out","w",stdout);

    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        string s;
        int k;
        cin >> s >> k;

        cout << "Case #" << i+1 << ": ";

        int r = s.size();
        vector<int> v(r,0);
        for (int j = 0; j < r; j++) {
            if (s[j] == '-')
                v[j] = 1;
        }

        int ret = 0;
        bool pos = true;
        for (int j = 0; j < r; j++) {
            if (j > r-k) {
                if (v[j] == 1) {
                    cout << "IMPOSSIBLE\n";
                    pos = false;
                    break;
                }
                continue;
            }
            if (v[j] == 1) {
                for (int l = j; l < j+k; l++) {
                    v[l]++;
                    v[l]%=2;
                }
                ret++;
            }
        }

        if (pos) {
            cout << ret << "\n";
        }
    }
}
