#include<stdlib.h>
#include<stdio.h>
struct HH {
   int K;
   int S;
};
int compare (const void * a, const void * b)
{
  return ( ((struct HH*)a)->K - ((struct HH*)b)->K );
}
int main()
{
   int T,D,N;
   struct HH hh[1000];
   float t[1000];
   scanf("%d",&T);
   for(int i = 1; i <=T; i++) {
      scanf("%d%d",&D,&N);
      for(int h = 0; h < N; h++)
         scanf("%d%d",&hh[h].K, &hh[h].S);
      qsort (hh, N, sizeof(struct HH), compare);
      int slowH = 0; int slowS = hh[0].S;
      for(int h = 0; h < N; h++) {
         if(hh[h].S < slowS) {
            slowH = h;
            slowS = hh[h].S;
         }
      }
      t[slowH] = static_cast<float>((D-hh[slowH].K))/static_cast<float>(slowS);
      for(int h = slowH-1; h >= 0; h--) {
         if( hh[h].S <= hh[h+1].S || ((hh[h+1].K-hh[h].K)/(hh[h].S-hh[h+1].S) >= t[h+1]) ) {
            t[h] = static_cast<float>((D-hh[h].K))/static_cast<float>(hh[h].S);
         }
         else {
            t[h] = t[h+1];
         }
      }
      double ans = static_cast<float>(D)/t[0];
      printf("Case #%d: %f\n",i,ans);
   }
   return 0;
}
