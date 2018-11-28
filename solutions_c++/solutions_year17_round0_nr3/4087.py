#include <bits/stdc++.h>

#define FOR(i,a,b) for (int i = (int)(a); i < (int)(b); ++i)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define x first
#define y second

#define TRACE(x) cerr << #x << " = " << x << endl
#define _ << " _ " <<

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

pii f(int n){return {n-1-n/2, n/2};}

void solve(){

  int n, k;
  cin >> n >> k;

  priority_queue<pii> Q;
  Q.push(f(n));

  REP(ttt,k-1){
    pii curr = Q.top(); Q.pop();
    Q.push(f(curr.x));
    Q.push(f(curr.y));
  }

  cout << Q.top().y << " " << Q.top().x << endl;
  
}

int main(){
  ios_base::sync_with_stdio(false);

  int t;
  cin >> t;
  REP(i,t) cout << "Case #" << i+1 << ": ", solve();

  return 0;
}
