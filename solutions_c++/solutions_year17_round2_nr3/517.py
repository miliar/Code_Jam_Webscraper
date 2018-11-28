#include<stdio.h>

int MaxDist[1000];
int Speed[1000];
double D[200][200];
void solve(int t) {
  int N, Q;
  scanf("%d %d",&N,&Q);
  for(int i=0;i<N;i++) scanf("%d %d",MaxDist+i,Speed+i);
  
  for(int i=0;i<N;i++) 
  for(int j=0;j<N;j++) {
    scanf("%lf",&(D[i][j]));
    D[i][i] = 0;
  }
  
  for(int k=0;k<N;k++) 
  for(int i=0;i<N;i++) 
  for(int j=0;j<N;j++) {
    if(D[i][k]<0 || D[k][j]<0) continue;
    if(D[i][j]<0 || D[i][j] > D[i][k]+D[k][j]) D[i][j] = D[i][k] + D[k][j];
  }
  
  for(int i=0;i<N;i++) 
  for(int j=0;j<N;j++) {
    if(D[i][j]<0 || D[i][j] > MaxDist[i]) D[i][j] = -1;
    else D[i][j] /= Speed[i];
  }
  
  for(int k=0;k<N;k++) 
  for(int i=0;i<N;i++) 
  for(int j=0;j<N;j++) {
    if(D[i][k]<0 || D[k][j]<0) continue;
    if(D[i][j]<0 || D[i][j] > D[i][k]+D[k][j]) D[i][j] = D[i][k] + D[k][j];
  }
  
  
  printf("Case #%d:",t);
  for(int q=0;q<Q;q++) {
    int i,j;
    scanf("%d %d",&i,&j);
    i--;j--;
    printf(" %.6lf",D[i][j]);
  }
  printf("\n");
}

int main() {
  int t,T;
  scanf("%d",&T);
  for(t=1;t<=T;t++) solve(t);
  return 0;
}
