#include <iostream>
using namespace std;
int T, k;
string s;

void change(int i) {
  for (int j = 0; j < k; ++j) {
    if (s[i + j] == '-') s[i + j] = '+';
    else s[i + j] = '-';
  }
}

void doit() {
  int res = 0;
  for (int i = 0; i <= s.size() - k; ++i) {
    if (s[i] == '-') {
      change(i);
      ++res;
    }
  }
  for (int i = s.size() - k; i < s.size(); ++i) {
    if (s[i] == '-') {
      printf("IMPOSSIBLE\n");
      return;
    }
  }
  printf("%d\n", res);
}

int main() {
  scanf("%d", &T);
  for (int t = 1; t <= T; ++t) {
    cin >> s;
    scanf("%d", &k);
    printf("Case #%d: ", t);
    doit();
  }
  return 0;
}
