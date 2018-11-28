#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;

string s;
int k;

int solve()
{
  int l, r,ans; l=r=ans=0;
  while(true)
  {
    while(l <= s.length()-1 && s[l] == '+')l++;
    //cout << "l vale " << l << endl;
    if(l >= s.length()) return ans;
    else{
      r = l;
      if(r + k-1 >= s.length()) return -1;
      for(int i = 0; i < k; i++){
        if(r >= s.length()) return ans;
        s[r] = (s[r] == '+') ? '-' : '+';
        r++;
      }
      ans++;
      //cout << "Entrando con ans " << ans << endl;
      //cout << s << endl;
    }
  }



  return 0;
}

int main()
{
  int T;
  scanf("%d",&T);
  for(int test = 1; test <= T; test++){
    cin >> s;
    scanf("%d",&k);
    int ans = solve();
    if(ans != -1)
     printf("Case #%d: %d\n",test,ans);
    else
      printf("Case #%d: IMPOSSIBLE\n",test);
    //cout << s << endl;
  }
  return 0;
}