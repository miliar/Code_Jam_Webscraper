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
    scidl(n, k);
    map<lint, lint> m;
    m[n] = 1;
    while (true) {
        auto it = *m.rbegin();
        m.erase(m.rbegin()->first);
        lint mx = it.first / 2;
        lint mn = it.first - 1 - mx;
        if (it.second >= k) {
            cout << mx << " " << mn << "\n";
            break;
        }
        k -= it.second;
        m[mx] += it.second;
        m[mn] += it.second;
    }
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