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

int R, C;
vector<string> input;
vector<vector<int> > chk;

int main() {//bitwise로 해보자
  // freopen( "A-large.in" , "r" , stdin );
  freopen( "out.txt" , "w" , stdout );
  int casenums = 0;
  scanf( "%d" , &casenums);
  for ( int casenum = 1; casenum <= casenums; ++casenum) {
    scanf("%d %d", &R, &C);
    chk = vector<vector<int> >(R, vector<int>(C, 0));
    input.clear();
    FOR(i, 0, R) {
      string im;
      cin >> im;
      input.push_back(im);
    }
    FOR(i, 0, R) {
      FOR(j, 0, C) {
        if (input[i][j] != '?' ) chk[i][j] = 1;
      }
    }

    //아직 처리하지 않은 알파벳을 하나 잡아서
    FOR(i, 0, R) {
      FOR(j, 0, C) {
        if (chk[i][j] == 0)continue;
        // cout << input[i][j] << endl;

        //상하좌우 최대한 확장한다
        int startX = 0, endX = 0, startY = 0, endY = 0;
        FOR(k, 1, 26) {
          if (j + k == C
              || input[i][j + k] != '?') {
            endX = j + k - 1;
            break;
          }
        }
        FOR(k, 1, 26) {
          if (j - k == -1
              || input[i][j - k] != '?') {
            startX = j - k + 1;
            break;
          }
        }

        FOR(k, 1, 26) {
          int chkhaja = 0;
          FORI(l, startX, endX) {
            if (i + k == R
                || input[i + k][l] != '?') {
              chkhaja = 1;
              break;
            }
          }
          if (chkhaja == 1) {
            endY = i + k - 1;
            break;
          }
        }
        FOR(k, 1, 26) {
          int chkhaja = 0;
          FORI(l, startX, endX) {
            if (i - k == -1
                || input[i - k][l] != '?') {
              chkhaja = 1;
              break;
            }
          }
          if (chkhaja == 1) {
            startY = i - k + 1;
            break;
          }
        }

        FORI(k, startY, endY) {
          FORI(l, startX, endX) {
            input[k][l] = input[i][j];
          }
        }
        // cout << startY << endY << endl;
        // cout << startX << endX << endl;
        // FOR(i, 0, R) {
        //   cout << input[i] << endl;
        // }
        // cout << "---------" << endl;
      }
    }

    printf( "Case #%d: \n" , casenum);
    FOR(i, 0, R) {
      cout << input[i] << endl;
    }
  }
}