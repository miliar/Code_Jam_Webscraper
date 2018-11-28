#include <bits/stdc++.h>
#define ll long long
#define int long long
#define F first
#define S second
using namespace std;

const int N = 1e5 + 10;

int n, m;
double maxl;
double a[N];

void sol() {
    cin >> n >> m;
    cin >> maxl;
    for(int i = 1; i <= n; i++) {
        cin >> a[i];
    }
    double l = 0, r = 1;
    while(r - l > 1e-15) {
        double mid = (l + r) / 2.;
        double sum = 0;
        for(int i = 1; i <= n; i++) {
            if(mid > a[i]) {
                sum += mid - a[i];
            }
        }
        if(sum <= maxl) {
            l = mid;
        } else {
            r = mid;
        }
    }
    double ans = 1;
    for(int i = 1; i <= n; i++) {
        if(a[i] <= l) {
            ans *= (l);
        } else {
            ans *= (a[i]);
        }
    }
    printf("%.10f", ans);
}

main() {
freopen("C-small-1-attempt1.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    //ios_base::sync_with_stdio(0);
    int n;
    cin >> n;
    for(int i = 1; i <= n; i++) {
        cout << "Case #" << i << ": ";
        sol();
        cout << endl;
    }
}


