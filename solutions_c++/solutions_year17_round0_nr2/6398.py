#include<bits/stdc++.h>
using namespace std;
char str[50];

int main() {
  int t,len;
  freopen("out.txt","w",stdout);
  scanf("%d",&t);
  for (int i = 1; i <= t; ++i) {
    printf("Case #%d: ",i);
    scanf("%s",str);
    len = strlen(str);
    for (int i = len - 1; i > 0; --i) {
      if (str[i] < str[i - 1]) {
        str[i] = '9';
        str[i - 1]--;
      }
      else if (str[i] == '0') str[i] = '9';
    }
    int j = 0;
    while (str[j] == '0') j++;
    for (int i = j; i < len; ++i) {
      str[i] = str[i] < str[i - 1] ? str[i - 1] : str[i];
      printf("%c",str[i]);
    }
    printf("\n");
  }
}
