#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
ll T;
ll N,Q;
ll E[111],S[111];
ll D[111][111];
ll W[111][111];

const double eps = 1e-6;
const ll INF = (1<<29LL) * (1<<29LL);

void wsf(){
  for(ll i=0;i<N;i++) {
    for (ll j = 0; j < N; j++){
      if( D[i][j] == -1 ) W[i][j] = INF;
      else W[i][j] = D[i][j];
    }
    W[i][i] = 0LL;
  }
  for(ll i=0;i<N;i++)
    for(ll j=0;j<N;j++)
      for(ll k=0;k<N;k++)
        W[j][k] = min( W[j][k], W[j][i] + W[i][k] );
}

typedef pair<double,int> P;
double H[111];

bool isgo( int a, int b ) {
  return W[a][b] <= E[a];
}

double dis( int a, int b ){
  return W[a][b] / (double)S[a];
}

double solve(ll s,ll t){
  fill( H, H+N, 1e15 );
  priority_queue<P,vector<P>,greater<P>> q;
  H[s] = 0.0;
  q.emplace( 0.0, s );
  while( !q.empty() ) {
    P p = q.top(); q.pop();
    double c = p.first;
    int id = p.second;
    if( H[id]+eps < c ) continue;

    for (int i = 0; i < N; i++) {
      if( !isgo( id, i ) ) continue;
      double nc = c + dis( id, i );
      if( H[i]-eps > nc ) {
        q.emplace( nc, i );
        H[i] = nc;
      }
    }
  }
  return H[t];
}

int main(){

  scanf("%d",&T);
  for(ll ttt=1;ttt<=T;ttt++){

    scanf("%d%d",&N,&Q);
    for(ll i=0;i<N;i++)
      scanf("%d%d",&E[i],&S[i]);
    for(ll i=0;i<N;i++)
      for(ll j=0;j<N;j++)
        scanf("%d",&D[i][j]);

    wsf();

    printf("Case #%d: ",ttt);
    for(int i=0;i<Q;i++){
      int s,t; scanf("%d%d",&s,&t); s--; t--;
      if( i ) printf(" ");
      printf("%.9lf",solve(s,t));
    }
    puts("");
  }
}
