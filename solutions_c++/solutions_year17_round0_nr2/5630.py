#include <cstdio>
#include <iostream>
using namespace std;

long long int tidy = -1;

bool is_tidy(long long int x) {
  if(x < 0) {
   return false;
  }

  long long int last = x % 10;
  x = x / 10;
  while(last >= (x % 10) && x > 0) {
    x = x / 10;
    last = x%10;
  }

  return (x == 0);
}

void tidy_number(long long int r, long long int x) {
  if (r < 0) {
    return;
  }

  if (!is_tidy(r)) {
    return;
  }
  
  if (r > x) {
    return;
  }

  tidy = max(tidy, r);

  long long d = r % 10;
  
  for(long long int i = d; i <= 9; i++) {
    tidy_number(i + r * 10L, x);
  }
  return;
}
int main() {
 int T;
 scanf("%d", &T);
 int cases = 0;
 while(T > 0) {
   T--;
   cases++;
   tidy = -1;
   long long int x;
   cin >> x;
   for(long long int i = 1; i <= (x >= 9 ? 9: x); i++) {
     tidy_number(i, x);
   }
   printf("Case #%d: %lld\n", cases, tidy);
 }
}
