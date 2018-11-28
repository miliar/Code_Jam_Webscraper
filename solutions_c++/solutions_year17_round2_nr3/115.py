#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<ll,ll> ii;
typedef long double ld;
typedef pair<ld,int> di;

const int maxn = 110;
const ld eps = 1e-8;
const ll inf = 1e18;
ll n,q;
ii horse[maxn];
ll dist[maxn][maxn];
ld d[maxn];

int main(){
  cout.precision(9);
  cout.setf(ios::fixed);
  int t; cin >> t;
  for(int cass = 1; cass <= t; ++cass){
    cout << "Case #" << cass << ":";
    cin >> n >> q;
    for(int i = 0; i < n; ++i){
      cin >> horse[i].first >> horse[i].second;
    }
    for(int i = 0; i < n; ++i){
      for(int j = 0; j < n; ++j){
        cin >> dist[i][j];
        if(dist[i][j] == -1) dist[i][j] = inf;
      }
    }
    for(int k = 0; k < n; ++k){
      for(int i = 0; i < n; ++i){
        for(int j = 0; j < n; ++j){
          dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j]);
        }
      }
    }
    for(int que = 0; que < q; ++que){
      int u,v;
      cin >> u >> v;
      --u; --v;
      for(int i = 0; i < n; ++i) d[i] = inf;
      d[u] = 0;
      priority_queue<di> q2;
      q2.push(di(0,u));
      while(!q2.empty()){
        di aux = q2.top();
        q2.pop();
        ld x = -aux.first;
        int w = aux.second;
        if(x > d[w]+eps) continue;
        for(int i = 0; i < n; ++i){
          if(dist[w][i] > horse[w].first) continue;
          if(d[i] > x + ld(dist[w][i])/ld(horse[w].second)){
            d[i] = x + ld(dist[w][i])/ld(horse[w].second);
            q2.push(di(-d[i],i));
          }
        }
      }
      cout << ' ' << d[v];
    }
    cout << '\n';
  }
}