#include <stdio.h>

int main(){
  int t;
  scanf("%d", &t);
  for(int tc=0; tc<t; tc++){
    long long n, k;
    scanf("%lld%lld", &n, &k);
    printf("Case #%d: ", tc+1);
    long long A = n, Acnt = 1, B = n-1, Bcnt = 0;
    while(1){
      A--, B--;
      if(Acnt >= k){
        printf("%lld %lld\n", A-A/2, A/2);
        break;
      }
      k -= Acnt;
      if(Bcnt >= k){
        printf("%lld %lld\n", B-B/2, B/2);
        break;
      }
      k -= Bcnt;
      long long newA = B/2+1, newB = B/2;
      long long newAcnt = 0, newBcnt = 0;
      if(A/2 == newA) newAcnt += Acnt;
      else newBcnt += Acnt;
      if(A-A/2 == newA) newAcnt += Acnt;
      else newBcnt += Acnt;
      if(B/2 == newA) newAcnt += Bcnt;
      else newBcnt += Bcnt;
      if(B-B/2 == newA) newAcnt += Bcnt;
      else newBcnt += Bcnt;
      A = newA, B = newB, Acnt = newAcnt, Bcnt = newBcnt;
    }
  }
  return 0;
}
