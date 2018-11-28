#include <bits/stdc++.h>

using namespace std;

void solve(int time){
  int n,p;
  cin >> n >> p;
  vector<int> g(n);
  int s[4] = {0,0,0,0};
  for(int i = 0;i < n;i++){
    cin >> g[i];
    g[i] %= p;
    s[g[i]]++;
  }
  int ans = 0;
  ans += s[0];
  if(p == 2){
    ans += (s[1]+1)/2;
  }
  else if(p == 3){
    if(s[1] > s[2]){
      ans += s[2];
      ans += (s[1]-s[2]+2)/3;
    }
    else{
      ans += s[1];
      ans += (s[2]-s[1]+2)/3;
    }
  }
  else{
    if(s[1] > s[3]){
      ans += s[3];
      s[1] -= s[3];
    }
    else{
      ans += s[1];
      s[1] = s[3]-s[1];
    }
    int ss = s[2]*2+s[1];
    ans += (ss+3)/4;
  }
  cout << "Case #" << time << ": ";
  cout << ans << endl;
}

int main(void){
  int t;
  cin >> t;
  for(int i = 1;i <= t;i++){
    solve(i);
  }
}
