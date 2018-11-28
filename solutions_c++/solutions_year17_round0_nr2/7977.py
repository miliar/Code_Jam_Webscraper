#include <stdio.h>
#include <iostream>

using std::swap;
using std::min;
using std::max;

#define LL long long

bool isTidy(LL x) {
  int d;
  int lastDigit = 9;
  while (x > 0) {
    d = x % 10;
    if (d <= lastDigit) {
      x /= 10;
      lastDigit = d;
    } else {
      return false;
    }
  }
  return true;
}

// inefficient method
LL maxTidy(LL bound) {
  while (!isTidy(bound)) {
    bound--;
  }
  return bound;
}

int digitCount(LL x) {
  int dc = 0;
  while (x > 0) {
    dc++;
    x /= 10;
  }
  return dc;
}

LL smartMaxTidy(LL bound) {
  if (bound < 100) {
    return maxTidy(bound);
  }
  if (isTidy(bound)) {
    return bound;
  }

  int dc = digitCount(bound);
  int *numArr = new int[dc];
  LL sum = 0;

  for (int i = 0; i < dc; i++) {
    numArr[dc-i-1] = bound % 10;
    bound /= 10;
  }

  int i = 0;
  while (i < dc-1) {
    if (numArr[i] <= numArr[i+1]) {
      i++;
    } else {
      break;
    }
  }

  while (i >= 0) {
    if (numArr[i] > numArr[i+1]) {
      numArr[i]--;
      i--;
    } else {
      break;
    }
  }

  for (int j = 0; j <= i+1; j++) {
    sum *= 10;
    sum += numArr[j];
  }
  for (int j = i+2; j < dc; j++) {
    sum *= 10;
    sum += 9;
  }

  return sum;
}

void test() {
  for (int i = 1; i < 50000; i++) {
    if (maxTidy(i) != smartMaxTidy(i)) {
      printf("Error: %d\n", i);
      break;
    }
  }
  printf("Prelim tests passed\n");
  while (true) {
    LL n;
    scanf("%lld", &n);
    printf("%lld\t%lld\n", maxTidy(n), smartMaxTidy(n));
  }
}

void thousand() {
  LL last = 0;
  LL ans;
  for (int i = 1; i <= 200; i++) {
    ans = maxTidy(i);
    if (ans == last) {
      printf("%d\n", i);
    } else {
      printf("%d\t\t\%lld\n", i, ans);
    }
    last = ans;
  }
}

int main() {
  // int T;
  // LL N;
  // scanf("%d", &T);
  // for (int i = 0; i < T; i++) {
  //   scanf("%lld", &N);
  //   printf("Case #%d: %lld\n", i+1, smartMaxTidy(N));
  // }
  // thousand();
  test();
}
