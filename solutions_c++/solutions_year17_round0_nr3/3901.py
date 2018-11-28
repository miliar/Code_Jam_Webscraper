#define _USE_MATH_DEFINES
#define INF 0x3f3f3f3f

#include <iostream>
#include <cstdio>
#include <sstream>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <stack>
#include <limits>
#include <map>
#include <string>
#include <cstring>
#include <set>
#include <deque>
#include <bitset>
#include <list>
#include <cctype>
#include <utility>

using namespace std;

typedef long long ll;
typedef pair <int,int> P;
typedef pair <int,P> PP;

static const double EPS = 1e-8;

static const int tx[] = {0,1,0,-1};
static const int ty[] = {-1,0,1,0};

int main(){
  int T;

  while (~scanf("%d",&T)) {
    for (int test_i = 1; test_i <= T; test_i++) {
      int N, K;
      scanf("%d %d", &N, &K);
      priority_queue<int, vector<int>, less<int> > que;
      que.push(N);
      for (int i = 0; i < K - 1; i++) {
	int length = que.top() - 1; que.pop();
	int lhs = length / 2;
	int rhs = length - lhs;
	que.push(lhs);
	que.push(rhs);
      }
      int length = que.top() - 1;
      int lhs = length / 2;
      int rhs = length - lhs;
      printf("Case #%d: %d %d\n", test_i, rhs, lhs);
    }
  }
}
