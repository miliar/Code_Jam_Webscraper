#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int n;
char s[20];

int main(void) {
  int tt;
  scanf("%d", &tt);
  for (int id = 1; id <= tt; ++id) {
    scanf("%s", s);
    n = strlen(s);
    int begin = 0;
    for (int i = 1; i < n; ++i) {
      if (s[i] > s[i - 1]) {
        begin = i;
      }
      if (s[i] < s[i - 1]) {
        --s[begin];
        for (int j = begin + 1; j < n; ++j) {
          s[j] = '9';
        }
      }
    }
    long long ans = 0;
    for (int i = 0; i < n; ++i) {
      ans = 10 * ans + s[i] - '0';
    }
    printf("Case #%d: %I64d\n", id, ans);
  }
  return 0;
}
