#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
double dp[1100][1100]; 

struct node{
  ll r;ll h;int id;
  bool operator>(const node &right) const{
    return r*h > right.r*right.h;
  }
};

void solve(){
  int n,k;
  vector< node > nodes;
  cin >> n >> k;
  for(int i = 0;i < n;++i){
    ll r,h;
    cin >> r >> h;
    node n = {r,h,i};
    nodes.push_back(n);
  }
  sort(nodes.begin(),nodes.end(),greater< node >());
  double res = 0;
  for(int i = 0;i < n;++i){
    node b = nodes[i];
    int cnt = 1;
    double calc = M_PI * b.r * b.r;
    calc += 2 * M_PI * b.r * b.h;
    for(int j = 0;j < n;++j){
      node now = nodes[j];
      if(cnt == k)break;
      if(now.id != b.id &&
         b.r >= now.r){
        calc += 2 * M_PI * now.r * now.h;
        ++cnt;
      }
    }
    if(cnt == k)
      res = max(res,calc);
  }
  cout << setprecision(15) << res << endl;
}


int main(void){
  int t;
  cin >> t;
  for(int i = 0;i < t;++i){
    printf("Case #%d: ",i+1);
    solve();
  }
  return 0;
}
