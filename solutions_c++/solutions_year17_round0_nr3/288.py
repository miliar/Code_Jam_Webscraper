#include <bits/stdc++.h>
using namespace std;

void solve(){
    long long n, k, used=0;
    cin >> n >> k;
    map<long long, long long> m;
    m[n] = 1;
    while(true){
        long long max_key = m.rbegin()->first;
        long long sz = max_key;
        long long cnt = m[max_key];
        if(used + cnt < k){
            used += cnt;
            if(sz&1){
                m[sz/2] += 2*cnt;
            }
            else{
                m[sz/2] += cnt;
                if(sz>2) m[(sz-1)/2] += cnt;
            }
            m.erase(max_key);
        }
        else{
            cout << sz/2 << ' ' << (sz-1)/2;
            break;
        }
    }
}

int main(){
    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);
    int t;
    cin >> t;
    for(int c=1; c<=t; c++){
        cout << "Case #" << c << ": ";
        solve();
        cout << endl;
    }
}
