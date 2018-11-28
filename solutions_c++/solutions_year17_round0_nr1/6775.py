#include<iostream>
#include<string>
#include<vector>

using namespace std;

void solve(string S, int K){
  int flips = 0;
  for(int i = 0; i < S.size()-K+1; i++){
    if(S[i] == '-'){
      flips++;
      for(int j = i; j < i+K; j++){
        if(S[j] == '-'){
          S[j] = '+';
        }else{
          S[j] = '-';
        }
      }
    }
  }
  if(K == 1){
    cout << flips << endl;
    return;
  }
  bool ok = true;
  // Check if last part is ok
  for(int i = S.size()-K+1; i < S.size(); i++){
    if(S[i] == '-'){
      ok = false;
      break;
    }
  }
  if(ok == true){
    cout << flips << endl;
  }else{
    cout << "IMPOSSIBLE" << endl;
  }
}

int main(){
  int T;
  cin >> T;
  int K;
  string S;
  for(int i = 0; i < T; i++){
    cin >> S;
    cin >> K;
    cout << "Case #" << i+1 << ": ";
    solve(S,K);
  }
  return 0;
}
