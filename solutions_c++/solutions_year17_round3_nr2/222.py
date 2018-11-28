#include <iostream>
#include <climits>
#include <queue>

#include <cassert>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define FORE(i,a,b) for(int i=(a);i<=(b);i++)
#define SET(A,p) memset(A,p,sizeof(A))

int busy[1<<11];
int dp[2][2][1<<10][1<<10];

struct state {
  int started_with;
  int last_with;
  int mins_0;
  int mins_1;

  state(int _started_with, int _last_with, int _mins_0, int _mins_1) {
    started_with = _started_with;
    last_with = _last_with;
    mins_0 = _mins_0;
    mins_1 = _mins_1;
  }
};

void adjust(int &a, int b) {
  if (a == -1) a = b;
  a = min(a,b);
}

void consider(queue<state> &Q, int p, int q, int r, int s) {
  if (dp[p][q][r][s] == -1) Q.push(state(p,q,r,s));
}

void do_case(int tc) {
  int P,Q;
  cin >> P >> Q;
  SET(busy,0);
  FOR(i,0,P) {
    int a, b;
    cin >> a >> b;
    FOR(j,a,b) busy[j] = 1;
  }
  FOR(i,0,Q) {
    int a, b;
    cin >> a >> b;
    FOR(j,a,b) busy[j] = 2;
  }
  SET(dp,-1);
  
  queue<state> qu;
  consider(qu,0,0,1,0);
  dp[0][0][1][0] = 0;
  consider(qu,1,1,0,1);
  dp[1][1][0][1] = 0;

  for(int i=1;i<1440;i++) {
    int ops = qu.size();
    assert(ops > 0);
    while(ops) {
      state cur = qu.front();
      qu.pop();
      if (cur.last_with == 0) {
        if(busy[i] != 1 && cur.mins_0 < 720) {
          consider(qu,cur.started_with,0,cur.mins_0+1,cur.mins_1);
          adjust(
            dp[cur.started_with][0][cur.mins_0+1][cur.mins_1],
            dp[cur.started_with][cur.last_with][cur.mins_0][cur.mins_1]);
        }
        if(busy[i] != 2 && cur.mins_1 < 720) {
          consider(qu,cur.started_with,1,cur.mins_0,cur.mins_1+1);
          adjust(
            dp[cur.started_with][1][cur.mins_0][cur.mins_1+1],
            1 + dp[cur.started_with][cur.last_with][cur.mins_0][cur.mins_1]);
        }
      } else {
        if(busy[i] != 2 && cur.mins_1 < 720) {
          consider(qu,cur.started_with,1,cur.mins_0,cur.mins_1+1);
          adjust(
            dp[cur.started_with][1][cur.mins_0][cur.mins_1+1],
            dp[cur.started_with][cur.last_with][cur.mins_0][cur.mins_1]);
        }
        if(busy[i] != 1 && cur.mins_0 < 720) {
          consider(qu,cur.started_with,0,cur.mins_0+1,cur.mins_1);
          adjust(
            dp[cur.started_with][0][cur.mins_0+1][cur.mins_1],
            1 + dp[cur.started_with][cur.last_with][cur.mins_0][cur.mins_1]);
        }
      }
      ops--;
    }
  }

  int res = INT_MAX;
  if (dp[0][0][720][720] != -1) {
    res = min(res,dp[0][0][720][720]);
  }
  if (dp[0][1][720][720] != -1) {
    res = min(res,1+dp[0][1][720][720]);
  }
  if (dp[1][0][720][720] != -1) {
    res = min(res,1+dp[1][0][720][720]);
  }
  if (dp[1][1][720][720] != -1) {
    res = min(res,dp[1][1][720][720]);
  }

  cout << "Case #" << tc << ": " << res << endl;
}

int main() {
  int T;
  cin >> T;
  FORE(tc,1,T) do_case(tc);
  return 0;
}