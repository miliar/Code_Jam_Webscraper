#include<stdio.h>

void solve(int t) {
  char cols[7] = "ROYGBV";
  int N, colors[6];
  scanf("%d",&N);
  for(int i=0;i<6;i++) scanf("%d",colors+i);
  printf("Case #%d: ",t);
  int mx=0,mxi;

  for(int i=0;i<6;i+=2) {
    if(colors[i]*2 == N && 2*colors[(i+3)%6] == N) {
      while(colors[(i+3)%6]-->0) printf("%c%c",cols[(i+3)%6],cols[i]);
      printf("\n");
      return;
    }
  }
  
  for(int i=0;i<6;i+=2) {
    colors[i] -= colors[(i+3)%6]>0;
    if(colors[i]<colors[(i+3)%6]) {
      printf("IMPOSSIBLE\n");
      return;
    }
    if(mx < colors[i]) {
      mxi = i;
      mx = colors[i];
    }
  }
  if(mx > colors[(mxi+2)%6]+colors[(mxi+4)%6]) {
    printf("IMPOSSIBLE\n");
    return;
  }
  for(int l=0;l<mx;l++) {
    for(int ii=0;ii<6;ii+=2) {
      int i = (mxi+ii)%6;
      if(ii == 2 && l >= colors[i]) continue;
      if(ii == 4 && l < mx-colors[i]) continue;
      printf("%c",cols[i]);
      //while(colors[(i+3)%6]-->0) printf("%c%c",cols[(i+3)%6],cols[i]);
    }
  }
  printf("\n");
}

int main() {
  int t,T;
  scanf("%d",&T);
  for(t=1;t<=T;t++) solve(t);
  return 0;
}
