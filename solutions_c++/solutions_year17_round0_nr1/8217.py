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


int main() {//bitwise로 해보자
  // freopen( "A-large.in" , "r" , stdin );
  freopen( "out.txt" , "w" , stdout );
  int casenums = 0;
  scanf( "%d" , &casenums);
  for ( int casenum = 1; casenum <= casenums; ++casenum) {
    string S;
    cin >> S;
    int K = 0, ret = 0;;
    scanf("%d", &K);
    FORI(i, 0, S.size() - K) {
      if (S[i] == '-') {
        ret++;
        FOR(j, 0, K) {
          S[i + j] = (S[i + j] == '+' ? '-' : '+');
        }
      }
    }
    int chk = 0;
    FOR(i, 0, S.size()) {
      if (S[i] == '-') {
        chk = 1;
        break;
      }
    }
    if (chk == 0) {
      //입출력
      printf( "Case #%d: " , casenum);
      cout << ret << endl;
    } else {
      printf( "Case #%d: IMPOSSIBLE\n" , casenum);
    }
  }
}