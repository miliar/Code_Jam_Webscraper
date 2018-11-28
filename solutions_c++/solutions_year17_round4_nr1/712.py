#include <cstdio>
#include <algorithm>
using namespace std;

const int MAXN = 107;

int T, n, p, g, num[MAXN];

int solve() {
  if (p == 2) return num[0] + (num[1] + 1) / 2;
  if (p == 3) {
    int t = min(num[1], num[2]);
    return num[0] + t + (num[1] + num[2] - 2 * t + 2) / 3; 
  }
  // p = 4

  return num[0];
}

int main()
{
   scanf("%d", &T);
   for (int cou = 1; cou <= T; cou ++) {
     scanf("%d%d", &n, &p);
     for (int i = 0; i < p; i ++) num[i] = 0;
     for (int i = 0; i < n; i ++) scanf("%d", &g), num[g % p] ++;
     printf("Case #%d: %d\n", cou, solve()); 
   }
}
