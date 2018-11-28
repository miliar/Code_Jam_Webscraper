#include <bits/stdc++.h>
using namespace std;

int solve(string x, int k){
  int flips = 0;
  int len = x.size();
  int i;
  
  for(i=0;i+k-1 < len; ++i){
    if(x[i] == '+') continue;
    for(int j=0;j<k;++j){
      x[i+j] = (x[i+j] == '+'? '-':'+');	
    }
    ++flips;
  }
  
  --i;
  for(;i<len;++i){
    if(x[i] == '-') return -1;
  }
  return flips;
}

int main(){
  ios::sync_with_stdio(false);
  
  int T;
  cin >> T;
  
  for(int t=0; t<T; ++t){
    string str;
    int k;
    cin >> str >> k;
    
    int res = solve(str, k);
    if(res == -1)
      cout << "Case #" << t + 1 <<": " << "IMPOSSIBLE" << endl;
    else
      cout << "Case #" << t + 1 <<": " << res << endl;    
  }
  
  return 0;
}