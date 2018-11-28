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

const double EPS = 1e-8;

signed main(){
     int tnum;
	cin >> tnum;
	for(int ti = 1; ti <= tnum; ti++){
        int n, k;
        cin >> n >> k;
        double unit;
        cin >> unit;
        vector<double> p(n + 1);
        rep(i, 0, n){
            cin >> p[i];
        }
        p[n] = 1.0;
        int now = -1;
        sort(all(p));
        rep(i, 0, n){
            double tmp = (i + 1) * (p[i + 1] - p[i]);
                // cout << unit << " " << tmp << endl;
            
            if((unit - tmp) > -EPS){
                unit -= tmp;
                rep(j, 0, i + 1) p[j] = p[i + 1];
                // cout << i << " " << p[i] << endl;
            }else{
                rep(j, 0, i + 1) p[j] += unit / (double)(i + 1);
                unit = 0.0;
            }
        }
        double ans = 1.0;
        rep(i, 0, n){
            // cout << " " << p[i] << endl;
            ans *= p[i];
        }
		cout << "Case #" << ti << ": ";
        printf("%.10lf\n", ans);
	}
}