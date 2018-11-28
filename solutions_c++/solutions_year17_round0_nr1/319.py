#include <bits/stdc++.h>
using namespace std;
int t,tt,n,m,i,j,r,a[1010];
char s[1010];
int main() {
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%s",s);
    n=strlen(s);
    for (i=0; i<n; i++) a[i]=int(s[i]=='-');
    scanf("%d",&m);
    for (r=i=0; i+m<=n; i++) if (a[i]) {
      for (j=0; j<m; j++) a[i+j]^=1;
      r++;
    }
    for (i=0; i<n; i++) if (a[i]) break;
    printf("Case #%d: ",t);
    if (i<n) puts("IMPOSSIBLE"); else printf("%d\n",r);
  }
  return 0;
}

