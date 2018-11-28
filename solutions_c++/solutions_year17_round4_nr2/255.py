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
    int tnum;
	cin >> tnum;
	for(int ti = 1; ti <= tnum; ti++){
        int n, c, m;
        cin >> n >> c >> m;
        int d[1010] = {};
        int cnt[1010] = {};
        rep(i, 0, m){
            int s, t;
            cin >> s >> t;
            s--; t--;
            cnt[t]++;
            d[s]++;
        }
        int MIN = 0;
        rep(i, 0, c) MIN = max(MIN, cnt[i]);
        int ans = MIN;
        rep(i, MIN, m + 1){
            int now = 0;        
            rep(j, 0, n){
                now += d[j];
                if(now > i * (j + 1)) break;
                if(j == n - 1){
                    ans = i;
                    i = m + 1;
                    break;
                }
            }
        }
        int many = 0;
        repb(i, n - 1, 0){
            many += max((int)0, d[i] - ans);
        }
		cout << "Case #" << ti << ": " << ans << " " << many << endl;
	}
}