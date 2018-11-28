#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>
#include <numeric>

using namespace std;

int main(void) {
  int T;
  scanf("%i", &T);
  
  for (int t = 1; t <= T; t++) {
    int n;
    scanf("%i", &n);
    
    pair<int,char> s[10];
    
    string colors = "ROYGBV";
    for (int i = 0, j = 0; i < 6; i++) {
      int a; scanf("%i", &a);
      if (i % 2 == 0) {
        s[j++] = make_pair(a, colors[i]);
      }
    }
    
    sort(s, s+3);
    
    int a[3]; char c[3];
    for (int i = 0; i < 3; i++) {
      a[i] = s[i].first;
      c[i] = s[i].second;
    }
    
    printf("Case #%i: ", t);
    if (a[2] - a[1] > a[0]) {
      puts("IMPOSSIBLE");
      continue;
    }
    
    while (accumulate(a, a+3, 0) > 0) {
      if (a[0] > 0) {
        if (a[1] < a[2]) {
          putchar(c[2]);
          putchar(c[0]);
          putchar(c[2]);
          putchar(c[1]);
          a[2]--;
        } else {
          putchar(c[2]);
          putchar(c[0]);
          putchar(c[1]);
        }
        a[0]--, a[1]--, a[2]--;
      } else {
        putchar(c[2]);
        putchar(c[1]);
        a[1]--, a[2]--;
      }
    }
    puts("");
  }
  
  return 0;
}