#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

#define MAXN 1500
int dp[MAXN][MAXN][2][2];
int cannot[2][MAXN];
int seen[MAXN][MAXN][2][2];

const int oo = 10000000;

int f(int time, int m, int who, int s) {
  const int tot_day = 1440;
  if (time >= tot_day) {
    if (m == tot_day/2 && who == s) {
      return 0;
    } else {
      return oo;
    }
  }
  
  if (cannot[who][time]) {
    return oo;
  }
  
  if (seen[time][m][who][s]) {
    return dp[time][m][who][s];
  }
  
  seen[time][m][who][s] = 1;
  
  int best = oo;
  if (who) {
    best = min(f(time+1, m, 1, s), f(time+1, m, 0, s) + 1);
  } else {
    best = min(f(time+1, m+1, 0, s), f(time+1, m+1, 1, s) + 1);
  }
  
  dp[time][m][who][s] = best;
  
  return best;
}

int main(void) {
  int T;
  scanf("%i", &T);
  
  for (int t = 1; t <= T; t++) {
    int a[2];
    scanf("%i %i", &a[0], &a[1]);
    
    memset(cannot, 0, sizeof(cannot));
    for (int j = 0; j < 2; j++) {
      for (int i = 0; i < a[j]; i++) {
        int l, r; scanf("%i %i", &l, &r);
        while (l < r) {
          cannot[j][l++] = 1;
        }
      }
    }
    
    memset(seen, 0, sizeof(seen));
    
    int c0 = f(0, 0, 0, 0);
    int c1 = f(0, 0, 1, 1);
    printf("Case #%i: %i\n", t, min(c0, c1));
  }
  
  return 0;
}