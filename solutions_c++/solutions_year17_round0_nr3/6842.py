#include <algorithm>
#include <assert.h>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <iterator>
#include <map>
#include <math.h>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

#define SZ(x) (int)(x.size())
#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)
#define TR(x) cout << #x << " = " << x << endl
#define _ << " _ " <<

bool tab[1000500];
int N, K;

void find(int &idx, int &l) {
  int len = 0;
  int iPrev;
  idx = -1;
  l = 0;
  F0(i, N+2) {
    if (!tab[i]) {
      len++;
    } else {
      if (len > 0 && len > l) {
        idx = iPrev;
        l = len;
      }
      iPrev = i+1;
      len = 0;
    }
  }
}

void print() {
  F0(i, N+2) {
    cout << (tab[i] ? '0' : '.');
  }
  cout << endl;
}

void calc(int idx, int &l, int &r) {
  int k = idx;
  l = 0;
  r = 0;
  while (!tab[--k]) {
    l++;
  }
  while (!tab[++idx]) {
    r++;
  }
}

int main(int argc, const char **argv) {
  int cases;
  cin >> cases;
  int idx, l;
  int left, right;
  F1(caseI, cases) {
    memset(tab, 0, sizeof(tab));
    cin >> N >> K;
    tab[0] = 1;
    tab[N + 1] = 1;
    F0(i, K) {
      // print();
      find(idx, l);
      assert(idx != -1);
      // std::cout << "idx:" << idx << std::endl;
      // std::cout << "l:" << l << std::endl;
      tab[idx + (l-1) / 2] = 1;
    }
    // print();
    calc(idx + (l-1) / 2, left, right);
    cout << "Case #" << caseI << ": " << max(left, right) << " " << min(left, right) << endl;
  }


  return 0;
}

