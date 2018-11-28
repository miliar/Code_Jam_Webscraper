#include<bits/stdc++.h>
using namespace std;

struct hor {
    int s, k;
    double t;
    bool operator <(const hor &p) {
        return (this->t > p.t);
    }
};

hor h[1099];

int main() {
    freopen("a.txt", "r", stdin);
    freopen("asmallOut.txt", "w", stdout);
    int d, n, i, t, tc;
    cin >> tc;
    for(t = 1; t <= tc; t++) {
        cin >> d >> n;
        for(i = 1; i <= n; i++) {
            cin >> h[i].k >> h[i].s;
            h[i].t = ((d - h[i].k)*1.0)/(h[i].s*1.0);
        }
        sort(h + 1, h + n + 1);
        double ans = (d*1.0)/h[1].t;
        printf("Case #%d: %0.6lf\n", t, ans);
    }
    return 0;
    /*cout << h[1].s << " ";
    cout << h[1].k << " ";
    cout << h[1].t << endl;
    cout << h[2].s << " ";
    cout << h[2].k << " ";
    cout << h[2].t << endl;
    cout << h[3].s << " ";
    cout << h[3].k << " ";
    cout << h[3].t << endl;*/
}
