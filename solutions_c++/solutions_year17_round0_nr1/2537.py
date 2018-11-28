#include<bits/stdc++.h>
using namespace std;
typedef pair<int,int> PII;
typedef long long ll;
const ll mod = 1e9+7;

void solve(int case_num){
  printf("Case #%d: ",case_num);
  string s;int n;
  cin >> s >> n;
  int res = 0;
  for(int i = 0;i+(n-1) < (int)s.size();++i){
    if(s[i] == '-'){
      ++res;
      for(int j = 0;j < n;++j){
        if(s[i+j] == '+')
          s[i+j] = '-';
        else
          s[i+j] = '+';
      }
    }
  }
  for(int i = 0;i < (int)s.size();++i){
    if(s[i] == '-'){
      cout << "IMPOSSIBLE" << endl;
      return;
    }
  }
  cout << res << endl;
  return;
}


int main(void){
  int n;
  cin >> n;
  for(int i = 0;i < n;++i){
    solve(i+1);
  }
  return 0;
}
