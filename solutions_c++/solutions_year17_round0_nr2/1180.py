#include<iostream>
#include<cstdio>
using namespace std;

typedef long long LL;

int main() {
  int cases;
  cin >> cases;
  for (int cas = 1; cas <= cases; cas++) {
    LL x;
    cin >> x;
    int a[25], len = 0;
    while (x > 0) {
      a[len++] = x % 10;
      x /= 10;
    }
    a[len++] = 0;
    int y;
    for (y = len-2; y >= 0; y--) {
      if (a[y] < a[y+1]) break;
    }
    if (y >= 0) {
      for (x = y+1; x < len; x++) {
	if (a[x] != a[y+1]) break;
      }
      a[x-1]--;
      for (x-=2; x >= 0; x--) {
	a[x] = 9;
      }
    }
    while (a[len-1] == 0) len--;
    
    printf("Case #%d: ", cas);
    for (x = len-1; x >= 0; x--) {
      cout << a[x];
    }
    cout << endl;
  }
  return 0;
}
