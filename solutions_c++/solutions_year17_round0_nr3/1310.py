#include <stdio.h>
#include <queue>

struct Data {
  long long num, val;
};

long long f(long long n, long long k) {
  std::queue<Data> que;
  que.push((Data){n, 1});
  while (1) {
    long long num = que.front().num;
    long long val = que.front().val;
    que.pop();
    if (!que.empty() && que.front().num == num) {
      val += que.front().val;
      que.pop();
    }
    if (k <= val) return num;
    k -= val;
    if (num <= 1) continue;
    if (num & 1) {
      que.push((Data){num/2, val * 2});
    } else {
      que.push((Data){num/2, val});
      que.push((Data){num/2-1, val});
    }
  }
}

int main() {
  int T;
  long long n, k;
  scanf("%d", &T);
  for (int t = 1; t <= T; ++t) {
    scanf("%lld%lld", &n, &k);
    long long ans = f(n, k);
    printf("Case #%d: %lld %lld\n", t, ans/2, (ans-1)/2);
  }
  return 0;
}
