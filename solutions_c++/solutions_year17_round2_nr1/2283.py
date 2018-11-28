#include <bits/stdc++.h>

#define F first
#define S second
#define pb push_back
#define INF (1 << 30)
#define SQR(a) ((a) * (a))

using namespace std;

const int N = 1111;

int d, n;
int k[N], s[N];

bool check(double v) {
    double t = d / v;
    for (int i = 0; i < n; i++) {
        double x = t * s[i] + k[i];
        if (x < d)
            return false;
    }
    return true;
}

void solve() {
    cin >> d >> n;
    for (int i = 0; i < n; i++) {
        cin >> k[i] >> s[i];
    }

    double ans = 0;
    for (int i = 0; i < n; i++) {
        double t = (d - k[i]);
        t /= s[i];
        ans = max(ans, t);
    }
    ans = d / ans;
    printf("%.8f", ans);

    //double l = 0;
    //double r = 1e9;

    //while (l < r - 1e-8) {
    //    double m = (l + r) / 2;
    //    if (check(m))
    //        l = m;
    //    else
    //        r = m;
    //}

    //printf("%.8f", l);
}

int main()
{
    //freopen("input.txt", "r", stdin);
    
    int t;
    cin >> t;

    for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        solve();
        cout << endl;
    }
        
    return 0;
}
