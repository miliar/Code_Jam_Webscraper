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

LL N, maxNum = 0;

LL pp(LL d, LL u) {
  LL ret = 1;
  FOR(i, 0, u) {
    ret *= d;
  }
  return ret;
}

bool recur(LL n, LL before, LL num) {//n자리에, n+1자리의 숫자는 before일때, 가능한가?
  // cout << n << " " << before << " " << num << endl;
  if (n == -1) return true;
  for (LL i = 9; i >= before; i--) {
    // cout << num + i * pow(10, n) << endl;
    if (num + i * pp(10, n) > N) {
      continue;
    }
    if (recur(n - 1, i, num + i * pp(10, n))) {
      maxNum += i * pp(10, n);
      return true;
    }
  }
  return false;
}

int main() {//bitwise로 해보자
  // freopen( "A-large.in" , "r" , stdin );
  freopen( "out.txt" , "w" , stdout );
  int casenums = 0;
  scanf( "%d" , &casenums);
  for ( int casenum = 1; casenum <= casenums; ++casenum) {
    cin >> N;
    LL dd = N;
    LL cnt = 0;
    maxNum = 0;
    while (dd > 0) {
      dd /= 10;
      cnt++;
    }
    recur(cnt - 1, 0, 0);
    printf( "Case #%d: " , casenum);
    cout << maxNum << endl;
  }
}