#include <cstdio>
#include <cstring>
using namespace std;

const int maxN = 1000 + 7;
int T, k;
char str[maxN];
bool mark[maxN];

int solve() {
  int flipped, ans, len = strlen(str);
  flipped = ans = 0;

  for (int i = 0; i <= len - k; i ++) { 
    if (i >= k && mark[i - k]) flipped ^= 1;
    if (flipped ^ (str[i] == '-' ? 1 : 0)) {
      mark[i] = true;
      flipped ^= 1;
      ans ++;
    } else {
      mark[i] = false;
    }
  }

  for (int i = len - k + 1; i < len; i ++) {
    if (i >= k && mark[i - k]) flipped ^= 1;
    if (flipped ^ (str[i] == '-' ? 1 : 0)) return -1;
  }

  return ans;
}

int main()
{
  scanf("%d", &T);
  for (int cou = 1; cou <= T; cou ++) {
    scanf("%s%d", str, &k);
    printf("Case #%d: ", cou);
    int times = solve();
    if (times < 0) {
      printf("IMPOSSIBLE\n");
    } else {
      printf("%d\n", times);
    }
  }
}
