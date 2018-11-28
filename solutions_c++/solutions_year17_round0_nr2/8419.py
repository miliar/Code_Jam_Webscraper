#include <bits/stdc++.h>

using namespace std;

bool isTidy(int n) {
  int t = n / 10, prev = n % 10;
  while (t > 0) {
    if (t % 10 <= prev) {
      prev = t % 10;
      t /= 10;
    }
    else
      return false;
  } 
  return true;
}

int brute(int n) {
  for (int i = n;  i >= 1; i--) {
    if (isTidy(i)) return i;
  }
}


int main() {
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    freopen("b.err", "w", stderr);

    int T;
    cin >> T;
    for(int tnum = 1; tnum <= T; ++tnum) {
        int n;
        cin >> n;
        cout << "Case #" << tnum << ": " << brute(n) << endl;
    }
    return 0;
}
