#include <bits/stdc++.h>
using namespace std;
struct pan {
    double area;
    pan(double a): area(a) {}
    bool operator < (const pan &o) const {
        return area < o.area;
    }
};
struct pan2 {
    double r,h;
    pan2(){}
    pan2(double _r, double _h): r(_r), h(_h) {}
    bool operator < (const pan2 &o) const {
        if(r == o.r) {
            return h > o.h;
        }
        return r > o.r;
    }
};
pan2 in[1005];
priority_queue<pan> Q;
int n, k;
double r[1005],h[1005];
void solve(int Case) {
    cin >> n >> k;
    for (int i = 0; i < n; i++) {
        cin >> in[i].r >> in[i].h;
    }

    sort(in, in+n);
    /*for (int i = 0; i < n; i++) {
        cout << in[i].r << " " << in[i].h << "\n";
    }*/
    double ans = 0;
    for (int i = 0; i < n; i++) {
        if(n - i + 1 < k) break;
        double sum = 2 * in[i].r * M_PI * in[i].h + M_PI * in[i].r * in[i].r;
        while(!Q.empty()) Q.pop();
        for(int j = i+1; j < n; j++) {
            Q.push(pan(2 * in[j].r * M_PI * in[j].h));
        }
        int kk = k-1;
        while(kk-- && !Q.empty()) {
            sum += Q.top().area;
            Q.pop();
        }
        if (kk > 0) continue;
        ans = max(ans, sum);
    }
    cout << "Case #" << (Case+1) <<": ";
    printf("%lf\n", ans);
}

int main () {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    cin >> T;
    for (int i=0;i<T;i++) solve(i);
}
