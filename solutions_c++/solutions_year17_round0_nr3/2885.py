#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
ll N, K;

void solve(){
    priority_queue<ll> que;
    set<ll> done;
    map<ll, ll> count;
    
    que.push(N);
    done.insert(N);
    count[N] = 1;
    
    while(true){
        auto x = que.top(); que.pop();
        
        ll y = x/2;
        ll z = (x-1)/2;
        
        count[y] += count[x];
        count[z] += count[x];
        
        if(done.find(y) == done.end()){
            que.push(y);
            done.insert(y);
        }
        if(done.find(z) == done.end()){
            que.push(z);
            done.insert(z);
        }
        
        if(K <= count[x]){
            cout << y << " " << z << endl;
            return;
        }
        K -= count[x];
    }
}

int main(){
    int T; cin >> T;
    for(int i=0; i<T; i++){
        cout << "Case #" << i+1 << ": ";
        cin >> N >> K;
        solve();
    }
    
    return 0;
}