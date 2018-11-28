#include <bits/stdc++.h>

using namespace std;

int T, k, ans, f[1005], x, cs;
string s;

int main()
{
  freopen("A-large.in", "r", stdin);
  freopen("out.txt", "w", stdout);

  cin >> T;
  while(T--){
    cin >> s >> k;
    ans = x = 0;
    memset(f, 0, sizeof f);
    for(int i=0; i<s.size(); i++){
      f[i] += i ? f[i - 1] : 0;
      int c = ((s[i] == '-') + f[i]) & 1;
      if(i + k - 1 >= s.size())
        continue;
      if(c){
        ++ans;
        ++f[i];
        --f[i + k];
      }
    }

    for(int i=0; i<s.size(); i++){
      if((f[i] & 1) && s[i] == '+')
        ans = -1;
      else if(!(f[i] & 1) && s[i] == '-')
        ans = -1;
    }
    cout << "Case #" << ++cs << ": ";
    if(ans == -1)
      puts("IMPOSSIBLE");
    else
      cout << ans << "\n";
  }
  return 0;
}
