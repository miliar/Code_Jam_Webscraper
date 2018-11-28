#include <cstdio>
#include <iostream>
#include <cmath>
#include <string>
#include <list>
#include <vector>
#include <algorithm>
#include <functional>
#include <utility>
#include <set>
#include <map>
#include <complex>
#include <queue>
#include <stack>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <string.h>
#include <unordered_set>
#include <unordered_map>
#include <mmintrin.h>
#include <xmmintrin.h>
#include <emmintrin.h>

#ifndef ONLINE_JUDGE
#include <gperftools/profiler.h>
#endif

using namespace std;

typedef unsigned int uint;
typedef long long int64;
typedef unsigned long long uint64;
typedef unsigned short ushort;
typedef unsigned char uchar;
typedef pair<int, int> ipair;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
#define SIZE(A) ((int)(A.size()))
#define LENGTH(A) ((int)(A.length()))
#define MP(A, B) make_pair(A,B)
const double pi = acos(-1.0);
#define FOR(i, a, b) for(int i=(a);i<(b);++i)
#define REP(i, a) for(int i=0;i<(a);++i)
#define ALL(a) (a).begin(),(a).end()

template<class T>
T sqr(const T& x) { return x * x; }

template<class T>
T lowbit(const T& x) { return (x ^ (x - 1)) & x; }

template<class T>
int countbit(const T& n) { return (n == 0) ? 0 : (1 + countbit(n & (n - 1))); }

template<class T>
void ckmin(T& a, const T& b) { if (b < a) a = b; }

template<class T>
void ckmax(T& a, const T& b) { if (b > a) a = b; }


int64 buff, debuff;

int64 solve_debuff(int64 num_attack, int64 num_debuff, int64 full_hd, int64 ak) {
  if (debuff == 0 && num_debuff > 0) return -1;
  int64 mcnt = 0;
  if (debuff > 0) mcnt = (ak + debuff - 1) / debuff;

  int64 ret = 0;
  int64 hd = full_hd;
  int64 last_debuff_round = 0;
  for (int64 round = 0; num_debuff > 0 && ak > 0; ++round) {
    ++ret;
    if (ak - debuff >= hd) {
      hd = full_hd;
    } else {
      ak = max(0LL, ak - debuff);
      --num_debuff;
      last_debuff_round = round;
    }
    hd -= ak;
    if (hd <= 0) return -1;
    if (round - last_debuff_round > 10) return -1;
  }
  /*
  for (; num_attack > 0; ) {
    int64 cnt = num_attack;
    int64 dcnt = (1LL << 60);
    if (ak > 0) ckmin(dcnt, (hd + ak - 1) / ak);
    if (dcnt >= cnt) {
      ret += cnt;
      break;
    }
    cnt = dcnt - 1;
    if (cnt <= 0) return -1;
    ret += cnt;
    num_attack -= cnt;
    ++ret;
    hd = full_hd - ak;
    if (hd <= 0) return -1;
  }
   */
  int64 last_attack_round = 0;
  for (int64 round = 0; num_attack > 0; ++round) {
    ++ret;
    if (num_attack <= 1) break;
    if (ak >= hd) {
      hd = full_hd;
    } else {
      --num_attack;
      last_attack_round = round;
    }
    hd -= ak;
    if (hd <= 0) return -1;
    if (round - last_attack_round > 10) return -1;
  }
  return ret;
}

int64 solve_attack(int64 ad, int64 hk) {
  int64 ret = (hk + ad - 1) / ad;
  if (buff == 0) return ret;
  int64 low = 0, high = ret;
  for (; high - low > 10000; ) {
    int64 x1 = (low * 2 + high) / 3;
    int64 x2 = (low + high * 2) / 3;
    int64 ad1 = ad + x1 * buff;
    int64 ad2 = ad + x2 * buff;
    int64 r1 = x1 + (hk + ad1 - 1) / ad1;
    int64 r2 = x2 + (hk + ad2 - 1) / ad2;
    ckmin(ret, r1);
    ckmin(ret, r2);
    if (r1 < r2)
      high = x2;
    else
      low = x1;
  }
  for (int64 x1 = low; x1 <= high; ++x1) {
    int64 ad1 = ad + x1 * buff;
    int64 r1 = x1 + (hk + ad1 - 1) / ad1;
    ckmin(ret, r1);
  }
  return ret;
}

int main() {
  //freopen("/home/acrush/CLionProjects/helloworld/input.txt", "r", stdin);
  freopen("/home/acrush/CLionProjects/helloworld/c1.in", "r", stdin); freopen("/home/acrush/CLionProjects/helloworld/c1.out", "w", stdout);
  // freopen("/home/acrush/CLionProjects/helloworld/c2.in", "r", stdin); freopen("/home/acrush/CLionProjects/helloworld/c2.out", "w", stdout);

  // std::ios_base::sync_with_stdio(false);
  int ntestcase;
  cin >> ntestcase;
  int64 hd, ad;
  int64 hk, ak;
  for (int case_id = 1; case_id <= ntestcase; ++case_id) {
    printf("Case #%d: ", case_id);
    cin >> hd >> ad >> hk >> ak >> buff >> debuff;
    int64 num_attack = solve_attack(ad, hk);
    int64 ret = (1LL << 60);
    for (int64 num_debuff = 0; num_debuff <= 100000; ++num_debuff) {
      int64 t = solve_debuff(num_attack, num_debuff, hd, ak);
      if (t >= 0 && t < ret) ret = t;
    }
    if (ret >= (1LL << 60)) {
      printf("IMPOSSIBLE\n");
    } else {
      printf("%lld\n", ret);
    }
  }

  return 0;
}