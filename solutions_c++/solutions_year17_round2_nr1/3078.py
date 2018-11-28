#include <iostream>
#include <algorithm>
#include <cstdio>
#include <string>
#include <cstring>
#include <cctype>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <map>
using namespace std;
 
#define REP(i, s, e) for (int i = (s); i < (e); i++)
#define REPI(i, s, e) for (int i = (s); i <= (e); i++)
#define rep(i, n) REP(i, 0, n)
#define repi(i, n) REPI(i, 0, n)
#define ALL(v) (v).begin(), (v).end()
 
#define dump(x) (cout << #x << " = " << x << endl)
#define dump2(x, y) (cout << "(" << #x << ", " << #y << ") = (" << x << ", " << y << ")" << endl)
#define dump3(x, y, z) (cout << "(" << #x << ", " << #y << ", " << #z << ") = (" << x << ", " << y << ", "<< z << ")" << endl)
 
typedef long long ll;
typedef pair<int, int> pii;


typedef long long ll;
typedef pair<int, int> pii;

int main()
{
  int T, D, N, K, S;
  int tc, nc;
  double hour, max_h, result;

  cin >> T;

  rep(tc, T){
    max_h = -1;
    cin >> D >> N;
    rep(nc, N){
      cin >> K >> S;
      hour = ((double) D - (double) K) / S;
      max_h = max(hour, max_h);
    }
    result = (double) D / max_h;
    printf("Case #%d: %.6lf", tc + 1, result);
    cout << endl;
  }
  return 0;


}