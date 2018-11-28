#include <stdio.h>

typedef unsigned long long ull;

int isTidy(ull n){
  int ant = n % 10;
  n /= 10;
//printf("primero eh %d, sobrou %llu\n", ant, n);
  while(n){
    if(n % 10 > ant) return 0;
    ant = n % 10;
    n /= 10;
//printf("agora ant eh %d e n %llu\n", ant, n);
  }
  return 1;
}

int main(void){
int t, x = 1;
  ull n;

  scanf("%d", &t);
  while(t--){
    scanf("%llu", &n);
    while(!isTidy(n)) n--;
    printf("Case #%d: %llu\n", x++, n);
  }

  return 0;
}
