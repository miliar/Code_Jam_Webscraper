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

int calc_days(vector<pair<int, int>>& ts) {
    sort(ts.begin(), ts.end());

    int res = 0;
    auto c = ts.size();
    vector<bool> on(c);
    vector<bool> tk(ts.size());
    int act = 0;
    while (act < ts.size()) {
        res++;
        fill(on.begin(), on.end(), false);
        int ct = 0;
        for (int i = 0; i < ts.size(); i++) {
            if (tk[i] || on[ts[i].second] || ts[i].first < ct) {
                continue;
            }
            tk[i] = true;
            on[ts[i].second] = true;
            ct++;
            act++;
        }
    }

    return res;
}

void solve() {
    scid(n, c, m);
    vector<pair<int, int>> ats;
    for (int i = 0; i < m; i++) {
        scid(p, b);
        --p; --b;
        ats.push_back({p, b});
    }

    int days = calc_days(ats);
    cout << days << " ";
    vector<int> cnt(n);
    for (auto& i : ats) {
        cnt[i.first]++;
    }

    int ap = 0;
    for (; days > 0; days--) {
        int cp = 0;
        for (int i = n - 1; i >= 0; i--) {
            int np = cnt[i] + cp - days;
            ap += max(0, np - cp);
            cnt[i] -= max(0, np - cp) + 1;
            cp = np;
        }
    }

    cout << ap << "\n";
}

int main() {
#ifdef TOXA31
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

    scid(t);
    for (int it = 1; it <= t; it++) {
        cout << "Case #" << it << ": ";
        solve();
    }

    return 0;
}