#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

char N[200];
int len;

bool update() {
  bool change = false;
  for (int i = len - 2; i >= 0; --i) {
    if (N[i] < N[i + 1]) {
      change = true;
      for (int j = i + 1; j < len; ++j) {
        if (N[j] == '0') {
          N[j] = '9';
        } else {
          N[j]--;
          break;
        }
      }

      for (int j = 0; j <= i; ++j) {
        N[j] = '9';
      }

      break;
    }
  }

  while (N[len - 1] == '0') {
    N[--len] = '\0';
  }
  return change;
}

int main() {
  ios ::sync_with_stdio(0);
  int t;
  cin >> t;
  for (int cn = 1; cn <= t; cn++) {
    cin >> N;

    len = strlen(N);

    reverse(N, N + len);
    while (update())
      ;
    reverse(N, N + len);

    printf("Case #%d: %s\n", cn, N);
  }
  return 0;
}
