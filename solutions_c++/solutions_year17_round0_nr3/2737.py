#include <bits/stdc++.h>
#define int long long

using namespace std;

void solve(int x) {
    cout << "Case #" << x << ':' << ' ';
    int n, k;
    cin >> n >> k;
    map <int, int> c;
    set <int> st;
    st.insert(-n);
    c[n] = 1;
    for (int i = 0; i < k; i += 0) {
        int d = *st.begin();
        d *= -1;
        if (i + c[d] < k) {
            int f = d / 2;
            c[f] += c[d];
            st.insert(-f);
            c[d - f - 1] += c[d];
            st.insert(-(d - f - 1));
            i += c[d];
            c[d] = 0;
            st.erase(st.begin());
        } else {
            cout << d / 2 << ' ' << (d - 1) / 2 << '\n';
            return ;
        }
    }
}

signed main() {
    freopen("input.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) solve(i);
    return 0;
}
