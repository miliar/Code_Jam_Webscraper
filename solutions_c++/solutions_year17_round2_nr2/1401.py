/**
 * Problem: B
 */
#include <algorithm>
#include <assert.h>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <iterator>
#include <list>
#include <limits>
#include <map>
#include <math.h>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <tuple>
#include <vector>
#include <stdexcept>
#include <typeinfo>

#define SZ(x) (int)(x.size())
#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)
#define FV(v) for(auto it = v.begin();it!=v.end();++it)
#define TR(x) cout << #x << " = " << x << endl
#define _ << " _ " <<

using namespace std;

typedef long long ll;
typedef vector<ll> vll;

int N, R, O, Y, G, B, V;

// R 0
// O 1
// Y 2
// G 3
// B 4
// V 5

char letters[6] = { 'R', 'O', 'Y', 'G', 'B', 'V' };
int H[6];

int main(int argc, const char **argv) {
  int cases;
  cin >> cases;
  int iMax, jMax, prev;
  int max;
  string str;
  F1(caseI, cases) {
    cin >> N;
    max = 0;
    str = "";
    F0(i, 6) {
      cin >> H[i];
      if (H[i] > max) {
        max = H[i];
        iMax = i;
      }
    }

    prev = -1;
    while (true) {
      max = 0;
      F0(i, 6) {
        if (i == prev) continue;
        if (H[i] >= max) {
          max = H[i];
          jMax = i;
        }
      }

      if (max == 0) break;
      if (H[iMax] == max && iMax != prev) {
        H[iMax]--;
        str += letters[iMax];
        prev = iMax;
      } else {
        H[jMax]--;
        str += letters[jMax];
        prev = jMax;
      }
    }

    if (str[0] == str[str.size()-1]) {
      cout << "Case #" << caseI << ": IMPOSSIBLE" << endl;
    } else {
      cout << "Case #" << caseI << ": " << str << endl;
    }

  }

  return 0;
}
