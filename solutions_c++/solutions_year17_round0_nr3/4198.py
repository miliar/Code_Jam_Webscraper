#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
priority_queue<ll> q;
int main(){
    int T; cin >> T;
    for(ll i = 1; i <= T; i++){
        ll N, K; cin >> N >> K;
        cout << "Case #" << i << ": ";
        ll top = 0;
        q.push(N);
        while(K--){
            top = q.top(); q.pop();
            if(top & 1){
                q.push(top/2);
                q.push(top/2);
            }
            else{
                q.push(top/2 -1);
                q.push(top/2);
            }
        }
        while(!q.empty()) q.pop();
        ll ans1, ans2;
        if(top & 1){
            ans1 = top/2;
            ans2 = top/2;
        }
        else {
            ans1 = top/2;
            ans2 = top/2 - 1;
        }
        cout << ans1 << " " << ans2 << endl;
    }
}
