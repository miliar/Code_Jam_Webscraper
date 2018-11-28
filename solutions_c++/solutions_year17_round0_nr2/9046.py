#include <cstdio>
#include <string>
#include <string.h>

using namespace std;

bool is_tidy(unsigned long long n, unsigned long long digit) {
  if (n == 0) {
    return true;
  }
  if (n%10 > digit) {
    return false;
  }
  return is_tidy(n/10, n%10);
}
bool is_tidy(unsigned long long n) {
  return is_tidy(n/10, n%10);
}

int main() {
  int t;
  scanf("%d", &t);

  for (int i=0; i<t; i++) {
    unsigned long long n;
    scanf("%llu", &n);
    for (unsigned long long j=n; j>0; j--) {
      if (is_tidy(j)) {
        printf("Case #%d: %llu\n", i+1, j);
        break;
      }
    }
  }
}
