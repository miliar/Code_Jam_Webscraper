#include<iostream>
#include<math.h>

using namespace std;


int T;
long long N;

int digits(long long n) { int res = 1;

  while(n /= 10) {
    res += 1;
  }

  return res;
}

long long findAns(long long n) {
  bool found = false;
  int ds;
  int right;
  int left;
  long long tmpN;

  while(!found) {
    found = true;

    ds = digits(n);
    tmpN = n;

    for(int i = 0; i < ds - 1; i++) {
      right = tmpN % 10;
      left = (tmpN / 10) % 10;
    
      if(left > right) {
        n -= 1;
        found = false;
        break;
      }
      else {
        tmpN /= 10;
      }
    }
  }

  return n;
}

int main() {
  FILE *in = fopen("B-small-attempt0.in", "r");
  FILE *out = fopen("B-small.out", "w");
  //scanf("%d", &T);
  fscanf(in, "%d", &T);

  for(int i = 0; i < T; i++) {
    //scanf("%llu", &N);
    fscanf(in, "%llu", &N);

    printf("digits: %d\n", digits(N));

    long long ans = findAns(N);

    //printf("Case #%d: %llu\n", i + 1, ans);
    fprintf(out, "Case #%d: %llu\n", i + 1, ans);
  }
}
