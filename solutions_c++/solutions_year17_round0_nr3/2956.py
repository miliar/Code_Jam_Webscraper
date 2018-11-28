#include <cstdio>

using namespace std;

long long n, k;
long long a, b;
long long acnt, bcnt;

int main() {
  int tc;
  scanf("%d", &tc);
  for(int kase = 1; kase <= tc; kase++) {
    scanf("%lld %lld", &n, &k);
    a = n;
    b = n - 1;
    acnt = 1;
    bcnt = 0;
    long long x = 1;
    while(((x << 1) - 1) < k) {
      if(a % 2) {
	a = b >> 1;
	b = a - 1;
	acnt = acnt * 2 + bcnt;
      } else {
	a = a >> 1;
	b = (b - 1) >> 1;
	bcnt = acnt + bcnt * 2;
      }
      x <<= 1;
    }
    long long r = k - (x - 1);
    long long ansa, ansb;
    if(r <= acnt) {
      ansa = a >> 1;
      ansb = a - ansa - 1;
    } else {
      ansa = b >> 1;
      ansb = b - ansa - 1;
    }
    printf("Case #%d: %lld %lld\n", kase, ansa, ansb);
  }
  return 0;
}
