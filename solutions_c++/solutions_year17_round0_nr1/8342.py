#include <bits/stdc++.h>
using namespace std;
string s;
int k;
int main(){
  freopen("A-small-attempt0.in", "r", stdin);
  freopen("out.out", "w", stdout);

  int t;
  int cas = 0;
  cin >> t;
  while(t--){
    cin >> s;
    cin >> k;
    int ans = 0, left = 0;
    string cur = "";
    for(int i = 0; i < s.size(); i++){
      if(left){
        if(s[i] == '+')
          s[i] = '-';
        else
          s[i] = '+';
        left--;
      }
      if(s[i] == '-')
        cur.push_back(s[i]);
      else{
        int tmp = cur.size();
        cur.clear();
        ans += (tmp/k);
        if(tmp%k){
          cur.push_back('-');
          left = (k - (tmp%k)) - 1;
          ans++;
        }
      }
    }
    int tmp = cur.size();
    if(tmp%k){
      printf("Case #%d: IMPOSSIBLE\n", ++cas);
    }
    else
      printf("Case #%d: %d\n",++cas,ans + (tmp/k));

  }

  return 0;
}
