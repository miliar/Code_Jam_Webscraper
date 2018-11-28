#include <bits/stdc++.h>
using namespace std;

#define rep(i,a,b) for (int i = a; i < b; i ++)
#define per(i,a,b) for (int i = b-1; i >= a; i --)

long long a[20], b[20];

bool BbiggerA() {
  per(i, 0, 20)
    if (b[i] > a[i])
      return true;
    else if (b[i] < a[i])
      return false;
  return false;
}

int main() {
  freopen("B.in", "r", stdin);
  freopen("B.out", "w", stdout);
  long long T, n;
  cin >> T;
  rep(t, 1, T + 1) {
    cin >> n;
    memset(a, 0, sizeof(a));
    memset(b, 0, sizeof(b));
    int index = 0;
    while (n > 0) {
      a[index] = n % 10;
      n /= 10;
      index ++;
    }
    per(i, 0, 20) {
      b[i] = a[i];
      per(j, 0, i)
        b[j] = b[i];
      if (BbiggerA()) {
        b[i] --;
        per(j, 0, i)
          b[j] = 9;
        break;
      }
    }
    cout << "Case #" << t << ": ";
    int i;
    for (i = 19; i >= 0; i --)
      if (b[i] != 0)
        break;
    for (; i >= 0; i --)
      cout << b[i];
    cout << endl;
  }
  return 0;
}
