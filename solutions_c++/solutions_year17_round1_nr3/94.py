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

int at(int ad, int hk, int b, int nb) {
  int a = ad + b*nb;
  return nb + (hk+a-1) / a;
}

int t(int hd, int ak, int d, int nd, int at) {
  int ret = 0;
  if(ak - d + ak - 2*d >= hd) return -1;
  int h = hd;
  for(int i = 0; i < nd; ++i) {
    ++ret;
    ak -= d;
    if(ak >= h) {
      ++ret;
      h = hd - ak - d;
    }
    h -= ak;
  }

  if(hd <= ak * 2) return -1;

  for(int i = 0; i < at-1; ++i) {
    ++ret;
    if(ak >= h) {
      ++ret;
      h = hd - ak;
    }
    h -= ak;
  }
  ++ret;

  return ret;

}

int best(int hd, int ad, int hk, int ak, int b, int d) {
  int nb = 0;
  int atnb = at(ad, hk, b, nb);

  if(b > 0) {
    int nbl = 0;
    int nbh = (hk - ad + b - 1) / b;

    for (int i = 1; i <= nbh; ++i) {
      int ati = at(ad, hk, b, i);
      if(ati < atnb) {
        nb = i;
        atnb = ati;
      }
    }
  }

  if(atnb < 2) {
    return atnb;
  }

  if(atnb == 2 && ak < hd) {
    return atnb;
  }

  int nd = 0;
  int ret = t(hd, ak, d, nd, atnb);

  if(d > 0) {
    int ndh = (ak + d - 1) / d;
    for (int i = 1; i <= ndh; ++i) {
      int ti = t(hd, ak, d, i, atnb);
      if(ti < ret || ret == -1) {
        nd = i;
        ret = ti;
      }
    }
  }

  return ret;

}

int main()
{
  int T;
  scanf("%d", &T);

  for(int t = 0; t < T; ++t) {
    printf("Case #%d: ", t+1);

    int hd, ad, hk, ak, b, d;

    scanf("%d%d%d%d%d%d", &hd, &ad, &hk, &ak, &b, &d);

    int ret = best(hd, ad, hk, ak, b, d);

    if(ret < 0) {
      printf("IMPOSSIBLE\n");
    } else {
      printf("%d\n", ret);
    }
  }

  return 0;
}
