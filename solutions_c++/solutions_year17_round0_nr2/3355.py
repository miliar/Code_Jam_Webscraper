#include <cstdio>
#include <cmath>
#include <cstring>
using namespace std;
#define MAXL 20

long long int solve(long long int);

int main() {
  int t;
  long long int in;

  scanf("%d", &t);
  for (int c = 1; c <= t; ++c) {
    scanf("%lld", &in);
    printf("Case #%d: %lld\n", c, solve(in));
  }
  return 0;
}

long long int solve(long long int in) {
  char str[MAXL];
  int digit;
  long long int p, q;
  sprintf(str, "%lld", in);
  digit = strlen(str);
  if (digit > 1) {
    for (int i = 2; i <= digit; ++i) {
      if (str[digit - i] > str[digit - i + 1]) {
        p = (long long int) in;
        q = (long long int) pow(10, i - 1);
        in = p - (p % q + 1);
      }
      sprintf(str, "%lld", in);
    }
  }
  return in;
}
