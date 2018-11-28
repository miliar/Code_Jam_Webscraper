#include <bits/stdc++.h>
#include <cstdio>

bool is_tidy(unsigned long long int number){
  int dig, last = 10;
  while(number){
    dig = number%10;
    if(dig > last) return false;
    last = dig;
    number = number/10;
  }
  return true;
}
 bool has_zero(unsigned long long int number){
   int dig;
   while(number){
     dig = number%10;
     if(dig == 0) return true;
     number = number/10;
   }
   return false;
 }

unsigned long long int next(unsigned long long int number){
  int digs = log10(number);
  unsigned long long int num = 0;
  unsigned long long int sum = 9;
  for(int i=0; i<digs; i++){
    num += sum;
    sum *= 10;
  }
  return num;
}

int main(){
  unsigned long long int T, N, cases = 1;

  scanf("%llu", &T);
  while(T--){
    scanf("%llu", &N);
    while(!is_tidy(N) && N > 0){
        N--;
    }
    printf("Case #%llu: %llu\n", cases++, N);
  }
  return 0;
}
