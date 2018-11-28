#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>
#include <iomanip>

#define For(i,a,b) for(ll i = a; i < b; i++)
#define rep(i,x) For(i,0,x)
#define foreach(i,c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define sz(x) ((ll)(x).size())
#define F first
#define S second
#define pb push_back
#define mp make_pair
#define TWO(x) (1LL<<(x))

using namespace std;

#define ll long long

int main() {
    ll np; cin>>np;
    rep(i, np){
        cout << "Case #"<<(i+1)<<":";

        ll n, q; cin>>n>>q;
        ll E[n];
        ll S[n];
        rep(i, n) {
            cin >> E[i] >> S[i];
        }

        ll D[n][n];
        rep(i, n) rep(j,n) {
            cin >> D[i][j];
        }
        rep(i, n) {
            D[i][i] = 0;
        }

        rep(k, n) {
            rep(i, n) {
                rep(j, n){
                    if(D[i][k] >= 0 && D[k][j] >= 0) {
                        ll attempt = D[i][k] + D[k][j];
                        if(D[i][j] == -1 || attempt < D[i][j]) {
                            D[i][j] = attempt;
                        }
                    }
                }
            }
        }

        rep(i, q) {
            double infi = std::numeric_limits<double>::max();

            ll start, finish; cin>>start>>finish;
            start--; finish--;
            vector<bool> V(n, false);
            vector<double> T(n, infi);
            set<pair<double, ll> > queue;
            T[start] = 0.0;
            queue.insert(make_pair(0.0, start));
            while(!queue.empty()) {
                auto it = queue.begin();
                ll at = it->second;
                queue.erase(it);
                if(V[at]) {
                    continue;
                }
                V[at] = true;

                double time = T[at];
                rep(to, n) {
                    ll dist = D[at][to];
                    //cout << "HEY:" << at << " " << to << " " << dist << " " << E[at] << endl;
                    if(dist >= 0 && dist <= E[at]) {
                        double hit_time = time + dist / double(S[at]);
                        if(hit_time < T[to]) {
                            assert(!V[to]);
                            T[to] = hit_time;
                            queue.insert(make_pair(hit_time, to));
                        }
                    }
                }
            }
            assert(V[finish] && T[finish] != infi);
            cout << " " << setprecision(10) << fixed << T[finish];
        }

        cout << endl;
    }
}
