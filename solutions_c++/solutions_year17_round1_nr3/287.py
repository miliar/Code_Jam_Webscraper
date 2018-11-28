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

int w[111][111][111][111];

int m0(int x) {
    return max(0, x);
}

void solve() {
    scid(hd, ad, hk, ak, b, d);
    int ohd = hd;
    int ohk = hk;
    for (int i = 0; i <= hd; ++i) {
        for (int j = 0; j <= max(ad, hk); ++j) {
            for (int k = 0; k <= hk; ++k) {
                for (int l = 0; l <= ak; ++l) {
                    w[i][j][k][l] = -1;
                }
            }
        }
    }

    w[hd][ad][hk][ak] = 0;
    queue<int> q;
    q.push(hd);
    q.push(ad);
    q.push(hk);
    q.push(ak);
    while (!q.empty()) {
        hd = q.front(); q.pop();
        ad = q.front(); q.pop();
        hk = q.front(); q.pop();
        ak = q.front(); q.pop();
        int cur = w[hd][ad][hk][ak];
        if (hk <= 0) {
            cout << cur << "\n";
            return;
        }
        if (hd <= 0) {
            continue;
        }

        if (w[m0(hd - ak)][ad][m0(hk - ad)][ak] == -1) {
            w[m0(hd - ak)][ad][m0(hk - ad)][ak] = cur + 1;
            q.push(m0(hd - ak));
            q.push(ad);
            q.push(m0(hk - ad));
            q.push(ak);
        }

        if (w[m0(hd - ak)][min(ohk, ad + b)][hk][ak] == -1) {
            w[m0(hd - ak)][min(ohk, ad + b)][hk][ak] = cur + 1;
            q.push(m0(hd - ak));
            q.push(min(ohk, ad + b));
            q.push(hk);
            q.push(ak);
        }

        if (w[m0(ohd - ak)][ad][hk][ak] == -1) {
            w[m0(ohd - ak)][ad][hk][ak] = cur + 1;
            q.push(m0(ohd - ak));
            q.push(ad);
            q.push(hk);
            q.push(ak);
        }

        if (w[m0(hd - m0(ak - d))][ad][hk][m0(ak - d)] == -1) {
            w[m0(hd - m0(ak - d))][ad][hk][m0(ak - d)] = cur + 1;
            q.push(m0(hd - m0(ak - d)));
            q.push(ad);
            q.push(hk);
            q.push(m0(ak - d));
        }
    }

    cout << "IMPOSSIBLE\n";
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