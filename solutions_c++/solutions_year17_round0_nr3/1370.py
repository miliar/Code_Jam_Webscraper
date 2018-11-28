#include <stdio.h>

#include <algorithm>
#include <map>

#define llu long long unsigned

// n -> k -> place
std::map<llu, std::map<llu, llu> > cache;

llu place(llu n, llu k) {
  if (k == 0) {
    return n;
  }

  if (cache[n].find(k) == cache[n].end()) {
    // number of stalls left on either side
    llu low = (n - 1) / 2;
    llu high = n / 2;

    cache[n][k] = std::max(place(low, k ? (k - 1) / 2 : 0), place(high, k / 2));
  }

  return cache[n][k];
}

int main() {
  int T;
  scanf("%d", &T);

  for (int t = 1; t <= T; t++) {
    llu n, k;
    scanf("%llu%llu", &n, &k);

    llu most = place(n, k - 1);

    printf("Case #%d: %llu %llu\n", t, most / 2, (most - 1) / 2);
  }

  return 0;
}
