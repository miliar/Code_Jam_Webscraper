/**

**/
#include <bits/stdc++.h>
using namespace std;

#define N 200005
#define maxN 1000000007
#define PI 3.14159265358979
#define bb __builtin_popcount
#define ll long long
long long n, test, k;
double a[N], p, kq;
void solve() {
    cin >> test;
    for (int te = 1; te <= test; te++) {
        cin >> n >> k;
        cin >> p;
        for (int i = 1; i <= n; i++) cin >> a[i];
        //sort(a + 1, a + n + 1);
        //for (int i = 1; i <= n; i++) cout << a[i] << " "; cout << endl;
        if (n == 1) {
            a[1] += p;
            p = 0;
        }
        while (p > 0) {
            int l = 1;
            for (int i = 1; i <= n; i++)
                if (a[l] > a[i]) l = i;
            if (a[l] == 1) break;
            int l2 = 0;
            for (int i = 1; i <= n; i++)
                if (i != l)
                    if (l2 == 0) l2 = i;
                    else if (a[l2] > a[i]) l2 = i;
            //cout << l << " " << l2 << " " << p << endl;
            //printf("%d %d %.5f\n", l, l2, p);
            if (p >= a[l2] - a[l]) {
                if (a[l2] == a[l]) {
                    int dem = 0;
                    for (int i = 1; i <= n; i++)
                        if (a[i] == a[l]) dem++;
                    double next = 1.0;
                    for (int i = 1; i <= n; i++)
                        if (a[i] > a[l] && a[i] < next) next = a[i];
                        //printf("now: %.5f", a[l]);
                    //cout << "next: " << next << endl;
                    //cout << "dem: " << dem << endl;
                    if (next == 0) {
                        int o = p / double(dem);
                        double tmp = a[l];
                        p = 0;
                        for (int i = 1; i <= n; i++)
                            if (a[i] == tmp) a[i] += o;
                    } else {
                        if (p > (next - a[l]) * double(dem)) {
                            double tmp = a[l];
                            double o = next - a[l];
                            for (int i = 1; i <= n; i++)
                                if (a[i] == tmp) a[i] += o;
                            p -= o * dem;
                        } else {
                            double tmp = a[l];
                            double o = p / double(dem);
                            for (int i = 1; i <= n; i++)
                                if (a[i] == tmp) a[i] += o;
                            p = 0;
                        }
                    }
                } else {
                    p -= a[l2] - a[l];
                    a[l] = a[l2];
                }
            } else {
                a[l] += p;
                p = 0;
            }
            //for (int i = 1; i <= n; i++) cout << a[i] << " "; cout << endl;
        }
        kq = a[1];
        for (int i = 2; i <= n; i++) kq *= a[i];
        printf("Case #%d: %.9f\n", te, kq);
    }
}
int main() {
    freopen("main.in", "r", stdin);
    //freopen("main.in", "w", stdout);
    freopen("main.out", "w", stdout);
    solve();
    //fclose(stdin);
    //fclose(stdout);
}
///CTKB1997
