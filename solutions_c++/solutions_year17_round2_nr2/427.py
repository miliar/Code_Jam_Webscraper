#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <string.h>

using namespace std;

const double pi = acos(-1.0);
const double eps = 1E-7;

typedef long long int64;
typedef unsigned long long uint64;
#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)
#define sqr(x) ((x)*(x))
#define Abs(x) ((x) < 0 ? (-(x)) : (x))
typedef pair<int,int> ipair;
#define SIZE(A) ((int)A.size())
#define MP(A,B) make_pair(A,B)
#define PB(X) push_back(X)
#define ME(a) memset((a), 0, sizeof((a)))
#define MM(a, b) memcpy((a), (b), sizeof((a)))
#define FOR(i,n) for (int (i) = 0; (i) < (n); ++(i))
#define REP(i,a,b) for (int (i) = (a); (i) < (b); ++(i))

int Tests;
string S;
int n, a1, a12, a2, a23, a3, a13;

int main() {
	scanf("%d", &Tests); 
	for (int tts = 0; Tests--; ) {
    // R, O, Y, G, B, V
    scanf("%d%d%d%d%d%d%d", &n, &a1, &a12, &a2, &a23, &a3, &a13);

    printf("Case #%d: ", ++tts);

    if (a1 >= a2 && a1 >= a3) {
      if (a1 > a2 + a3) {
        puts("IMPOSSIBLE");
        continue;
      }
      S = "";
      for (int i = 0; i < a1; ++i) S += 'R';
      int j = 0;
      for (int i = 0; i < a2; ++i) {
        S = S.substr(0, 2 * j + 1) + 'Y' + S.substr(2 * j + 1, S.length() - 2 * j - 1);
        ++j;
      }
      int k = a3;
      for (int i = 0; i < a3 && j < a1; ++i) {
        S = S.substr(0, 2 * j + 1) + 'B' + S.substr(2 * j + 1, S.length() - 2 * j - 1);
        ++j;
        --k;
      }
      j = 0;
      for (int i = 0; i < k; ++i) {
        S = S.substr(0, 2 * j + 1) + 'B' + S.substr(2 * j + 1, S.length() - 2 * j - 1);
        ++j;
      }
    } else if (a2 >= a1 && a2 >= a3) {
      if (a2 > a1 + a3) {
        puts("IMPOSSIBLE");
        continue;
      }
      S = "";
      for (int i = 0; i < a2; ++i) S += 'Y';
      int j = 0;
      for (int i = 0; i < a1; ++i) {
        S = S.substr(0, 2 * j + 1) + 'R' + S.substr(2 * j + 1, S.length() - 2 * j - 1);
        ++j;
      }
      int k = a3;
      for (int i = 0; i < a3 && j < a2; ++i) {
        S = S.substr(0, 2 * j + 1) + 'B' + S.substr(2 * j + 1, S.length() - 2 * j - 1);
        ++j;
        --k;
      }
      j = 0;
      for (int i = 0; i < k; ++i) {
        S = S.substr(0, 2 * j + 1) + 'B' + S.substr(2 * j + 1, S.length() - 2 * j - 1);
        ++j;
      }
    } else if (a3 >= a1 && a3 >= a2) {
      if (a3 > a2 + a1) {
        puts("IMPOSSIBLE");
        continue;
      }
      S = "";
      for (int i = 0; i < a3; ++i) S += 'B';
      int j = 0;
      for (int i = 0; i < a2; ++i) {
        S = S.substr(0, 2 * j + 1) + 'Y' + S.substr(2 * j + 1, S.length() - 2 * j - 1);
        ++j;
      }
      int k = a1;
      for (int i = 0; i < a1 && j < a3; ++i) {
        S = S.substr(0, 2 * j + 1) + 'R' + S.substr(2 * j + 1, S.length() - 2 * j - 1);
        ++j;
        --k;
      }
      j = 0;
      for (int i = 0; i < k; ++i) {
        S = S.substr(0, 2 * j + 1) + 'R' + S.substr(2 * j + 1, S.length() - 2 * j - 1);
        ++j;
      }
    }
    cout << S << endl;
	}
	return 0;
}