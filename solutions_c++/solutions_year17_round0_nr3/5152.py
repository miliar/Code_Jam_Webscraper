#include <bits/stdc++.h>
#define ll long long
#define int long long
#define F first
#define S second
using namespace std;

const int N = 1e6 + 10;

struct node {
    int l, r, idx;
    friend bool operator < (node a, node b) {
        if(min(a.l, a.r) != min(b.l, b.r)) return min(a.l, a.r) > min(b.l, b.r);
        if(max(a.l, a.r) != max(b.l, b.r)) return max(a.l, a.r) > max(b.l, b.r);
        return a.idx < b.idx;
    }
    node(){}
    node(int _l, int _r, int _idx) {
        l = _l;
        r = _r;
        idx = _idx;
    }
};

set <node> st;

int n, m, val, l[N], r[N], used[N];

void solve() {
    st.clear();
    cin >> n >> m;
    m--;
    memset(used, 0, sizeof(used));
    int mid = (n + 1) >> 1;
    st.insert(node(mid - 1, n - mid, mid));
    used[0] = used[n + 1] = 1;
    for(int i = 1; i <= m; i++) {
        auto cur = *st.begin();
        st.erase(cur);
        int idx = cur.idx;
        while(!used[idx]) {
            idx--;
        }
        int mid = (cur.idx + idx) >> 1;
        st.insert(node(mid - idx - 1, cur.idx - mid - 1, mid));
        idx = cur.idx;
        while(!used[idx]) {
            idx++;
        }
        mid = (cur.idx + idx) >> 1;
        st.insert(node(idx - mid - 1, mid - cur.idx - 1, mid));
        used[cur.idx] = 1;
    }
    cout << max(st.begin()->l, st.begin()->r) << ' ' << min(st.begin()->l, st.begin()->r) << endl;
}

main() {
    ios_base::sync_with_stdio(0);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int n;
    cin >> n;
    for(int i = 1; i <= n; i++) {
        cout << "Case #" << i << ": ";
        solve();
    }
}
