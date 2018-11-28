#include <bits/stdc++.h>
using namespace std;
int t,tt,n,i,j;
char s[22],last;
int main() {
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%s",s);
    n=strlen(s);
    last='9';
    for (i=n-1; i>=0; i--) {
      if (s[i]>last) {
        s[i]--;
        for (j=i+1; j<n; j++) s[j]='9';
      }
      last=s[i];
    }
    for (i=0; i<n-1; i++) if (s[i]!='0') break;
    printf("Case #%d: %s\n",t,s+i);
  }
  return 0;
}

