/**
 * jerry
 * C.cpp
 */

#include <assert.h>
#include <ctype.h>
#include <limits.h>
#include <math.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#include <algorithm>
#include <array>
#include <bitset>
#include <chrono>
#include <complex>
#include <deque>
#include <forward_list>
#include <fstream>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <memory>
#include <numeric>
#include <queue>
#include <random>
#include <regex>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

using namespace std;

typedef long long int lli;
typedef pair<int, int> pii;
typedef pair<int, lli> pil;
typedef pair<lli, int> pli;
typedef pair<lli, lli> pll;

int gInt () {
  int i;
  scanf("%d", &i);
  return i;
}

lli gLong () {
  lli i;
  scanf("%lld", &i);
  return i;
}

double gDouble () {
  double i;
  scanf("%lf", &i);
  return i;
}

void quit () {
  fflush(stdout);
  exit(0);
}

lli hd, ad;
lli hk, ak;
lli b, d;

/*
pll reqd(lli nd) {
  lli applied = 0;
  lli moves = 0;
  lli h = hd;
  lli a = ak;
  bool waslastheal = false;
  for (; applied < nd; ++moves) {
    lli nexta = max<lli>(0, a - d);
    if (h - nexta <= 0) {
      if (waslastheal) {
        return make_pair(-1, -1);
      }
      h = hd;
      waslastheal = true;
    } else {
      a = nexta;
      h -= a;
      ++applied;
      waslastheal = false;
    }
  }
  return make_pair(moves, h);
}

lli req(lli nd, lli nb) {
  lli moves = 0;
  if (b == 0) {
    nb = 0;
  }
  if (d == 0) {
    nd = 0;
  }

  // Handle debuffs
  pll reqdres = reqd(nd);
  moves += reqd.first;
  lli myh = reqd.second;
  lli hisa = max<lli>(0, ak - d * nd);

  return moves;
}
*/

// state: his health, my atk, his atk
// result: num moves, my health
pll dp[101][101][101];

lli solve() {
  hd = gLong();
  ad = gLong();
  hk = gLong();
  ak = gLong();
  b = gLong();
  d = gLong();
  lli maxadhk = max(ad, hk);

  for (lli i = 0; i <= hk; ++i) {
    for (lli j = ad; j <= maxadhk; ++j) {
      for (lli k = 0; k <= ak; ++k) {
        dp[i][j][k] = make_pair<lli>(999999999999LL, 0);
      }
    }
  }
  dp[hk][ad][ak] = make_pair<lli>(0, -hd);

  lli ans = 99999999999LL;
  for (lli i = hk; i >= 0; --i) {
    for (lli j = ad; j <= maxadhk; ++j) {
      for (lli k = ak; k >= 0; --k) {
        lli prevmoves = dp[i][j][k].first;
        lli prevhd = -dp[i][j][k].second;
        if (prevhd < 0) {
          continue;
        }

        //fprintf(stderr, "his health: %lld   my attack: %lld   his attack: %lld   moves: %lld   myhealth: %lld\n", i, j, k, prevmoves, prevhd);

        // transition: attack
        lli nexti = max<lli>(0, i - j);
        if (nexti == 0) {
          dp[nexti][j][k] = min(dp[nexti][j][k], make_pair<lli>(prevmoves + 1, -prevhd));
          ans = min(ans, prevmoves + 1);
        } else {
          if (prevhd <= k) {
            if (2 * k < hd) {
              dp[nexti][j][k] = min(dp[nexti][j][k], make_pair<lli>(prevmoves + 2, -(hd - 2 * k)));
            }
          } else {
            dp[nexti][j][k] = min(dp[nexti][j][k], make_pair<lli>(prevmoves + 1, -(prevhd - k)));
          }
        }

        // transition: buff
        if (b > 0) {
          lli nextj = min(maxadhk, j + b);
          if (prevhd <= k) {
            if (2 * k < hd) {
              dp[i][nextj][k] = min(dp[i][nextj][k], make_pair<lli>(prevmoves + 2, -(hd - 2 * k)));
            }
          } else {
            dp[i][nextj][k] = min(dp[i][nextj][k], make_pair<lli>(prevmoves + 1, -(prevhd - k)));
          }
        }

        // transition: debuff
        if (d > 0) {
          lli nextk = max<lli>(0, k - d);
          if (prevhd <= nextk) {
            if (k + nextk < hd) {
              dp[i][j][nextk] = min(dp[i][j][nextk], make_pair<lli>(prevmoves + 2, -(hd - k - nextk)));
            }
          } else {
            dp[i][j][nextk] = min(dp[i][j][nextk], make_pair<lli>(prevmoves + 1, -(prevhd - nextk)));
          }
        }
      }
    }
  }

  return ans;
}

int main (int argc, char ** argv) {
  int t = gInt();
  for (int i = 0; i < t; ++i) {
    lli ans = solve();
    printf("Case #%d: ", i + 1);
    if (ans >= 99999999999LL) {
      printf("IMPOSSIBLE\n");
    } else {
      printf("%lld\n", ans);
    }
  }
  quit();
}
