// 12:20am 4/8
#include <bits/stdc++.h>
#define print(vec, type) copy(vec.begin(), vec.end(), ostream_iterator<type>(cout, " "))
using namespace std;

int T, K, counter;
string S;

void solve(){
  counter=0;
  cin >> S >> K;
  vector<char> S_(S.c_str(), S.c_str() + S.size());
  // copy(S_.begin(), S_.end(), ostream_iterator<char>(cout, " "));
  // print(S_, char);
  for(int i=0; i<=S_.size()-K; ++i){
    if(S_[i]=='-'){
      counter++;
      for(int j=i; j<i+K; ++j){
        S_[j]=(S_[j]=='+')?'-':'+';
      }
    }
    // print(S_, char);
    // cout << '\n';
  }
  for(int i=S_.size()-K+1; i<S_.size(); ++i){
    if(S_[i]!='+'){
      cout << "IMPOSSIBLE";
      // cout << ' ' << i << ' ' << S_[i];
      return;
    }
  }
  cout << counter;
}

int main(){
  cin >> T;
  for(int i=1; i<=T; ++i){
    cout << "Case #" << i << ": ";
    solve();
    cout << endl;
  }
  return 0;
}