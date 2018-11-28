#include <bits/stdc++.h>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define endl "\n"
#define cv(c) (int)(c-'a')
#define db(x) cerr << #x << ": " << x << " "
#define db2(x, y) cerr << #x << ": " << x << " " << #y << ": " << y << " "
#define bn() cerr << endl
#define sep() cerr << "-------" << endl
#define inf 1000000002
#define linf 1000000000000000002

using namespace std;
typedef long long ll;
typedef long double ld;

ll v[100];
struct evento{
    ll x;
    int tipo;
    pair<int, int> ind;
};
vector<evento> ev;
pair<ll, ll> t[100][100];
set<pair<ll, ll> > s[100];
bool cmp(evento a, evento b){
    if (a.x == b.x){
        if (a.tipo == b.tipo) return a.ind < b.ind;
        return a.tipo < b.tipo;
    }
    return a.x < b.x;
}
int main(){
    ios::sync_with_stdio(false);
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("ou", "w", stdout);

    int te;
    cin >> te;
    int caso = 1;
    while (te--){

        int n, p;
        cin >> n >> p;

        for (int i = 0; i < n; i++){
            cin >> v[i];
        }
        memset(t, 0, sizeof(t));
        ev.clear();
        for (int i = 0; i < n; i++){
            for (int j = 0; j < p; j++){
                ll a;
                cin >> a;
                ll l = a * 100;
                ll r = l;
                l = ceil((ld)l / (ld)110);
                r = floor((ld)r / (ld)90);
                l = ceil((ld)l / v[i]);
                r = r / v[i];
                if (l > r) continue;
                evento e;
                e.x = l;
                e.tipo = 1;
                e.ind = mp(i, j);
                ev.pb(e);
                e.x = r;
                e.tipo = 2;
                ev.pb(e);
                t[i][j] = mp(l, r);
                //cout << "Insere " << l << " " << r << " " << endl;
            }
        }
        sort(ev.begin(), ev.end(), cmp);

        for (int i = 0; i < n; i++){
            s[i].clear();
        }
        int res = 0;
        for (int i = 0; i < ev.size(); i++){
            ll val = ev[i].x;
            int tipo = ev[i].tipo;
            pair<ll, ll> onde = ev[i].ind;
            if (tipo == 1){
                s[onde.fi].insert(mp(t[onde.fi][onde.se].fi, onde.se));
            }
            else{
                if (!s[onde.fi].count(mp(t[onde.fi][onde.se].fi, onde.se))) continue;
                bool som = true;
                for (int i = 0; i < n; i++){
                    if (i == onde.fi) continue;
                    if (s[i].size() == 0){
                        som = false;
                    }
                }
                if (som){
                    res++;
                    for (int i = 0; i < n; i++){
                        if (i == onde.fi) continue;
                        s[i].erase(s[i].begin());
                    }
                }
                s[onde.fi].erase(mp(t[onde.fi][onde.se].fi, onde.se));
            }
        }

        cout << "Case #" << caso << ": " << res << endl;
        caso++;
    }
    return 0;
}

