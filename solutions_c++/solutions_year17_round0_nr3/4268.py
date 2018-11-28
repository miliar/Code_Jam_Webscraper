#include <bits/stdc++.h>

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int tests;
  scanf("%d", &tests);
  int test_number = 0;
  while (tests--) {
    printf("Case #%d: ", ++test_number);
    int n, k;
    scanf("%d%d", &n, &k);
    std::multiset<int, std::greater<int>> lens;
    lens.insert(n);
    for (int i = 0; i < k; i++) {
      int len = *lens.begin();
      lens.erase(lens.begin());
      lens.insert(std::max(0, (len - 1) / 2));
      lens.insert(std::max(0, len - (len - 1) / 2 - 1));
      if (i + 1 == k) {
        printf("%d %d\n", std::max(0, len - (len - 1) / 2 - 1), std::max(0, (len - 1) / 2));
      }
    }
  }
  return 0;
}
