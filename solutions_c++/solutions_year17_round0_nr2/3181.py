#include <cstdio>

long long int pow10(int n) {
  long long int r = 1;
  while(n--) r*=10;
  return r;
}

int digit(long long int x, int n) {
  return x/pow10(n)%10;
}

bool valid(long long int x) {
  for(int i=0; i<18; i++) if(digit(x, i) < digit(x, i+1)) return false;
  return true;
}

long long int solve(long long int x) {
  for(int i=0; i<18; i++) {
    if(not valid(x % pow10(i+1))) {
      x -= (x % pow10(i)) + 1;
    }
  }
  return x;
}

long long int bforce(long long int x) {
  for(long long int i=x; i>=0; i--) {
    if(valid(i)) return i;
  }
}

int main() {
  int t; scanf("%d", &t);

  for(int _i=1; _i<=t; _i++) {
    printf("Case #%d: ", _i);
    long long int n; scanf("%lld", &n);

    printf("%lld\n", solve(n));
  }
}
