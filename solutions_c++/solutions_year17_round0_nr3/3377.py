#include <cstdio>
#include <cstring>
#include <queue>
#include <utility>
#define MAX 1000001
inline int max(int a, int b) { return (a > b) ? a : b; }
inline int min(int a, int b) { return (a < b) ? a : b; }
int n, k;
char s[MAX];
using namespace std;
typedef pair<int,int> ipair;
void occupy(int l, int r, int k) {
  //printf("%s\n", s);
  //getchar();
  if (!k) return;
  int i = (l + r)/2;
  s[i] = '0';
  --k;
  if ((l + r)%2) {
    occupy(i + 1, r, k/2 + k%2);
    occupy(l, i -1, k/2);
  } else {
    occupy(l, i -1, k/2);
    occupy(i + 1, r, k/2 + k%2);
  }
}
int main() {
  int t;
  scanf("%d", &t);
  for (int c = 1; c <= t; ++c) {
    memset(s, '.', MAX*sizeof(char));
    scanf("%d %d", &n, &k);
    s[n] = '\0';
    occupy(0, n - 1, k - 1);
    int max_left = 0;
    //printf("FINAL: 0%s0\n", s);
    for (int i = 0; i < n; ++i) {
      int left_count = 0;
      while (s[i++] == '.')
        ++left_count;
      --i;
      if (left_count > max_left) max_left = left_count - 1;
    }
    int res = max_left/2;
    printf("Case #%d: %d %d\n", c, res + max_left%2, res);
    //printf("0%s0\n", s);
  }
  return 0;
}
