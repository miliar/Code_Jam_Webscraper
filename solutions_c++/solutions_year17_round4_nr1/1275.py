#include <cstdio>
#include <algorithm>
using namespace std;

const int maxn = 128;
int num[maxn];
int chocolate[maxn];

int main() {
  int tests;
  int n, p;
  scanf(" %d", &tests);
  for(int test_number=1; test_number<=tests; ++test_number) {
    printf("Case #%d:", test_number);
    scanf(" %d %d", &n, &p);
    for(int i=0; i<p; ++i)
      num[i]=0;
    for(int i=0; i<n; ++i) {
      scanf(" %d", &chocolate[i]);
      num[chocolate[i]%p]++;
    }
    if (p==2) {
      printf(" %d\n", n - num[1]/2);
    }
    else if (p==3) {
      int matches = min(num[1], num[2]);
      num[1]-=matches;
      num[2]-=matches;
      int answer = matches;
      int remainder = num[1]+num[2];
      answer += remainder - (remainder+2)/3;
      printf(" %d\n", n - answer);
    }
    else if (p==4) {
      int matches = min(num[1], num[3]);
      num[1]-=matches;
      num[3]-=matches;
      int remainder = num[1]+num[3];
      int answer = matches;
      answer += num[2]/2;
      if (num[2]%2) {
	remainder -= 2;
	answer += 2;
      }
      answer += remainder - (remainder+3)/4;
      printf(" %d\n", n - answer);
    }
  }
  return 0;
}
