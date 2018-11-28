#include<bits/stdc++.h>
using namespace std;

int g[102];

int Main() {
  int n, p;
  scanf("%d %d", &n, &p);
  
  int modulo[p];
  for (int i=0; i<p; i++) modulo[i] = 0;
  
  int s = 0;
  for (int i=0; i<n; i++) {
    scanf("%d", g + i);
    ++modulo[g[i] % p];
    s += g[i];
  }
  
  int tmp = (s % p > 0);
  if (p == 2) {
    return 0 * printf("%d\n", modulo[0] + modulo[1] / 2 + tmp);
  }
  
  if (p == 3) {
    int mini = min(modulo[1], modulo[2]);
    int maks = max(modulo[1], modulo[2]);
    return 0 * printf("%d\n", modulo[0] + mini + (maks-mini) / 3 + tmp);
  }
  
  if (p == 4) {
    int mini = min(modulo[1], modulo[3]);
    int maks = max(modulo[1], modulo[3]);
    int diff = maks - mini;
    
    int tot = 0;
    tot += modulo[0];
    tot += modulo[2] / 2;
    tot += mini;
    if ((modulo[2] & 1) && (diff >= 2)) {
      diff -= 2;
      tot++;
    }
    tot += diff / 4;
    
    return 0 * printf("%d\n", tot + tmp);
  }
}


int main() {
  int t;
  scanf("%d", &t);
  for (int tc=0; tc<t; ++tc){ 
    printf("Case #%d: ", tc+1);
    Main();
  }

  return 0;
}