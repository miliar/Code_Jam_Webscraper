#include<iostream>
#include<string>

using namespace std;
using ll = long long;

//ll solve(ll N);
string solve(string N);

int main() {
  int T; cin>>T; cerr<<"Total case: "<<T<<endl;
  for(int i=0;i<T;++i) {
    //ll N; cin >> N;
    string N; cin >> N;
    cerr << "Case #" << i+1 << ": N:"<< N << endl;
    string ans = solve(N);
    cout << "Case #" << i+1 << ": " << ans << endl;
    cerr << " -> " << ans << endl;
  }
  return 0;
}

string solve(string N) {
  string ans = N + '9';
  for(int i=N.size()-2;i>=0;--i) {
    if(ans[i]>ans[i+1]) {
      ans[i]--;
      for(int j=i+1;j<N.size();++j) ans[j]='9';
      cerr << ans << endl;
    }
  }
  if(ans[0]=='0') ans = ans.substr(1,ans.size()-2);
  else ans = ans.substr(0,ans.size()-1);
  return ans;
}

