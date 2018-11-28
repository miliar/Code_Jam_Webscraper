#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <map>
#include <set> 
#include <sstream>
#include <fstream>
#include <utility>
#include <string>
#include <vector>
#include <stack>
#include <queue>
using namespace std;
#define REP(i,a) for(int i=0;i<a;i++)
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define SIZE(c) (int)c.size()
#define ALL(c) (c).begin(),(c).end() 
typedef pair<int, int> PII;

long long p(int x, int y) {
  if (y == 0) {
    return 1;
  }
  long long ret = p(x, y / 2);
  ret = ret * ret;
  if (y % 2 == 1) {
    ret *= x;
  }
  return ret;
}

long long dp[20][15][5];

long long go(int idx, int last, bool less, vector<int> &vec) {
  if (idx == SIZE(vec)) {
    return 0;
  }
  
  if (dp[idx][last][less] != -1) {
    return dp[idx][last][less];
  }
  
  long long currMul = p(10, SIZE(vec) - idx - 1);
  if (less) {
    long long next = go(idx + 1, 9, true, vec);
    if (next == -1) {
      return dp[idx][last][less] = next;
    }
    return dp[idx][last][less] = 9 *  currMul + next;
  } else {
    long long ret = -1;
    for (int i = vec[idx]; i >= 1; i--) {
      if (last == 10 || i >= last) {
        long long next = go(idx + 1, i, i < vec[idx], vec);
        if (next == -1) {
          continue;
        }
        next = i * currMul + next;
        ret = max(ret, next);
      } else {
        break;
      }
    }
    return dp[idx][last][less] = ret;
  }
}

long long solve(long long n) {
  vector<int> vec;
  while (n) {
    vec.push_back(n % 10);
    n /= 10;
  }
  reverse(ALL(vec));
  memset(dp, -1, sizeof dp);
  long long ret = go(0, 10, false, vec);
  
  if (ret == -1) {
    ret = 0;
    for (int i = 0; i < SIZE(vec) - 1; i++) {
      ret *= 10;
      ret += 9;
    }
    return solve(ret);
  }
  return ret;
}

int main() {
	//freopen("b.in", "r", stdin); 
	//freopen("B-small-attempt0.in", "r", stdin); freopen("B-small-attempt1.out", "w", stdout);
	//freopen("B-small-attempt1.in", "r", stdin); freopen("B-small-attempt1.out", "w", stdout);
	//freopen("B-small-attempt2.in", "r", stdin); freopen("B-small-attempt2.out", "w", stdout);
	//freopen("B-small-attempt3.in", "r", stdin); freopen("B-small-attempt3.out", "w", stdout);
	
	freopen("B-large.in", "r", stdin); freopen("B-large.out", "w", stdout);
	
	int nT;
	cin>>nT;
	for (int t=1; t<=nT; t++) {
    long long n;
    cin>>n;
		printf("Case #%d: ", t);
    cout << solve (n) << endl;
	}
	return 0;
}
