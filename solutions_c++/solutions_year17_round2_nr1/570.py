
#include <bits/stdc++.h>
using namespace std;
using ll =long long;
using vl=vector<ll>;
using vb=vector<bool>;
using vs=vector<string>;
using vvl=vector<vl>;
using pll=pair<ll,ll>;
const ll oo =0x3f3f3f3f3f3f3f3fLL;
const double eps=1e-9;
#define sz(c) ll((c).size())
#define all(c) begin(c),end(c)
#define mp make_pair
#define mt make_tuple
#define pb push_back
#define eb emplace_back
#define xx first
#define yy second
#define FOR(i,a,b) for(ll i=(a); i<(b); i++)
#define FORD(i,a,b) for(ll i=ll(b)-1;i>=(a);i--)
#define TR(X) ({if(1) cerr << "TR: " << (#X) << " = " << (X) << endl; })
int main(){ cin.sync_with_stdio(0);
        ll T; cin >> T;
        cout << fixed << setprecision(20) << endl;
        FOR(TC, 1, T+1) {
                ll N, D; cin >> D >> N;
                vector<pll> horses(N);
                FOR(i, 0, N) {
                        cin >> horses[i].xx >> horses[i].yy;
                }
                sort(all(horses));

                double arrival = 0.0;
                FORD(i, 0, N) {
                        double res = (double(D) - horses[i].xx) / horses[i].yy;
                        arrival = max(res, arrival);
                }

                cout << "Case #" << TC << ": " << (D / arrival) << endl;
        }
} //cin.tie(0) bei schnellem Wechseln
