#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
#define all(x) (x).begin(), (x).end()

void read();
void kill();

const int M = 1010;

int n, c, m;
int cnt[M];
int a[M];

void read() {
  cin >> n >> c >> m;
  fill(cnt, cnt + c, 0);
  fill(a, a + n, 0);

  for (int i = 0; i < m; ++i) {
    int p, b;
    cin >> p >> b;
    --p;
    --b;
    cnt[b]++;
    a[p]++;
  }
}

int fun(int t) {
  int cur = 0;
  int ans = 0;
  for (int i = n - 1; i >= 0; --i) {
    int nw = a[i];
    int diff = nw - t;
    if (diff > 0) {
      ans += diff;
    }
    cur += diff;
    cur = max(cur, 0);
  }

  if (cur)
    return -1;
  return ans;
}

void kill() {
  int l = *max_element(cnt, cnt + c);
  int r = 1010;

  while (l < r) {
    int m = (l + r) / 2;
    if (fun(m) != -1)
      r = m;
    else 
      l = m + 1;
  }
  cout << l << " " << fun(l) << "\n";
}

int main() {
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cout << "Case #" << i << ": ";
    read();
    kill();
    cerr << "Case #" << i << " done.\n";
  }
  return 0;
}
