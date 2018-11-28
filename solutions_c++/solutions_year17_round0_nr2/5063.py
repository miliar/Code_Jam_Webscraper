#include <bits/stdc++.h>

using namespace std;

main(){
  int t;
  scanf("%d", &t);

  for(int c=1;c<=t;c++){
    printf("Case #%d: ", c);

    string s;
    cin >> s;

    if(s.size() == 1){
      printf("%c\n", s[0]);
      continue;
    }

    int nove = s.size();
    for(int i=s.size()-1;i>0;i--){
      if(s[i-1] > s[i]){
        nove = i;
        s[i-1]--;
      }
    }

    int i = 0;
    while(s[i] == '0')
      i++;
    for(;i<nove;i++)
      printf("%c", s[i]);
    for(int i=nove;i<s.size();i++)
      printf("9");

    printf("\n");
  }
}