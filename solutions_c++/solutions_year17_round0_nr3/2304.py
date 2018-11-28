#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>

using namespace std;

#define ll          long long
#define pb          push_back
#define mp          make_pair
#define pii         pair<int,int>
#define vi          vector<int>
#define all(a)      (a).begin(),(a).end()
#define F           first
#define S           second
#define sz(x)       (int)x.size()
#define hell        1000000007
#define endl        '\n'

using namespace std;
int test = 1;

//             499        X        500
//        249   X   249       249   X   250
//     124 X 124 124 X 124 124 X 124 124 X 125
//
// 499X500                                               // 1 X
// 249X249 249X250                                       // 2 Xs
// (124X124)*3 124X125                                   // 4 Xs
// (61X62)*7                             (62X62)         // 8 Xs
// (30X30 30X31)*7                       (30X31)*2       // 16 Xs
// ((14X15)*3 15X15)*7                (14X15 15X15)*2    // 32 Xs
// ((6X7 7X7)*3 (7X7)*2)*7            (6X7 (7X7)*3)*2    // 64 Xs
// ((2X3 (3X3)*3)*3 (3X3)*4)*7        (2X3 (3X3)*7)*2    // 128 Xs
// ((0X1 (1X1)*7)*3 (1X1)*8)*7        (0X1 (1X1)*15)*2   // 256 Xs
//
// Min Parts                                    Small, Large
//1000    1                                         1, 0
// 499    2  0,1                                    1, 1                499 = 1000/2-1
// 249    4  0*3,1                                  3, 1      4-1=3     249 = 499/2
// 124    8  0*7,1                                  7, 1      8-1=7     124 = 249/2
// 61    16  (0,1)*7,1*2                            7, 9     16-7=9      61 = 124/2-1
// 30    32  (0*3,1)*7,(0,1)*2                     23, 9     32-9=23     30 = 61/2
// 14    64  ((0,1)*3,1*2)*7,(0,1*3)*2             23, 41   64-23=41     14 = 30/2-1
// 6    128  ((0,1*3)*3,1*4)*7,(0,1*7)*2           23, 105 128-23=105     6 = 14/2-1
// 2    256  ((0,1*4)*3,1*8)*7,(0,1*8)*2           23, 233 256-23=233     2 = 6/2-1
// 0    512  ((0,1*8)*3,1*16)*7,(0,1*16)*2         23, 489 512-23=489     0 = 2/2-1

// Min  Parts  Small, Large
//  4      1       1, 0
//  1      2       1, 1

void solve() {
  cout << "Case #" << test++ << ": ";
  unsigned long long n, k;
  cin >> n >> k;

  unsigned long long Parts = 1, Small = 1, Large = 0, Max, Min = n;

  while (k) {
    if (k <= Parts) {
      // All K people fit in partitions at this level.

      if (k <= Large) {
        // All people fit in large partitions.
        ++Min;
      }

      if (Min % 2) {
        // Odd.
        Min /= 2;
        Max = Min;
      } else {
        // Even.
        Min = Min/2 - 1;
        Max = Min + 1;
      }

      break;
    }

    // More people than partitions: fill up all Parts, then subdivide.
    k -= Parts;
    Parts *= 2;

    if (Min % 2) {
      // Odd.
      Min /= 2;
      Small = Parts - Large;  // Large = Large;
    } else {
      // Even.
      Min = Min/2 - 1;
      Large = Parts - Small;  //Small = Small;
    }
  }
  cout << Max << " " << Min << endl << flush;
}

signed main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  int t = 1;
  cin >> t;
  while (t--) {
    solve();
  }
  return 0;
}

