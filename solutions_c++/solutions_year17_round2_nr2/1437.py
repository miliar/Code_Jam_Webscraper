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
        int n;
        int d[6] = {};
        string str = "ROYGBV";
        cin >> n;
        rep(i, 0, 6) cin >> d[i];
        int sum[3] = {};
        int MAX = 0, idx = 0;
        rep(i, 0, 3){
            // int id = i * 2;
            // for(int j = -1; j <= 1; j++){
            //     sum[i] += d[(id + j + 6) % 6];
            // }
            sum[i] = d[i * 2];
            if(sum[i] > MAX){
                MAX = sum[i];
                idx = i * 2;
            }
        }
        string ans = "";
        int add = n - 2 * MAX;
        rep(i, 0, MAX){
            ans += str[idx];
            bool f = false;            
            rep(j, 0, 6){
                if(j != idx && d[j] > 0 && f == false){
                    ans += str[j];
                    d[j]--;
                    f = true;
                    if(i < add) f = false;
                }
            }
        }
        if(MAX > n / 2){
             cout << "Case #" << ti + 1 << ": IMPOSSIBLE" << endl;
        }else{
            cout << "Case #" << ti + 1 << ": " << ans << endl;
        }
    }
}