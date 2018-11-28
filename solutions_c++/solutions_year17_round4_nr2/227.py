#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
const int MAX_N = 300030;
const ll  MODD = 1000000007;

vector<pair<int,int> > A;

int n,c,m;

int ans = 0;
bool can_do(int rides){
  vector<vector<int> > v(n+10);
  ans = 0;

  for(auto p : A){
    if(v[p.first].size() < rides){
      v[p.first].push_back(p.second);
      continue;
    }
    ans++;

    for(int i=1;i<p.first;i++)
      if(v[i].size() < rides){
        v[i].push_back(p.second);
        goto good;
      }
    return false;
    good:;

  }
  return true;
}

void do_case(){
  cin >> n >> c;
  cin >> m;
  A.clear();
  vector<int> ctr(c+1,0);
  for(int i=0;i<m;i++){
    int p,b; cin >> p >> b;
    A.emplace_back(p,b-1);
    ctr[b-1]++;
  }

  sort(A.begin(),A.end());

  int lo = 1, hi = 1;
  lo = hi = *max_element(ctr.begin(),ctr.end());
  while(!can_do(hi)) hi *= 2;

  while(hi - lo > 3){
    int mid = (hi+lo)/2;
    (can_do(mid) ? hi : lo) = mid;
  }
  while(!can_do(lo)) lo++;

  cout << lo << " " << ans << endl;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout << fixed << setprecision(9);
  
  int T,C=1; cin >> T;
  
  while(T--) {
    cout << "Case #" << C++ << ": ";
    //cout << do_case() << endl;
    do_case();
  }
  
  return 0;
}
