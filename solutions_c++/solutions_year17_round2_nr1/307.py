#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

void solve(){
  int D; cin >> D;
  int n; cin >> n;
  vector<pii> horses;
  for(int i=0;i<n;i++){
    int p, v; cin >> p >> v;
    horses.push_back(pii(p,v));
  }
  double lo = 0;
  double hi = 1e15;
  for(int ee=0;ee<300;ee++){
    double mid = (hi + lo) / 2;
    bool ok = true;
    for(pii x : horses){
      double p = x.first;
      double v = x.second;
      if(p * mid >= D * (mid - v)){
	continue;
      }
      ok = false;
      break;
    }
    if(ok) lo = mid;
    else hi = mid;
  }
  printf("%.10f", lo);
}

int main(){
  int T; cin >> T;
  for(int i=0;i<T;i++){
    cout << "Case #" << (i+1) << ": "; solve(); cout << "\n";
  }
}
