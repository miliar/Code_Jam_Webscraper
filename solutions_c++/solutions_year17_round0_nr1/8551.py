#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;
int n;
int main(){
  cin >> n;
  for(int i=1; i<=n; i++){
    string s; int k;
    cin >> s >> k;
    int ret = 0;
    int len =s.length();
    for(int j=0; j<len; j++){
      //printf("(%d,%c)",j,s[j]);
      if(s[j] == '-' && (j+k <= len)){
        for(int t =0; t<k; t++){
          if(s[j+t] == '-')s[j+t] = '+';
          else s[j+t] = '-';
        }ret++;
        //cout << s << '\n';
      }
    }
    bool flag = true;
    for(int j=0; j<len; j++){
      if(s[j] == '-') flag = false;
    }
    if(flag) printf("Case #%d: %d\n",i,ret);
    else printf("Case #%d: IMPOSSIBLE\n",i);
  }
  return 0;
}
