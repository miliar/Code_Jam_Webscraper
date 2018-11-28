#include <cstdio>
#include <algorithm>

using namespace std;

char s[50];

inline void solve () {
  scanf ("%s", s + 1);
  s[0] = '0';

  int i;
  for (i = 1;s[i] != 0;i ++) {
    if (s[i] < s[i - 1]) {
      break;
    }
  }
  if (s[i] != 0) {
    for (i = i - 1;i >= 1;i --) {
      if (s[i] > s[i - 1]) {
        break;
      }
    }
    s[i] --;
  }

  int j;
  for (j = 1;s[j] != 0 and j <= i;j ++) {
    if (s[j] != '0') {
      break;
    }
  }
  for (;s[j] != 0 and j <= i;j ++) {
    printf ("%c", s[j]);
  }
  for (;s[j] != 0;j ++) {
    printf ("9");
  }
  printf ("\n");
}

int main () {
  int t;
  scanf ("%d", &t);

  for (int i = 1;i <= t;i ++) {
    printf ("Case #%d: ", i);
    solve ();
  }
}
