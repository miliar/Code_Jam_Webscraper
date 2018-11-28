#include <bits/stdc++.h>

#define mt make_tuple
#define mp make_pair
#define pb push_back
#define rs resize

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> ii;
typedef vector<ll> vi;
typedef vector<ld> vld;
typedef vector<vi> vvi;
typedef vector<ii> vii;
typedef vector<string> vs;

const ll inf = 2e17;

int n;
vi e, s;
  vvi d;
  
ld calc(int u, int v){
  vld dist(n,(ld)inf);
  dist[u] = 0;
  vector<bool> sure(n,false);
  for(int i = 0 ; i < n-1 ; i++){
    ld bDist = inf;
    int mJ;
    for(int j = 0 ; j < n ; j++){
      if(sure[j])
        continue;
      if(dist[j] < bDist){
        bDist = dist[j];
        mJ = j;
      }
    }
    int j = mJ;
    sure[j] = true;
    for(int k = 0 ; k < n ; k++){
      if(sure[k])
        continue;
      if(d[j][k] <= e[j])
      dist[k] = min(dist[k], dist[j] + ((ld)d[j][k])/((ld)s[j]));
    }
  }
  return dist[v];
}

void test(){
  int q;
  cin >> n >> q;
  e.clear(); e.rs(n);
  s.clear(); s.rs(n);
  d.clear(); d.rs(n);
  
  for(int i = 0 ; i < n ; i++){
    cin >> e[i] >> s[i];
  }
  for(int i = 0 ; i < n ; i++){
    d[i].rs(n);
    for(int j = 0 ; j < n ; j++){
      cin >> d[i][j];
      if(d[i][j] == -1){
        d[i][j] = inf;
      }
    }
  }
  for(int k = 0 ; k < n ; k++)
    for(int i = 0 ; i < n ; i++)
      for(int j = 0 ; j < n ; j++)
        d[i][j] = min(d[i][j],d[i][k]+d[k][j]);
  
  for(int i = 0 ; i < q ; i++){
    int u, v;
    cin >> u >> v; u--; v--;
    cout << (i == 0 ? "" : " ") << calc(u,v);
  }
  cout << endl;
}

int main(){
    int t;
    cin >> t;
    cout << setprecision(20);
    for( int i = 1;i<= t;i++){
        cout << "Case #" << i << ": ";
        test();
    }
	return 0;
}
