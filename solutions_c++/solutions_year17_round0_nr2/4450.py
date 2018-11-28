#include <bits/stdc++.h>

using namespace std;

vector<long long> v;

void solve() {
  long long n; cin>>n;
  cout<<*prev(upper_bound(v.begin(), v.end(),n))<<endl;
}

int main() {
  vector<long long> tmp;
  for(int i = 1;i < 10;i++) {
    v.push_back(i);
  }
  tmp = v;
  vector<long long> tmp2;
  for(int i = 2;i <= 19;i++) {
    for(auto e : tmp) {
      for(int j = e % 10;j < 10;j++) {
        if(e * 10 + j > 1e18) continue;
        v.push_back(e * 10 + j);
        tmp2.push_back(e * 10 + j);
      }
    }
    tmp = tmp2;
    tmp2.clear();
  }
  assert(freopen("input.txt","r",stdin));
  assert(freopen("output.txt","w",stdout));
  int t; cin>>t;
  for(int i = 1;i <= t;i++) {
    cerr<<"Executing Case #"<<i<<endl;
    cout<<"Case #"<<i<<": ";
    solve();
  }

}
