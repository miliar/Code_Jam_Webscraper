#include <bits/stdc++.h>
using namespace std;
#define REP(i,a,n) for(int i=(a); i<(int)(n); i++)
#define rep(i,n) REP(i,0,n)
#define FOR(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define ALLOF(c) (c).begin(), (c).end()
typedef long long ll;
typedef unsigned long long ull;

#define INF 1000000000000000000LL

int N, Q;
int E[105];
int S[105];
int G[105][105];
int U[105];
int V[105];

struct ST {
  int a, b;
  double mn;
};
bool operator<(const ST& a , const ST& b){
  return a.mn < b.mn;
}
bool operator>(const ST& a , const ST& b){
  return a.mn > b.mn;
}

double v[105][105];
ll dist[105][105];

void solve(){

  rep(i,N){
    rep(j,N){
      if(G[i][j] == -1) dist[i][j] = INF;
      else dist[i][j] = G[i][j];
    }
  }
  
  rep(k,N) rep(i,N) rep(j,N) dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j]);

  vector<double> ret;
  rep(qq,Q){
    int st = U[qq];
    int gl = V[qq];
    rep(i,N){
      rep(j,N){
        v[i][j] = -1;
      }
    }
    
    priority_queue<ST,vector<ST>,greater<ST>> q;
    q.push((ST){st,st,0});
    while(!q.empty()){
      ST e = q.top(); q.pop();
      if(e.b == gl){
        ret.push_back(e.mn);
        break;
      }
      if(v[e.a][e.b] != -1) continue;
      v[e.a][e.b] = e.mn;
      //cout << " " << e.a << " " << e.b << " " << e.mn << endl;
      
      rep(i,N){
        if(G[e.b][i] == -1) continue;
        if(dist[e.a][i] <= E[e.a]){
          double t = G[e.b][i]/(double)S[e.a];
          //cout << " add1:" << e.a << " " << i << " " << e.mn << " " << t << endl;
          q.push((ST){e.a,i,e.mn+t});
        }
        if(dist[e.b][i] <= E[e.b]){
          double t = G[e.b][i]/(double)S[e.b];
          //cout << " add2:" << e.b << " " << i << " " << e.mn << " " << t << endl;
          q.push((ST){e.b,i,e.mn+t});
        }
      }
    }
  }
  rep(i,ret.size()){
    if(i!=0) printf(" ");
    printf("%.12lf", ret[i]);
  }
}
int main(){
  int T;
  cin >> T;

  rep(t,T){
    cin >> N >> Q;
    rep(i,N){
      cin >> E[i] >> S[i];
    }
    rep(i,N){
      rep(j,N){
        cin >> G[i][j];
      }
    }
    rep(k,Q){
      cin >> U[k] >> V[k];
      U[k]--;
      V[k]--;
    }

    cout << "Case #" << t+1 << ": ";
    solve();
    cout << endl;
  }
  
  return 0;
}



//ios::sync_with_stdio(false);
