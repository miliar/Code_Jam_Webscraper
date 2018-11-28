#include <bits/stdc++.h>
using namespace std;
int t,tt,n,m,x,s,i,r,c,a[5];
int main() {
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%d%d",&n,&m);
    for (i=0; i<m; i++) a[i]=0;
    for (s=i=0; i<n; i++) {
      scanf("%d",&x);
      a[x%m]++;
      s+=x;
    }
    r=a[0]+int(s%m!=0);
    if (m>2) {
      c=min(a[1],a[m-1]);
      r+=c;
      a[1]-=c;
      a[m-1]-=c;
    }
    if (m%2==0) {
      c=a[m/2]/2;
      a[m/2]-=c*2;
      r+=c;
    }
    if (m==3) {
      r+=(a[1]+a[2])/3;
    } else if (m==4) {
      if (a[2]==1 && a[1]>1) { r++; a[2]--; a[1]-=2; }
      if (a[2]==1 && a[3]>1) { r++; a[2]--; a[3]-=2; }
      r+=(a[1]+a[3])/4;
    }
    printf("Case #%d: %d\n",t,r);
  }
  return 0;
}

