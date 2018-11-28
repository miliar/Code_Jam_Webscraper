#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cstring>
#include <queue>
#include <utility>
using namespace std;
void solve() {
  uint64_t val;
  cin >> val;
  int digits[20];
  int N = 0;
  while (val) {
    digits[N] = val % 10;
    val /= 10;
    ++N;
  }
  int pivot = N-2;
  for (; pivot>=0; --pivot) {
    if (digits[pivot] < digits[pivot+1]) {
      break;
    }
  }
  if (pivot != -1) {
    digits[pivot+1]--;
    for (; pivot >= 0; --pivot) {
      digits[pivot] = 9;
    }
    for (int i = 0; i < N-1; ++i) {
      if (digits[i] < digits[i+1]) {
        digits[i+1]--;
        digits[i] = 9;
      }
    }
  }
  uint64_t ans = 0;
  for (int i = N-1; i>=0; --i) {
    ans *= 10;
    ans += digits[i];
  }
  printf(" %lld", ans);
}

int main(){
  int T;
  scanf("%d",&T);
  for (int TC=1;TC<=T;++TC) {
    printf("Case #%d:", TC);
    solve();
    printf("\n");
  }
  return 0;
}