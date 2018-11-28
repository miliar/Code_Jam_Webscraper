#include <algorithm>
#include <cassert>
#include <cstring>
#include <iostream>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define TRACE(x) cout << #x << " = " << x << endl
#define _ << " _ " <<

typedef long long llint;

const string NO = "IMPOSSIBLE";

string mul(string s, int k) {
  string ret = "";
  REP(i, k) ret += s;
  return ret;
}

string solveEasy(int R, int B, int Y) {
  int x[3] = {R, B, Y};
  string ch[3] = {"R", "B", "Y"};
  
  int N = x[0] + x[1] + x[2];
  if (N == 1) {
    REP(i, 3) {
      if (x[i] == 1) return ch[i];
    }
    assert(false);
  }

  if (N == 2) {
    REP(i, 3) REP(j, i) {
      if (x[i] == 1 && x[j] == 1) return ch[i] + ch[j];
    }
    return NO;
  }
  
  assert(N >= 3);

  int i = max_element(x, x + 3) - x;
  if (x[i] > N/2) return NO;

  string ret = ch[i];
  x[i]--;
  while (x[i] > 0) {
    int j = (i + 1) % 3;
    int k = (i + 2) % 3;

    if (x[j] < x[k]) swap(j, k);
    if (x[j] == 0) return NO;
    ret += ch[j] + ch[i];
    x[j]--, x[i]--;
  }

  int j = (i + 1) % 3;
  int k = (i + 2) % 3;
  if (x[j] < x[k]) swap(j, k);
  
  if (x[j] > x[k]) {
    ret += ch[j];
    x[j]--;
  }
  if (x[j] != x[k]) return NO;
  ret += mul(ch[k] + ch[j], x[j]);
  return ret;
}

string solve(int R, int B, int Y, int RY, int BY, int RB) {
  if (R == BY && B+Y+RY+RB == 0) return mul("RG", R);
  if (B == RY && R+Y+BY+RB == 0) return mul("BO", B);
  if (Y == RB && B+R+RY+BY == 0) return mul("YV", Y);
  
  if (RY > B || BY > R || RB > Y) return NO;
  B -= RY, R -= BY, Y -= RB;

  if (RY > 0 && B == 0) return NO;
  if (BY > 0 && R == 0) return NO;
  if (RB > 0 && Y == 0) return NO;
  
  int N = R + B + Y;
  string ans = solveEasy(R, B, Y);
  if (ans == NO) return NO;

  string ret;
  REP(i, N) {
    ret.push_back(ans[i]);
    if (ans[i] == 'R' && BY > 0) {
      REP(j, BY) ret += "GR";
      BY = 0;
    }
    if (ans[i] == 'B' && RY > 0) {
      REP(j, BY) ret += "OB";
      RY = 0;
    }
    if (ans[i] == 'Y' && RB > 0) {
      REP(j, BY) ret += "VY";
      RB = 0;
    }
  }
  assert(RY == 0 && BY == 0 && RB == 0);
  return ret;
}

int main(void) {
  int TC;
  scanf("%d", &TC);
  for (int tp = 1; tp <= TC; ++tp, fflush(stdout)) {
    int N, R, O, Y, G, B, V;
    scanf("%d %d %d %d %d %d %d", &N, &R, &O, &Y, &G, &B, &V);

    string ans = solve(R, B, Y, O, G, V);
    printf("Case #%d: ", tp);
    puts(ans.c_str());
  }
  return 0;
}
