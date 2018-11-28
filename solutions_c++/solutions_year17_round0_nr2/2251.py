#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
using namespace std;
char rs[30];
char *solve(){
  char s[30];
  scanf("%s", s);
  int n = strlen(s);
  for(int i = 0; i*2 < n; ++i)
    swap(s[i], s[n-i-1]);

  int last9 = -1;
  for(int i = 1; i < n; ++i){
    if(s[i-1] < s[i]){
      last9 = i-1;
      s[i-1] = '9';
      --s[i];
    }
  }
  if(n > 0 && s[n-1] == '0') --n;
  for(int i = n-1, p = 0; i >= 0; --i){
    rs[p++] = i > last9 ? s[i] : '9';
    rs[p] = 0;
  }
  return rs;
}
int main(){
  int T;
  scanf("%d",&T);
  for(int i = 0; i < T; ++i){
    char *rc = solve();
    printf("Case #%d: %s\n", i+1, rc);
  }
}
