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
        int n, p;
        cin >> n >> p;
        int d[4] = {};
        rep(i, 0, n){
            int a;
            cin >> a;
            d[a % p]++;
        }
        int ans = d[0];
        if(p == 2){
            ans += (d[1] + 1) / 2;
        }else if(p == 3){
            int tmp = min(d[1], d[2]);
            ans += tmp;
            d[1] -= tmp;
            d[2] -= tmp;
            ans += d[1] / 3;
            d[1] %= 3;
            ans += d[2] / 3;
            d[2] %= 3;
            if(d[1] + d[2]) ans++; 
        }else if(p == 4){
            int tmp = min(d[1], d[3]);
            ans += tmp;
            d[1] -= tmp;
            d[3] -= tmp;
            ans += d[1] / 4;
            d[1] %= 4;
            ans += d[3] / 4;
            d[3] %= 4;
            ans += d[2] / 2;
            d[2] %= 2;
            if(d[2] == 1){
                if(d[1] >= 2){
                    d[2]--;
                    d[1] -= 2;
                    ans++;
                }else if(d[3] >= 2){
                    d[2]--;
                    d[3] -= 2;
                    ans++;
                }
            }
            if(d[1] + d[2] + d[3]) ans++;
        }
		cout << "Case #" << ti << ": " << ans << endl;
	}
}