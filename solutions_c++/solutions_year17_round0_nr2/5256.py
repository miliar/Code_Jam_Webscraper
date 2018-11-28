#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>
#define TESTING false

void doCase(long long n);

int main(){
  int T;
  scanf("%d", &T);

  long long s;
  for (int i = 1; i<=T; i++){
    scanf("%lld", &s);

    printf("Case #%d: ",i);
    doCase(s);
    if (i!=T) printf("\n");
  }
}

void doCase(long long n){
  std::vector<int> digits;

  while(n){
    digits.push_back(n%10);
    n/=10;
  }


  int min = digits[0];

  int ninePoint = 0;

  for (int i = 0; i<digits.size(); i++){
    if (TESTING) printf("\n %d %d\n",min,i);
    if (min<digits[i] && i!=0){
      ninePoint = i;
      --digits[i];
    }
    min = digits[i];
  }

  for (int i = 0; i<ninePoint; i++){
    digits[i] = 9;
  }

  std::reverse(digits.begin(), digits.end());

  bool nonZeroPrinted = false;
  for (int i:digits){
    if (i!=0 || nonZeroPrinted) printf("%d", i);

    if (i!=0) nonZeroPrinted = true;
  }

}
