#include <bits/stdc++.h> 

using namespace std;

const int N = 30;

char s[N];
int t, cs = 0, n;

int main (int argc, char const *argv[]) {
  scanf("%d", &t); while (t--) {
    scanf("%s", s + 1);
    n = strlen(s + 1);
    for (int i = 1; i < n; ++i) {
      if (s[i] > s[i + 1]) {
        int j = i;
        while (j > 1 and s[j] == s[j - 1]) --j;
        s[j++]--;
        while (j <= n) s[j++] = '9';
        break;
      }
    }
    int at = 1;
    while (s[at] == '0') ++at;
    printf("Case #%d: ", ++cs);
    puts(s + at);
  }
  return 0;
}

