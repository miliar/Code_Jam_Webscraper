#include <stdio.h>

char s[55];

int main(){
  int T;
  scanf("%d", &T);
  for(int tc=0; tc<T; tc++){
    scanf("%s", s);
    int len;
    for(len=0; s[len]; len++);
    int valid = 1;
    for(int i=1; i<len; i++) if(s[i-1] > s[i]) valid = 0;
    if(valid){ printf("Case #%d: %s\n", tc+1, s); continue; }
    for(int nine=1; nine<len; nine++){
      for(int i=0; i<nine; i++) s[len-i-1] = '9';
      s[len-nine-1]--;
      int valid = 1;
      for(int i=0; i<len; i++) if(s[i] < '0' || s[i] > '9') valid = 0;
      for(int i=1; i<len; i++) if(s[i-1] > s[i]) valid = 0;
      if(valid){
        printf("Case #%d: ", tc+1);
        int foundnonzero=0;
        for(int i=0; s[i]; i++) if(s[i] != '0') { foundnonzero = i; break; }
        for(int i=foundnonzero; s[i]; i++) printf("%c", s[i]);
        printf("\n");
        break;
      }
    }
  }
  return 0;
}
