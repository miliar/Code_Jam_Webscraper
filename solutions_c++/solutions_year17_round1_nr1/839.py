#include<iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main() {
  int cases;
  cin >> cases;
  for (int cas = 1; cas <= cases; cas++) {
    int ny, nx;
    char a[30][30];
    
    cin >> ny >> nx;
    for (int y = 0; y < ny; y++) {
      for (int x = 0; x < nx; x++) {
	cin >> a[y][x];
      }
    }
    for (int y = 0; y < ny; y++) {
      char lastX = '?';
      for (int x = 0; x < nx; x++) {
	if (a[y][x] != '?') {
	  if (lastX == '?') {
	    for (int x2 = 0; x2 < x; x2++) {
	      a[y][x2] = a[y][x];
	    }
	  }
	} else {
	  a[y][x] = lastX;
	}
	lastX = a[y][x];
      }
    }
    if (a[0][0] == '?') {
      for (int y = 1; y < ny; y++) {
	if (a[y][0] != '?') {
	  for (int y2 = 0; y2 < y; y2++) {
	    for (int x = 0; x < nx; x++) {
	      a[y2][x] = a[y][x];
	    }
	  }
	  break;
	}
      }
    }
    for (int y = 1; y < ny; y++) {
      if (a[y][0] == '?') {
	for (int x = 0; x < nx; x++) {
	  a[y][x] = a[y-1][x];
	}
      }
    }
    printf("Case #%d:\n", cas);
    for (int y = 0; y < ny; y++) {
      for (int x = 0; x < nx; x++) {
	cout << a[y][x];
      }
      cout << endl;
    }
  }
  return 0;
}
