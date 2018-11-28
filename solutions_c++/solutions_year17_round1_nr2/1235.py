#include <cstdio>
#include <algorithm>

using namespace std;

int vals[2][8], s[2], n, p;
int mem[1000][1000];
int proc(int b1 = 0, int b2 = 0, int cnt = 0) {
  if(mem[b1][b2] != -1) return mem[b1][b2];
  int ans = cnt;
  for(int i = 0; i < p; ++i)
  if(!((b1>>i)&1) && ((vals[0][i]*10 + (s[0]*11-1))/(s[0]*11) <= (vals[0][i]*10)/(s[0]*9)))
  for(int j = 0; j < p; ++j)
    if(!((b2>>j)&1) && (vals[1][j]*10 + (s[1]*11-1))/(s[1]*11) <= (vals[1][j]*10)/(s[1]*9))
      if((vals[0][i]*10)/(s[0]*9) >= (vals[1][j]*10 + (s[1]*11-1))/(s[1]*11) && (vals[0][i]*10 + (s[0]*11-1))/(s[0]*11) <= (vals[1][j]*10)/(s[1]*9))
        ans = max(ans, proc(b1|(1<<i), b2|(1<<j), cnt+1));
  return mem[b1][b2] = ans;
}
int main() {
  int t;
  scanf("%d", &t);
  for(int cas = 1; cas <= t; ++cas) {
    scanf("%d %d", &n, &p);
    for(int i = 0; i < n; ++i) scanf("%d", s + i);
    for(int i = 0; i < n; ++i)
    for(int j = 0; j < p; ++j)
      scanf("%d", &vals[i][j]);
    if(n == 1) {
      int ans = 0;
      for(int i = 0; i < p; ++i)
        if((vals[0][i]*10 + (s[0]*11-1))/(s[0]*11) <= (vals[0][i]*10)/(s[0]*9))
          ++ans;
      printf("Case #%d: %d\n", cas, ans);
    } else {
      memset(mem, -1, sizeof mem);
      printf("Case #%d: %d\n", cas, proc());
    }
  }
  return 0;
}