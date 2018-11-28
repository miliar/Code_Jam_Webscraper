#include <bits/stdc++.h>

#define F first
#define S second
#define prev azaza
#define mp make_pair
#define pb push_back

using namespace std;
typedef long long ll;
typedef long double ld;

const int max_n = 1001, inf = 1000111222;



int main()
{
    //freopen("B-small-attempt0.in", "r", stdin);
    //freopen("B-small-attempt0.out", "w", stdout);
    int T;
    cin >> T;
    for (int I = 1; I <= T; ++I) {
        int r, o, y, g, b, v, n;
        //cin >> n >> r >> o >> y >> g >> b >> v;
        cin >> r >> y >> b;
        int m[3];
        m[0] = r;
        m[1] = y;
        m[2] = b;
        vector<int> ans;
        int pr = -1;
        int maxx = -1;
        for (int i = 0; i < 3; ++i) {
            if (m[i] > maxx) {
                maxx = m[i];
                pr = i;
            }
        }
        int last = pr;
        ans.pb(pr);
        m[pr]--;
        bool isimp = false;
        while (m[0] + m[1] + m[2]) {
            if (m[0] + m[1] + m[2] == m[last]) {
                isimp = 1;
                break;
            }
            int c1, c2;
            if (last == 0) {
                c1 = 1;
                c2 = 2;
            } else if (last == 1) {
                c1 = 0;
                c2 = 2;
            } else {
                c1 = 0;
                c2 = 1;
            }
            if (m[c1] > m[c2]) {
                ans.pb(c1);
                m[c1]--;
                last = c1;
            } else if (m[c2] > m[c1]) {
                ans.pb(c2);
                m[c2]--;
                last = c2;
            } else {
                if (c1 == pr) {
                    ans.pb(c1);
                    m[c1]--;
                    last = c1;
                } else {
                    ans.pb(c2);
                    m[c2]--;
                    last = c2;
                }
            }
        }
            cout << "Case #" << I << ": ";
            if (isimp || ans[0] == ans.back()) {
                cout << "IMPOSSIBLE";
            } else {
                for (int i = 0; i < ans.size(); ++i) {
                    if (ans[i] == 0) cout << 'R';
                    else if (ans[i] == 1) cout << 'Y';
                    else cout << 'B';
                }
            }
            cout << endl;
    }
    return 0;
}

