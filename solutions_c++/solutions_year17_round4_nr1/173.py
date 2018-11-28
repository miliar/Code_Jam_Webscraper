#include <cstring>
#include <queue>
#define REP(i,n) for(int i=0; i<(int)(n); i++)

#include <cstdio>
inline int getInt(){ int s; scanf("%d", &s); return s; }

#include <set>

using namespace std;

vector<vector<vector<vector<vector<int> > > > > memo;
int p;

int solve(int n, int p0, int p1, int p2, int p3) {
  if(p0 + p1 + p2 + p3 == 0) return 0;
  if(memo[n][p0][p1][p2][p3] != -1) return memo[n][p0][p1][p2][p3];

  int ret = 0;

  if(p0) ret = max(ret, (n == 0 ? 1 : 0) + solve((n + 0) % p, p0 - 1, p1, p2, p3));
  if(p1) ret = max(ret, (n == 0 ? 1 : 0) + solve((n + p - 1 % p) % p, p0, p1 - 1, p2, p3));
  if(p2) ret = max(ret, (n == 0 ? 1 : 0) + solve((n + p - 2 % p) % p, p0, p1, p2 - 1, p3));
  if(p3) ret = max(ret, (n == 0 ? 1 : 0) + solve((n + p - 3 % p) % p, p0, p1, p2, p3 - 1));

  // printf("%d %d %d %d %d: %d\n", n, p0, p1, p2, p3, ret);
  return memo[n][p0][p1][p2][p3] = ret;
}

int main(){
  const int t = getInt();

  REP(cc,t) {
    const int n = getInt();
    const int p = ::p = getInt();
    vector<int> cnt(4);
    REP(i,n) cnt[getInt() % p]++;

    memo = vector<vector<vector<vector<vector<int> > > > >(p,
      vector<vector<vector<vector<int> > > >(cnt[0] + 1,
        vector<vector<vector<int> > >(cnt[1] + 1,
          vector<vector<int> >(cnt[2] + 1,
            vector<int>(cnt[3] + 1, -1)))));

    printf("Case #%d: %d\n", cc + 1, solve(0, cnt[0], cnt[1], cnt[2], cnt[3]));
  }

  return 0;
}
