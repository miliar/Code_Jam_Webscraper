#include <bits/stdc++.h>
#define int long long
#define double long double
#define eps 1e-9
#define inf 1e4
#define fs first
#define sc second
#define pi acos(-1)

using namespace std;

void solve(int X) {
    int N, K;
    cin >> N >> K;
    //out << N << " " << K << '\n';
    double p;
    cin >> p;
    //out << p << '\n';
    vector <double> st;
    double x;
    for (int i = 0; i < N; i++) {
        cin >> x;
        st.push_back(x);
    }
    sort(st.begin(), st.end());

    while (p > eps) {
        int i = 0;
        while (i < N && st[i] - st[0] < eps) {
            i++;
        }
        double add;
        if (i == N) {
            add = p / i;

        } else {
            add = min(p / i, st[i] - st[0]);
        }
        for (int j = 0; j < i; j++) {
            st[j] += add;
        }
        p -= add * i;
    }
    cout << "Case #" << X <<  ": ";
    double ans = 1.0;
    for (double x : st) {
        ans *= x;
    }
    cout << fixed << setprecision(10) << ans;
    cout << '\n';
}


signed main() {
    freopen("input.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t = 1;
    cin >> t;
    for (int i = 1; i <= t; i++) solve(i);
    return 0;
}

