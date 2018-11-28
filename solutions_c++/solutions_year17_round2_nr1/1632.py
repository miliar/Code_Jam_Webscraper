#include <bits/stdc++.h>
#define rep(i, a, n) for(int i = a; i < n; i++)
#define repb(i, a, b) for(int i = a; i >= b; i--)
#define all(a) a.begin(), a.end()
#define o(a) cout << a << endl
#define int long long
#define fi first
#define se second
using namespace std;
typedef pair<int, int> P;


signed main(){
    int tn;
    cin >> tn;
    rep(ti, 0, tn){
        int d, n;
        cin >> d >> n;
        double MAX = 0.0;
        rep(i, 0, n){
            int s, v;
            cin >> s >> v;
            double tmp = (double)(d - s) / (double)v;
            MAX = max(MAX, tmp);
        }
        double ans = d / MAX;
        cout << "Case #" << ti + 1 << ": ";
        printf("%.10lf\n", ans);
    }
}