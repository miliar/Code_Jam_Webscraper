#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define pll pair<ll, ll>
#define mp make_pair

#define X first
#define Y second


ll t, n, k;

void solve(ll n, ll k){
    map<ll, ll> pq;
    pq.insert(mp(n, 1));

    ll curK = 0;
    while(curK < k){
        map<ll, ll>::iterator pq_iter = --pq.end();
        pll pq_top = *pq_iter;

        pq.erase(pq_iter);

        ll val = pq_top.X;
        ll ptime = pq_top.Y;

        if(val%2 == 1){
            ll tmp = (val - 1)/2;
            map<ll, ll>::iterator it = pq.find(tmp);
            ll ttime;
            if(it == pq.end()){
                ttime = 0;
            }else{
                ttime = it->second;
                pq.erase(it);
            }
            pq.insert(mp(tmp, ttime + ptime*2));
        }else{
            ll tmp = (val - 1)/2;
            map<ll, ll>::iterator it;
            ll ttime;

            it = pq.find(tmp);
            if(it == pq.end()){
                ttime = 0;
            }else{
                ttime = it->second;
                pq.erase(it);
            }
            pq.insert(mp(tmp, ttime + ptime));

            it = pq.find(val - 1 - tmp);
            if(it == pq.end()){
                ttime = 0;
            }else{
                ttime = it->second;
                pq.erase(it);
            }

            pq.insert(mp(val - 1 - tmp, ttime + ptime));
        }
        curK += ptime;
        if(curK >= k){
            cout<<(val-1 - (val-1)/2)<<" "<<(val-1)/2<<endl;
            return;
        }
    }
}

int main(){
    //freopen("input.txt", "r", stdin);
    //freopen("output1.txt", "w", stdout);

    cin>>t;
    for(int i = 0; i < t; i++){
        cin>>n>>k;
        cout<<"Case #"<<i+1<<": ";
        solve(n, k);
    }

    return 0;
}
