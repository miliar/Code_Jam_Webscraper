
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
        cout << fixed << setprecision(20);
        FOR(TC, 1, T+1) {
                ll N, Q; cin >> N >> Q;
                vl es(N), ss(N);
                FOR(i, 0, N) cin >> es[i] >> ss[i];

                vvl adj(N, vl(N, oo));
                FOR(i, 0, N) {
                        FOR(j, 0, N) {
                                cin >> adj[i][j];
                        }
                }

                vector<vector<double>> new_adj(N, vector<double>(N, DBL_MAX));

                FOR(start, 0, N) {
                        priority_queue<pair<double, pll>, vector<pair<double, pll>>, greater<pair<double, pll>>> todo;

                        todo.push( {0.0, {start, es[start]}});

                        while (sz(todo)) {
                                pair<double, pll> cur = todo.top();
                                todo.pop();

                                double time = cur.xx;
                                ll city = cur.yy.xx;
                                ll remaining = cur.yy.yy;

                                FOR(i, 0, N) {
                                        if (adj[city][i] == -1 || i == city) continue;
                                        double new_dis = time + double(adj[city][i]) / ss[start];
                                        ll new_remaining = remaining - adj[city][i];
                                        if (new_remaining < 0) continue;
                                        if (new_dis >= new_adj[start][i]) continue;

                                        new_adj[start][i] = new_dis;
                                        todo.push( {new_dis, {i, new_remaining}} );
                                }
                        }
                }

                //FOR(i, 0, N) { FOR(j, 0, N) { cout << new_adj[i][j] << "\t"; } cout << endl; }
                vector<vector<double>> dis(new_adj);
                FOR(i, 0, N) dis[i][i] = 0.0;

                FOR(k, 0, N) {
                FOR(i, 0, N) {
                FOR(j, 0, N) {
                        if (dis[i][k] == DBL_MAX || dis[k][j] == DBL_MAX) continue;
                        dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j]);
                }
                }
                }


                //FOR(i, 0, N){FOR(j, 0, N) { cout << dis[i][j] << "\t"; }cout << endl;}

                cout << "Case #" << TC << ":";
                FOR(i, 0, Q) {
                        ll U, V; cin >> U >> V;
                        U --, V--;
                        cout << " " << dis[U][V];
                }
                cout << endl;
        }
} //cin.tie(0) bei schnellem Wechseln
