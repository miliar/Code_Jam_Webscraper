#include<stdio.h>
#include<cstring>


void cal(char s[], int k, int c) {
  int len = strlen(s);
  int count = 0;
  for(int i = 0 ; i < len-k+1 ; i++) {
      if(s[i] == '-') {
          int j = i + k-1;
          if(j < len) {
              //int check = 0;
              //while(j+1 < len) {
                //if(s[j+1] == '+') check = 1;
                //else if(s[j+1] == '-' && check == 1) break;
                //if(s[j+1] == '+') break;
                //j++;
              //}
              count++;
              for(int k = i ; k <= j ; k++) {
                  if(s[k] == '+') s[k] = '-';
                  else s[k] = '+';
              }
          }
      }
  }
      for(int i = len-k+1; i < len ; i++) {
          if(s[i] == '-') {
            printf("Case #%d: IMPOSSIBLE\n", c);
            return ;
          }
      }
      printf("Case #%d: %d\n", c, count);
}

int main() {
  int n, k;
  char s[100000];
  scanf("%d", &n);
  for(int i = 0 ; i < n ; i++) {
    scanf("%s %d", s, &k);
    cal(s, k, i+1);
  }
}