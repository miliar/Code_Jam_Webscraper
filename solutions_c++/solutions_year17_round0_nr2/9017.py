#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#define forn(n) for(int i=0;i<n;i++)
typedef long long LL;
using namespace std;
LL get_tail_zero(LL N, int index) {
  for(int i=1;i<=index; i++) {
    N /= 10;
  }
  for(int i=1;i<=index; i++) {
    N *= 10;
  }
  return N;
}
int get_digit_len(LL N) {
  int len = 0;
  do {
    len++;
    N /= 10;
  } while(N);
  return len;
}
int get_digit (LL N, int index) {
  int result;
  for (int i =0 ;i < index; i++) {
    result = N % 10;
    N /= 10;
  }
  return result;
}
LL task(LL N) {
  int digit_len = get_digit_len(N);
  int last = get_digit(N, digit_len);
  for (int i=digit_len-1;i>0;i--){
    int current = get_digit(N, i);
//    cout << "current: " << current << ", last: " << last << ", i: " <<i <<endl;
    if (current < last) {
      LL result = get_tail_zero(N, i) - 1;
      return result;
      return 0;
    }
    last = current;
  }
  return N;
}
bool is_invalid(LL N) {
  int digit_len = get_digit_len(N);
  int last = get_digit(N, digit_len);
  for (int i=digit_len-1;i>0;i--){
    int current = get_digit(N, i);
    if (current < last) {
      return true;
    }
  }
  return false;
}
int solve(int case_num){
  LL N;
  cin >> N;
  N= task(N);
  while (is_invalid(N)) {
    N = task(N);
  }
  printf("Case #%d: %lld\n", case_num, N);
  return 0;
}

int main(){
  int T, i;
  scanf("%d", &T);
  getchar();
  for (i = 1; i<=T; ++i )
    solve(i);
  return 0;
}
