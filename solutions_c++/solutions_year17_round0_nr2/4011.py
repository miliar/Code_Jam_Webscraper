#include<cstdio>
#include<cstring>

int main() {
  int ncases;
  scanf("%d", &ncases);
  for (int ncase = 0; ncase < ncases; ncase++) {
    char s[25];
    scanf("%s", s);
    int n = strlen(s);
    int apos = n+1, ppos = -1;
    //printf("read %s\n",s);
    for (int i = 0; i < n-1; i++) {
      if (s[i] < s[i+1])
        ppos = i;
      if (s[i] > s[i+1]) {
        //printf("invert at %d ppos is %d digits are %c > %c\n", i, ppos, s[i], s[i+1]);
        apos = ppos;
        break;
      }
    }
    printf("Case #%d: ", ncase+1);
    for (int i = 0; i < n; i++) {
      if (i > apos+1) {
        putchar('9');
        continue;
      }
      if (i == apos+1) {
        char c = s[i] - 1;
        if (c != '0')
          putchar(c);
        continue;
      }
      putchar(s[i]);
    }
    printf("\n");
  }
  return 0;
}

