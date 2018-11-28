#include <bits/stdc++.h>

using namespace std;

using ll = long long;
using ld = long double;

int main() {
    #if __APPLE__
        freopen("in", "r", stdin);
        freopen("out", "w", stdout);
    #endif
    ios::sync_with_stdio(0);
    cin.tie(nullptr);
    int t;
    cin >> t;
    int r = 0;
    while (t--) {
        ++r;
        ll x;
        cin >> x;
        cout << "Case #" << r << ": ";
        int cnt = 0;
        vector<int> a;
        ll w = x;
        while (w) {
            ++cnt;
            a.push_back(w % 10);
            w /= 10;
        }
        reverse(a.begin(), a.end());
        ll res = 0;
        --cnt;
        while (cnt > 0) {
            res = res * 10 + 9;
            --cnt;
        }
        for (int i = 0; i < a.size() - 1; ++i) {
            if (a[i] > a[i + 1]) {
                for (int j = i + 1; j < a.size(); ++j) {
                    a[j] = 9;
                }
                int cur = i;
                while (cur > 0) {
                    if (a[cur] - 1 >= a[cur - 1]) break;
                    --cur;
                }
                --a[cur];
                for (int j = cur + 1; j < a.size(); ++j) {
                    a[j] = 9;
                }
                break;
            }
        }
        /*vector<int> st;
        int st1 = 0;
        for (int i = 1; i <= x; ++i) {
            int w = i;
            vector<int> q;
            while (w) {
                q.push_back(w % 10);
                w /= 10;
            }
            reverse(q.begin(), q.end());
            bool f = true;
            for (int i = 0; i < q.size() - 1; ++i) {
                if (q[i] > q[i + 1]) f = false;
            }
            int p = 0;
            if (f) {
                st = q;
                for (int e : q) p = p * 10 + e;
                st1 = p;
            }
        }*/
        if (a[0] < 1) {
            /*if (res != st1) {
                cout << x << " -- > "  << res << '\n';
                return 0;
            }*/
            cout << res << '\n';
        } else {
            /*if (st != a) {
                cout << x << " -- > " ;
                for (int e : a) cout << e;
                cout << '\n';
                return 0;
            }*/
            for (int e : a) cout << e;
            cout << '\n';
        }
    }
}