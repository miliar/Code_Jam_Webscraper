#include <stdio.h>

using namespace std;

int f(int i){
  int r = 10;
  while(i > 9 && i%10 <= r){
    r = i%10;
    i/=10;
  }

  return i<=r?1:0;
}

int main(){
  int euc[1001];
  euc[0] = 0;
  for(int i=1;i<1001;i++){
    euc[i] = f(i)?i:euc[i-1];
  }
  
  int T, t = 0, input;
  scanf("%d", &T);
  while(t < T){
    scanf("%d", &input);
    printf("Case #%d: %d\n", ++t, euc[input]);
  }
  return 0;
}
