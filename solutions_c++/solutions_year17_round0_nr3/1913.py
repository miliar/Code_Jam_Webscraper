#include<bits/stdc++.h>
using namespace std;

long long T, N, K;

map<long long,long long,greater<long long>> M;

int main(){
  cin >> T;
  for(int t=1; t<=T; t++){
    cout << "Case #" << t << ": ";
    M.clear();
    cin >> N >> K;
    M[N] = 1;
    while(true){
      auto p = *M.begin();
      M.erase(M.begin());
      if(p.second >= K){
        cout << (p.first)/2 << " " << (p.first-1)/2 << endl;
        break;
      }
      if(M.count(p.first/2) == 0){
        M[p.first/2] = p.second;
      }
      else{
        M[p.first/2] += p.second;
      }
      if(M.count((p.first-1)/2) == 0){
        M[(p.first-1)/2] = p.second;
      }
      else{
        M[(p.first-1)/2] += p.second;
      }
      K -= p.second;
    }
  }

  return 0;
}
