#include <cstdio>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

#define TRACE(x) cerr << #x << " = " << x << endl
#define REP(i, n) for (int i=0; i<n; i++)
#define FOR(i, a, b) for (int i=(a); i<(b); i++)
#define _ << " " <<

typedef long long ll;
typedef pair<int, int> P;
#define X first
#define Y second

const int MAX = 1005;

int poredak[MAX];
int cnt[8], poc[8];
char slova[8] = "ROYGBV";
int jedan[6] = {1, 0, 1, 0, 1, 0};
int komp[6] = {3, -1, 5, -1, 1, -1};
vector <string> V[6];  
string sol;

void go(int ind, int prvi) {
  assert(!V[ind].empty());
  string tmp = V[ind].back();
  V[ind].pop_back();
  for (auto it : tmp) sol.push_back(it);

  //  TRACE(ind);  
  int mx = -1, koji = -1;
  REP(i, 6) {
    if (i != ind && !V[i].empty() && (int) ((i == prvi) + V[i].size()) > mx) {
      mx = (i == prvi) + (int) V[i].size();
      koji = i;
    }
  }

  if (koji != -1 && !V[koji].empty())
    go(koji, prvi);
}

int indsl(char c) {
  REP(i, 6) if (slova[i] == c) return i;
  assert(0);
}

void solve() {
  sol = "";
  REP(i, 6) V[i].clear();

  int sve = 0;
  REP(i, 6) sve += cnt[i];

  REP(i, 6) {
    if (!jedan[i]) continue;
    if (cnt[komp[i]] + cnt[i] == sve) {
      if (cnt[komp[i]] != cnt[i]) {
	printf("IMPOSSIBLE\n");
	return;
      }

      REP(j, cnt[i]) {
	sol.push_back(slova[i]);
	sol.push_back(slova[komp[i]]);
      }

      printf("%s\n", sol.c_str());
      return;
    }

    if (cnt[komp[i]] && cnt[i] < cnt[komp[i]] + 1) {
      //      TRACE(i _ cnt[i] _ cnt[komp[i]]);
      printf("IMPOSSIBLE\n");
      return;
    }
    
    if (cnt[komp[i]]) {
      string tmp = "";
      tmp.push_back(slova[i]);
      cnt[i]--;
      for (; cnt[komp[i]]; ) {
	tmp.push_back(slova[komp[i]]);
	tmp.push_back(slova[i]);
	cnt[i]--;
	cnt[komp[i]]--;
      }

      V[i].push_back(tmp);
    }

    //    TRACE(i _ cnt[i]);

    for (; cnt[i]; cnt[i]--) {
      string a = ""; a.push_back(slova[i]);
      V[i].push_back(a);
    }
  }

  int mx = 0, uk = 0;
  REP(i, 6) {
    if (V[i].size() > V[mx].size())
      mx = i;
    uk += (int) V[i].size();
  }
  
  //  TRACE(mx _ uk);
  if (2 * (int) V[mx].size() > uk) {
    printf("IMPOSSIBLE\n");
    return;      
  }

  go(mx, mx);
  assert(sol[0] != sol.back());
  assert((int) sol.size() == sve);
  
  REP(i, sve) {
    int a = indsl(sol[i]);
    int b = indsl(sol[(i+1)%sve]);
    assert(a != b);
    assert(jedan[a] + jedan[b]);
    if (jedan[a] + jedan[b] == 1) {
      if (jedan[a]) assert(b == komp[a]);
      if (jedan[b]) assert(a == komp[b]);
    }
  }

  printf("%s\n", sol.c_str());
}

int main()
{
  int brt;
  scanf("%d", &brt);
  
  REP(tt, brt) {
    int n;
    scanf("%d", &n);

    REP(i, 6) scanf("%d", &cnt[i]);
    memcpy(poc, cnt, sizeof cnt);
    
    //    REP(i, 6) if (!jedan[i]) assert(!cnt[i]);

    printf("Case #%d: ", tt+1);
    solve();
  }

  return 0;
}
