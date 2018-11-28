#include <cstdio>
#include <cassert>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <utility>
#include <sstream>
using namespace std;
typedef long long ll;

void solve() {
  ll N;
  char buf[100];
  scanf(" %s", buf);
  int len = strlen(buf);
  bool flag = false;
  for (int i = len - 2; i >= 0; i--) {
    if (flag) {
      if (buf[i] > '0') {
	buf[i]--;
	flag = false;
      } else {
	buf[i] = '9';
      }
    }
    if (buf[i] > buf[i+1]) {
      if (buf[i] > '0') {
	buf[i]--;
      } else {
	buf[i] = '9';
	flag = true;
      }
      for (int j = i + 1; j < len; j++) {
	buf[j] = '9';
      }
    }
  }
  for (int i = 0; i < len; ++i) {
    if (buf[i] != '0' || i == len - 1) {
      printf("%s\n", buf + i);
      break;
    }
  }
}

int main() {
  int T;
  scanf(" %d", &T);
  for (int ii = 0; ii < T; ii++) {
    printf("Case #%d: ", ii + 1);
    solve();
  }
}
