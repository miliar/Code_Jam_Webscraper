#include <cstdio>
#include <algorithm>

using namespace std;

int main(void) {
  int T;
  scanf("%i", &T);
  
  for (int t = 1; t <= T; t++) {
    int n, p;
    scanf("%i %i", &n, &p);
    
    int a[p];
    for (int i = 0; i < p; i++) {
      a[i] = 0;
    }
    
    for (int i = 0; i < n; i++) {
      int m; scanf("%i", &m);
      a[m%p]++;
    }
    
    int ans = a[0];
    if (p == 3) {
      ans += min(a[2], a[1]);
      ans += ((max(a[2], a[1]) - min(a[2], a[1])) + 2) / 3;
    } else if (p == 2) {
      ans += (a[1] + 1) / 2;
    } else {
      ans += min(a[3], a[1]);
      ans += a[2] / 2;
      
      int r = max(a[3], a[1]) - min(a[3], a[1]);
      if (a[2] % 2) {
        ans++;
        ans += (r + 1) / 4;  
      } else {
        ans += (r + 3) / 4;
      }
    }
    
    printf("Case #%i: %i\n", t, ans);
  }
  
  return 0;
}