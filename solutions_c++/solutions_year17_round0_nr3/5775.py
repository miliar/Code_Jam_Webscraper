#include <iostream>
#include <utility>
#include <algorithm>

using namespace std;
typedef long long LL;
#define mp make_pair

int arr[1005], ls[1005], rs[1005], minval[1005], maxval[1005];
pair<int, pair<int, pair<int, int> > > item;

int t;
LL k, n;
int main() {
  cin >> t;
  for (int tc = 1; tc <= t; tc++) {
    cin >> n >> k;

    memset(arr, 0, sizeof(arr));
    arr[0] = arr[n+1] = 1;

    int y, z;
    while (k--) {
      int last = 0;
      memset(ls, 0, sizeof(ls));
      memset(rs, 0, sizeof(rs));
      for (int i = 1; i <= n; i++) {
        ls[i] = i - last;
        if (arr[i]) last = i;
      }
      last = n + 1;
      item = make_pair(0, make_pair(0, make_pair(0, 0)));
      for (int i = n; i >= 1; i--) {
        rs[i] = last - i;
        if (arr[i]) last = i;

        minval[i] = min(ls[i], rs[i]);

        int a = min(ls[i], rs[i]);
        int b = max(ls[i], rs[i]);
        int c = -i;
        if (!arr[i]) item = max(item, mp(a, mp(b, mp(c, i))));
      }
      int index = item.second.second.second;
      arr[index] = 1;

      y = item.second.first;
      z = item.first;
    }

    printf("Case #%d: %d %d\n", tc, y - 1, z - 1);
  }
  return 0;
}
