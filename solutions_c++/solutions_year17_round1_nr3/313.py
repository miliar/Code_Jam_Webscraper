#include <bits/stdc++.h>

using namespace std;
#define X first
#define Y second
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;

#define debug(x) cerr << #x << " = " << (x) << endl;
template<typename T>
ostream& operator<<(ostream& o, vector<T>& v) {
    for (auto& x : v) o << x << ' ';
    return o;
}

typedef pair<ll, ll> pll;
const ll INF = LLONG_MAX / 2;
ll Hd, Ad, Hk, Ak, B, D;
pll f(ll hp, ll num_times) {
    ll turns = 0;
    ll dmg = Ak;
    for (int i = 0; i < num_times; i++){
        ll ndmg = max(0LL, dmg - D);
        if (ndmg >= Hd) return {-1, -1};
        if (ndmg >= hp) {
            hp = Hd - dmg;
            turns++, i--;
        } else {
            dmg = ndmg;
            hp -= ndmg;
            turns++;
        }
        if (turns > num_times * 2) return {-1, -1};
    }
    return {hp, turns};
}

pll g(ll hp, ll eatk, ll num_times){
    ll turns = 0;
    for (int i = 0; i < num_times; i++){
        if (eatk >= Hd) return {-1, -1};
        if (eatk >= hp) {
            hp = Hd - eatk;
            turns++, i--;
        } else {
            hp -= eatk;
            turns++;
        }
        if (turns > num_times * 2) return {-1, -1};
    }
    return {hp, turns};
}

ll h(ll hp, ll ehp, ll eatk, ll atk) {
    map<pll, int> memo;
    ll turns = 0;
    for (;;){
        if (memo.count({hp, ehp})) return -1;
        memo[{hp, ehp}] = 1;
        if (atk >= ehp) return turns + 1;
        if (eatk >= Hd) return -1;
        if (eatk >= hp) {
            hp = Hd - eatk;
            turns++;
        } else {
            hp -= eatk;
            ehp -= atk;
            turns++;
        }
    }
    return -1;
}

void solve(){
    cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
    ll res = INF;
    for (int debuff = 0; debuff <= 100; debuff++){
        pll p = f(Hd, debuff);
        if (p.X == -1) continue;
        for (int buff = 0; buff <= 100; buff++){
            pll q = g(p.X, max(0LL, Ak - debuff * D), buff);
            if (q.X == -1) continue;
            ll r = h(q.X, Hk, max(0LL, Ak - debuff * D), Ad + buff * B);
            if (r == -1) continue;
            ll cur = p.Y + q.Y + r;
            if (cur < res) {
                res = min(res, cur);
            }
        }
    }
    if (res == INF) cout << "IMPOSSIBLE" << endl;
    else cout << res << endl;
}

int main(){
    std::ios_base::sync_with_stdio(false); cin.tie(0);
    int tc; cin >> tc;
    for (int cs = 1; cs <= tc; cs++) {
        cout << "Case #" << cs << ": ";
        solve();
    }

}
