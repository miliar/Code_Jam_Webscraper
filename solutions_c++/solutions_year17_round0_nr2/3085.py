#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <cstring>
#include <cassert>
#include <utility>
#include <iomanip>

using namespace std;

int tn;
long long n;

bool tidy(long long x) {
  int lst = 9;
  while (x) {
    int cur = x % 10;
    x /= 10;
    if (cur > lst) {
      return false;
    }
    lst = cur;
  }
  return true;
}

int main() {
  //assert(freopen("input.txt","r",stdin));
  //assert(freopen("output.txt","w",stdout));

  scanf("%d", &tn);

  for (int test = 1; test <= tn; test++) {
    cin >> n;
    while (!tidy(n)) {
      n--;
    }
    printf("Case #%d: ", test);
    cout << n << endl;
  }

  return 0;
}