#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;

bool confirm(int r, int n1, int n2) {
  return (10 * n1 >= 9 * r * n2) &&
    (10 * n1 <= 11 * n2 * r);
}

/*
int getCount(int n1, int n2) {
  int tmp = n1 / n2;
  for (int ret = tmp-1; ret <= tmp+1; ret++) {
    if (confirm(ret, n1, n2)) return ret;
  }
  return -1;
}
*/

int getCountMi(int n1, int n2) {
  int tmp = n1 / n2;
  int ret = -1;
  if (confirm(tmp+1, n1, n2)) ret = tmp+1;
  if (confirm(tmp, n1, n2)) ret = tmp;
  while (ret > 0 && confirm(ret-1, n1, n2)) ret--;
  return ret;
}

int getCountMa(int n1, int n2) {
  int tmp = n1 / n2;
  int ret = -1;
  if (confirm(tmp, n1, n2)) ret = tmp;
  if (confirm(tmp+1, n1, n2)) ret = tmp+1;
  while (ret >= 0 && confirm(ret+1, n1, n2)) ret++;
  return ret;
}

int main() {
  int cases;
  cin >> cases;
  for (int cas = 1; cas <= cases; cas++) {
    int ny, nx, r[55], a[55][55], ix[55];
    cin >> ny >> nx;
    for (int i = 0; i < ny; i++) {
      cin >> r[i];
    }
    for (int y = 0; y < ny; y++) {
      for (int x = 0; x < nx; x++) {
	cin >> a[y][x];
      }
    }
    for (int i = 0; i < ny; i++) {
      sort(a[i], a[i] + nx);
      ix[i] = 0;
    }
    int ans = 0;
    for (ix[0] = 0; ix[0] < nx; ix[0]++) {
      int mi = getCountMi(a[0][ix[0]], r[0]);
      int ma = getCountMa(a[0][ix[0]], r[0]);
      if (mi < 0) continue;
      //printf("%d %d\n", mi, ma);
      //printf("count %d\n", count);
      for (int count = mi; count <= ma; count++) {
	int y;
	for (y = 1; y < ny; y++) {
	  //int count2 = -1;
	  int mi2, ma2;
	  bool ok2 = false;
	  for (; ix[y] < nx; ix[y]++) {
	    mi2 = getCountMi(a[y][ix[y]], r[y]);
	    ma2 = getCountMa(a[y][ix[y]], r[y]);
	    if (mi2 > count) break; // too big already
	    if (count >= mi2 && count <= ma2) { // found
	      ok2 = true;
	      break;
	    }
	  }
	  if (!ok2) break;
	}
	if (y == ny) {
	  ans++;
	  for (int y = 1; y < ny; y++) {
	    ix[y]++;
	  }
	  break;
	}
      }
    }
    printf("Case #%d: %d\n", cas, ans);
  }
  return 0;
}
