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

void solve() {
    scids(s);
    int n = s.size();
    int p = -1;
    for (int i = 0; i + 1 < n; ++i) {
        if (s[i] > s[i + 1]) {
            p = i;
            break;
        }
    }
    if (p != -1) {
        if (s[p] == '1') {
            for (int i = 0; i < n - 1; i++) {
                cout << 9;
            }
            cout << "\n";
            return;
        }
        while (p > 0 && s[p - 1] == s[p]) {
            p--;
        }
        s[p]--;
        for (int i = p + 1; i < n; i++) {
            s[i] = '9';
        }
    }

    cout << s << "\n";
}

int main() {
#ifdef TOXA31
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

    scid(t);
    for (int it = 1; it <= t; ++it) {
        cout << "Case #" << it << ": ";
        solve();
    }

    return 0;
}