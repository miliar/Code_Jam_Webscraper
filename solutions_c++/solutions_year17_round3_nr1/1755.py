#define _CRT_SECURE_NO_WARNINGS
//자료구조
#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional> //greater, less

#include <tuple>
#include <utility>

#include <iostream>
#include <string>
#include <cstring>
#include <memory>
#include <cmath>
#ifndef M_PI
#define M_PI (3.14159265358979323846264338327950288)
#endif

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define FORD(i,a,b) for(int i=(a);i>(b);--i)
#define FORI(i,a,b) for(int i=(a);i<=(b);++i)
#define FORID(i,a,b) for(int i=(a);i>=(b);--i)
#define REP(i,a) for(int i=0;i<(a);++i)
#define MAX(a,b) a = max(a,b)
#define MIN(a,b) a = min(a,b)

typedef long long LL;
//typedef pair<int,int> pii;
//typedef pair<LL,LL> pll;
// typedef pair<string,string> pss;
typedef vector<int> vi;
typedef vector<vi> vvi;
// typedef vector<pii> vii;
// typedef vector<LL> vl;
// typedef vector<vl> vvl;

int N, K;
vector<pair<int, int> > R;

bool cmp(const pair<int, int> &a, pair<int, int> &b) {
  double AA = 2 * a.first * M_PI * a.second;
  double BB = 2 * b.first * M_PI * b.second;
  return AA > BB;
}

int main() {//bitwise로 해보자
  // freopen( "A-large.in" , "r" , stdin );
  freopen( "out.txt" , "w" , stdout );
  int casenums = 0;
  scanf( "%d" , &casenums);

  for ( int casenum = 1; casenum <= casenums; ++casenum) {
    scanf("%d %d", &N, &K);
    R = vector<pair<int, int> >(N, make_pair(0, 0));

    double ret = 0.0;
    FOR(i, 0, N) {
      scanf("%d %d", &R[i].first, &R[i].second);
      // cout << R[i] << H[i] << endl;
    }
    sort(R.begin(), R.end(), cmp);
    FOR(i, 0, N) {
      double rr = 0.0;
      rr += pow(R[i].first, 2) * M_PI;
      rr += 2 * R[i].first * M_PI * R[i].second;

      // cout << maxR << endl;

      // R.erase(R.begin() + idx);
      // FOR(i, 0, N) {
      //   cout << R[i].first << " " << R[i].second << endl;
      // }
      // cout << endl;
      int cnt = 0;
      int idx = 0;
      while (cnt < K - 1 && idx < N) {
        if (i == idx || R[i].first < R[idx].first) {
          idx++;
          continue;
        }
        rr += 2 * R[idx].first * M_PI * R[idx].second;
        // cout << i << " " << R[i].first << " " << R[i].second << endl;
        cnt++;
        idx++;
      }
      MAX(ret, rr);
    }

    printf( "Case #%d: %.9f\n" , casenum, ret);
  }

}
