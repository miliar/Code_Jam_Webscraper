#include <bits/stdc++.h>
using namespace std;

bool check(const string& s){
  for(char c : s)
    if( c == '-' ) return false;
  return true;
}

int main(){
  int T; cin >> T;
  for(int ttt=1;ttt<=T;ttt++){

    int K;
    string S;
    cin >> S >> K;

    int res = 0;
    for(int i=0;i<S.size()-K+1;i++){
      if( S[i] == '-' ) {
        res++;
        for(int j=i;j<i+K;j++)
          S[j] = (S[j]=='-'?'+':'-');
      }
    }

    cout << "Case #" << ttt << ": ";
    if( check( S ) ) cout << res << endl;
    else cout << "IMPOSSIBLE" << endl;
  }
}