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

const double PI = acos(-1.0); 

signed main(){
    int tnum;
	cin >> tnum;
	for(int ti = 1; ti <= tnum; ti++){
        int n, k;
        cin >> n >> k;
        vector<int> r(n), h(n);
        rep(i, 0, n){
            cin >> r[i] >> h[i];
        }
        int MAX = 0;
        rep(i, 0, n){
            vector<int> d;
            int tmp = r[i] * r[i] + 2 * r[i] * h[i];
            rep(j, 0, n){
                if(j == i) continue;
                if(r[j] > r[i]) continue;
                d. push_back(r[j] * h[j]); 
            }
            if(d.size() < k - 1) continue;
            sort(all(d));
            reverse(all(d));
            rep(j, 0, k - 1){
                tmp += 2 * d[j];
            }
            MAX = max(MAX, tmp);
        }
        double ans = (double)MAX * PI;
		cout << "Case #" << ti << ": ";
        printf("%.10lf\n", ans);
	}
}