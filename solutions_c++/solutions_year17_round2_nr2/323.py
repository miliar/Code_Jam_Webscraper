#include <cstdio>
#include <cstring>
#include <cassert>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR (i, 0, n)
#define _ << " _ " <<
#define TRACE(x) cerr << #x << " = " << x << endl
#define debug(...) fprintf(stderr, __VA_ARGS__)
#define debug
#define TRACE(x)

using namespace std;

typedef long long llint;

const int MAXN = 1010;
const char CHR[] = {'R', 'Y', 'B'};

int r, g, b, cnt[3], n;
int o, y, v;
vector<char> s[MAXN];

void solve_small(int tc) {
  printf("Case #%d: ",tc);
  REP(i, MAXN) s[i].clear();
  cnt[0] = r; cnt[1] = y; cnt[2] = b;
  debug("\n");
  TRACE(cnt[0] _ cnt[1] _ cnt[2]);
  REP(i, 3)
    if (cnt[i] == max(max(r, y), b)) {
      int ot = r + y + b - cnt[i];
      if (ot < cnt[i]) {
	printf("IMPOSSIBLE\n");
	return;
      }
      REP(j, cnt[i]) s[j].push_back(CHR[i]);
      REP(col, 3) {
	if (col == i) continue;
	REP(x, cnt[col]) {
	  int pos = -1;
	
	  REP(j, cnt[i])
	    if ((int)s[j].size() == 1)
	      pos = j;
	  REP(j, cnt[i])
	    if (pos == -1 && s[j].back() != CHR[col])
	      pos = j;

	  assert(pos != -1);
	  s[pos].push_back(CHR[col]);
	  TRACE(col _ pos);
	}
      }
      REP(j, cnt[i])
	for (char chr : s[j])
	  printf("%c",chr);
      printf("\n");
      return;
    }
}

void solve(int tc) {
  scanf("%d",&n);
  scanf("%d %d %d",&r,&o,&y);
  scanf("%d %d %d",&g,&b,&v);

  solve_small(tc);
}

int main(void) {
  int tc;
  scanf("%d",&tc);
  REP(it, tc) {
    solve(it+1);
  }
  
  return 0;
}
