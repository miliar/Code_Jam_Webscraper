#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int MOD = 1e9+7;
void solve(){
    ll n,k;
    cin >> n >> k;
    map<ll,ll> cnt;
    cnt[n]++;
    vector<ll> bfs(1,n);
    for(int i = 0; i < bfs.size(); ++i){
        ll s = bfs[i];
        ll p = (s+1)/2;
        k -= cnt[s];
        //cout << s << ' ' << cnt[s] << ' ' << p << '\n';
        if(k <= 0){
            cout << max(p-1,s-p) << ' ' << min(p-1,s-p) << '\n';
            return;
        }
        if(cnt[s-p] == 0)
            bfs.push_back(s-p);
        cnt[s-p] += cnt[s];
        if(cnt[p-1] == 0)
            bfs.push_back(p-1);
        cnt[p-1] += cnt[s];
    }
}
int main(){
    int t;
    cin >> t;
    for(int tc = 1; tc <= t; ++tc){
        cout << "Case #" << tc << ": ";
        solve();
    }
}
