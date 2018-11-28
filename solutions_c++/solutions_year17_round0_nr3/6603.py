#include <cstdio>
#include <cassert>
#include <set>
#include <cstring>

int len2interval(int x) {
  return -x;
}

//... -> .O. 3 -> 1,1
//.... -> .O.. 4 -> 1,2

int i2i1(int xx) { // interval to #1 interval
  int x = -xx;
  if (x%2 == 0) return -(x/2);
  return -(x/2);
}

int i2i2(int xx) { // interval to #1 interval
  int x = -xx;
  if (x%2 == 0) return -(x/2-1);
  return -(x/2);
}

int main() {
//  for (int i = 0; i < 1000; i++) assert(-i2i1(-i)-i2i2(-i) == i-1);
  int T;
  scanf("%d", &T);
  for (int TT = 0; TT < T; TT++) {
    std::multiset<int> s; // -len
    int N, K;
    scanf("%d%d", &N, &K);
    s.insert(-N);
    for (int i = 1; i < K; i++) {
      int x = *(s.begin());
      int a = i2i1(x);
      int b = i2i2(x);
      s.erase(s.begin());
      if (a)
        s.insert(a);
      if (b)
        s.insert(b);
//      printf("%d -> %d %d\n", -x, -a, -b);
    }
      int x = *(s.begin());
      int a = i2i1(x);
      int b = i2i2(x);
    printf("Case #%d: %d %d\n", TT+1, -a, -b);
  }
  return 0;
}
