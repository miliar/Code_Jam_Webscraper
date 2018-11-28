#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef long long lglg;

int low(int good) {
  if(good % 10 != 0) {
    return (good * 9) / 10 + 1;
  }
  return (good * 9) / 10;
}

int high(int good) {
  return (good * 11) / 10;
}

int main()
{
  int T;
  scanf("%d", &T);

  for(int t = 0; t < T; ++t) {
    printf("Case #%d: ", t+1);

    int ret = 0;

    int n, p;

    int ideal[50];
    int pack[50][51];
    int idx[50];

    scanf("%d%d", &n, &p);

    for (int i = 0; i < n; ++i) {
      scanf("%d", &(ideal[i]));
    }


    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < p; ++j) {
        scanf("%d", &(pack[i][j]));
      }
      sort(&(pack[i][0]), &(pack[i][p]));
      idx[i] = 0;
    }

    int serv = 1;

    while(true) {
      bool end = false;
      bool good = true;

      for (int i = 0; i < n; ++i) {
        while(idx[i] < p && pack[i][idx[i]] < low(serv*ideal[i])) {
          ++idx[i];
        }

        if(idx[i] >= p) {
          end = true;
          break;
        }

        if(pack[i][idx[i]] > high(serv*ideal[i])) {
          good = false;
          break;
        }
      }

      if(end) {
        break;
      }

      if(good) {
        for (int i = 0; i < n; ++i) {
          ++idx[i];
        }
        ++ret;
      } else {
        ++serv;
      }
    }

    printf("%d\n", ret);
  }

  return 0;
}
