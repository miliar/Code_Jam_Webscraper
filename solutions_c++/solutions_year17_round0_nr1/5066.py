#include <bits/stdc++.h>

using namespace std;

main(){
  int t;
  scanf("%d", &t);

  for(int c=1;c<=t;c++){
    int k;
    string s;
    cin >> s >> k;

    int ans = 0;

    for(int i=0;i<=s.size()-k;i++){
      if(s[i] == '-'){
        ans++;
        for(int j=i;j<i+k;j++)
          s[j] = (s[j] == '+') ? '-' : '+';
      }
    }
    for(int i=s.size()-k;i<s.size();i++)
      if(s[i] == '-')
        ans = -1;

    printf("Case #%d: ", c);
    if(ans < 0) printf("IMPOSSIBLE\n");
    else
      printf("%d\n", ans);
  }
}