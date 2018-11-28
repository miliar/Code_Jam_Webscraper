#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>

bool IsTidy(const long long num) {
  int n_digits = 0;
  long long tmp = num;
  while (tmp) {
    n_digits++;
    tmp /= 10;
  }

  int min_digit = num % 10;  
  tmp = num;
  for (int i = 0; i < n_digits; i++) {
    if (min_digit < (tmp % 10)) {
      return false;
    }
    else {
      min_digit = tmp % 10;
    }
    tmp /= 10;
  }
  return true;
}

long long Solve(const long long &num) {
  int n_digits = 0;
  long long tmp = num;
  while (tmp) {
    n_digits++;
    tmp /= 10;
  }
  
  long long res = num;
  long long base = 1;
  for (int i = 0; i < n_digits; i++) {
    if (IsTidy(res)) {
      return res;
    } else {
      res -= (base * (((res / base) % 10) + 1));
    }
    base *= 10;
  }
  return res;
}

int main() {
  int n_cases;
  scanf("%d\n", &n_cases);
  for (int i = 0; i < n_cases; i++) {
    long long num;
    scanf("%lld", &num);
    long long res = Solve(num);
    printf("Case #%d: %lld\n", i + 1, res);
  }
  return 0;
}