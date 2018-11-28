#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

const int DEAD = 100000;

set<ll> seen;
int B, D;
int init_health;
int res;

ll encode(int hd, int ad, int hk, int ak) {
    ll res = hd;
    res *= 1000;
    res += ad;
    res *= 1000;
    res += hk;
    res *= 1000;
    res += ak;
    return res;
}

void decode(ll value, int &hd, int &ad, int &hk, int &ak) {
    ak = value % 1000;
    value /= 1000;
    hk = value % 1000;
    value /= 1000;
    ad = value % 1000;
    value /= 1000;
    hd = value % 1000;
    value /= 1000;
}

void solve(){
    seen.clear();
    res = DEAD;
    int hd, ad, hk, ak;
    cin >> hd >> ad >> hk >> ak >> B >> D;
    init_health = hd;
    
    queue<pair<ll, int> > q;
    ll start = encode(hd, ad, hk, ak);
    seen.insert(start);
    q.push(make_pair(start, 0));
    
    while (!q.empty()){
        pair<ll, int> plli = q.front();
        q.pop();
        decode(plli.first, hd, ad, hk, ak);
        int nb = plli.second;
        
        if (ad >= hk){
            cout << nb + 1 << endl;
            return;
        }
        
        { // ATK
            int _hd = hd, _ad = ad, _hk = hk - ad, _ak = ak;
            _hd -= _ak;
            ll encoded = encode(_hd, _ad, _hk, _ak);
            if (_hd > 0 && seen.count(encoded) == 0){
                q.push(make_pair(encoded, nb + 1));
                seen.insert(encoded);
            }
        }
        { // DEBUFF
            int _hd = hd, _ad = ad, _hk = hk, _ak = max(ak - D, 0);
            _hd -= _ak;
            ll encoded = encode(_hd, _ad, _hk, _ak);
            if (_hd > 0 && seen.count(encoded) == 0){
                q.push(make_pair(encoded, nb + 1));
                seen.insert(encoded);
            }
        }
        { // HEAL
            int _hd = init_health, _ad = ad, _hk = hk, _ak = ak;
            _hd -= _ak;
            ll encoded = encode(_hd, _ad, _hk, _ak);
            if (_hd > 0 && seen.count(encoded) == 0){
                q.push(make_pair(encoded, nb + 1));
                seen.insert(encoded);
            }
        }
        { // BUFF
            int _hd = hd, _ad = ad + B, _hk = hk, _ak = ak;
            _hd -= _ak;
            ll encoded = encode(_hd, _ad, _hk, _ak);
            if (_hd > 0 && seen.count(encoded) == 0){
                q.push(make_pair(encoded, nb + 1));
                seen.insert(encoded);
            }
        }
    }
    cout << "IMPOSSIBLE" << endl;
}
    
    
    

int main(){
    int T;
    cin >> T;
    for (int i=1; i<=T; i++){
        cout << "Case #" << i << ": ";
        solve();
    }
}
    
