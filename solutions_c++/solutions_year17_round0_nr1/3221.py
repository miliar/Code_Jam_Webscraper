#include <cstdio>

char flip[256];

int main() {
  int t; scanf("%d", &t);
  char s[1005];
  flip['-'] = '+';
  flip['+'] = '-';
  int k;
  for(int _i=1; _i<=t; _i++) {
    printf("Case #%d: ", _i);
    scanf(" %s %d", s, &k);
    int len=0;
    for(; s[len]!='\0'; len++);
    int flipped = 0;
    for(int i=0; i<=len-k; i++) {
      if(s[i] == '-') {
        flipped++;
        for(int j=0; j<k; j++) {
          s[i+j] = flip[s[i+j]];
        }
      }
    }
    bool happy = true;
    for(int i=0; i<len; i++) {
      if(s[i] == '-') happy = false;
    }
    if(happy) printf("%d\n", flipped);
    else printf("IMPOSSIBLE\n");
  }
}
