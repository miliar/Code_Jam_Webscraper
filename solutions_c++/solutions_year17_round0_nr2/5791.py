#include <iostream>
#include <string>
#include <cstdio>
using namespace std;


int peeps[1001];

void solve(int CASE) {
  string n;

  cin >> n;

  n = string(n.rbegin(), n.rend());

  int x = -1;
  for (int i = 0; i + 1 < n.size(); i++) {
    if (n[i] < n[i+1]) {
      n[x = i] = 'x';

      if (n[i+1] != '0') n[i+1]--;
    }
  }

  for (int i = 0; i <= x; i++) n[i] = '9';

  x = 0;
  for (int i = 0; i < n.size(); i++) if (n[i] != '0') x = i;

  n.resize(x+1);
  n = string(n.rbegin(), n.rend());

  printf("Case #%d: %s\n", CASE, n.c_str());
}

int main() {
  int T;

  cin >> T;

  for (int i = 1; i <= T; i++) {
    solve(i);
  }

  return 0;
}
