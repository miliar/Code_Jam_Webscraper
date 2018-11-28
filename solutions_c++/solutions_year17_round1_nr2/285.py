#include <bits/stdc++.h>
using namespace std;

template<typename T>
void sci(T& t) {
    cin >> t;
}

template<typename T, typename... Ts>
void sci(T& t, Ts&... ts) {
    sci(t);
    sci(ts...);
}

#define scid(vars...) int vars; sci(vars)
#define scidl(vars...) lint vars; sci(vars)
#define scidd(vars...) double vars; sci(vars)
#define scids(vars...) string vars; sci(vars)

template <typename T, typename Cmp=std::greater<T>>
using heap = priority_queue<T, std::vector<T>, Cmp>;

typedef long long lint;

lint a[55][55];
lint r[55];
lint p[55];

void solve() {
    scid(n, m);
    for (int i = 0; i < n; i++) {
        sci(r[i]);
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            sci(a[i][j]);
        }
        sort(a[i], a[i] + m);
        p[i] = 0;
    }

    int ans = 0;
    for (int t = 1; t <= 1e6; t++) {
        bool ok = true;
        for (int i = 0; i < n; i++) {
            while (p[i] < m && 10 * a[i][p[i]] < 9 * r[i] * t) {
                p[i]++;
            }
            if (p[i] == m) {
                cout << ans << "\n";
                return;
            }
            if (a[i][p[i]] * 10 > 11 * r[i] * t) {
                ok = false;
            }
        }
        if (ok) {
            ans++;
            t--;
            for (int i = 0; i < n; i++) {
                p[i]++;
            }
        }
    }
    cout << ans << "\n";
}

int main() {
#ifdef TOXA31
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

    scid(t);
    for (int it = 1; it <= t; ++it) {
//        cerr << it << endl;
        cout << "Case #" << it << ": ";
        solve();
    }

    return 0;
}