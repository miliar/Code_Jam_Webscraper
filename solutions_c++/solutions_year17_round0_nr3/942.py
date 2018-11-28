#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

bool a[1100000];

long long minval(long long x, long long y) {
  if (x == -1)  return y;
  if (y == -1)  return x;
  if (x < y)
    return x;
  else
    return y;
}

long long getans(long long n, long long k) {
  if (k == 1) return n - 1;
  if (k == 0) return -1;
  long long n_n = (n-1) / 2;
  long long n_k = k / 2;
  if (n % 2 == 0 && k % 2 == 0)
    return minval(getans(n_n, n_k - 1), getans(n_n + 1, n_k));
  else
    return getans(n_n, n_k);
}

int main() {
  freopen("input.txt", "r", stdin);
  freopen("answer.txt", "w", stdout);
  int T;
  long long n, k;
  cin >> T;
  for (int _ = 1; _ <= T; _ ++) {
    cin>>n>>k;
    // memset(a, 0, sizeof a);
    // a[0] = 1;
    // a[n + 1] = 1;
    long long maxleng;
    // for (int t = 0; t < k; t++) {
    //   maxleng = -1;
    //   int l_rec = 0, r_rec = 0 ;
    //   for (int i = 1; i <= n; i++) {
    //     if (a[i] == 0) {
    //       int j;
    //       for (j = i+1; a[j] == 0; j++);
    //       if (j - i - 1 > maxleng) {
    //         maxleng = j - i - 1;
    //         l_rec = i;
    //         r_rec = j - 1;
    //       }
    //       i = j;
    //     }
    //   }
    //   a[l_rec + maxleng / 2] = 1;
    //   // printf("!!!%d\n", maxleng);
    // }
    maxleng = getans(n,k);
    printf("Case #%d: %lld %lld\n", _, maxleng - (maxleng / 2), maxleng / 2);
  }
}
