#include <cstdio>
#include <vector>
#include <climits>

using namespace std;

struct ts {
  int l, r, type;
  ts() { }
  ts(int L, int R, int Type): l(L), r(R), type(Type) { }
  bool operator<(const ts& rhs) const {
    return l < rhs.l;
  }
};

struct tt {
  int len, tl, tr;
  tt() { }
  tt(int Len, int TL, int TR): len(Len), tl(TL), tr(TR) { }
};
vector<ts> seq;
vector<tt> trans;

int a[2], cnt[2], memo[301][721][721];
int go(int i = 0, int j = cnt[0], int k = cnt[1]) {
    if(memo[i][j][k] != -1) return memo[i][j][k];
    if(i == trans.size()) return memo[i][j][k] = 0;
    memo[i][j][k] = INT_MAX;
    if(j >= trans[i].len) {
      int t = 2;
      if(trans[i].tl == 0) --t;
      if(trans[i].tr == 0) --t;
      memo[i][j][k] = min(memo[i][j][k], t + go(i+1, j - trans[i].len, k));
    } else {
      if(trans[i].tl == trans[i].tr) memo[i][j][k] = min(memo[i][j][k], 2 + go(i+1, 0, k - trans[i].len + j));
      else memo[i][j][k] = min(memo[i][j][k], 1 + go(i+1, 0, k - trans[i].len + j));
    }
    if(k >= trans[i].len) {
      int t = 2;
      if(trans[i].tl == 1) --t;
      if(trans[i].tr == 1) --t;
      memo[i][j][k] = min(memo[i][j][k], t + go(i+1, j, k - trans[i].len));
    } else {
      if(trans[i].tl == trans[i].tr) memo[i][j][k] = min(memo[i][j][k], 2 + go(i+1, j - trans[i].len + k, 0));
      else memo[i][j][k] = min(memo[i][j][k], 1 + go(i+1, j - trans[i].len + k, 0));
    }
    return memo[i][j][k];
}

int main() {
  int t; scanf("%d", &t);
  int l, r;
  for(int cas = 1; cas <= t; ++cas) {
    for(int i = 0; i < 2; ++i) scanf("%d", a + i);
    seq.clear();
    for(int i = 0; i < 2; ++i)
      for(int j = 0; j < a[i]; ++j) {
        scanf("%d %d", &l, &r);
        seq.push_back(ts(l, r, i));
      }
    sort(seq.begin(), seq.end());
    cnt[0] = cnt[1] = 720;
    for(auto i: seq)
      cnt[1 - i.type] -= (i.r - i.l);
    trans.clear();
    int t = 0;
    for(int i = 0; i < seq.size()-1; ++i)
      if(seq[i+1].l - seq[i].r)
        trans.push_back(tt(seq[i+1].l - seq[i].r, 1-seq[i].type, 1-seq[i+1].type));
      else if(seq[i+1].type != seq[i].type)
        ++t;
    if(1440 - seq[seq.size()-1].r + seq[0].l)
      trans.push_back(tt(1440 - seq[seq.size()-1].r + seq[0].l, 1-seq[seq.size()-1].type, 1-seq[0].type));
    else if(seq[seq.size()-1].type != seq[0].type)
      ++t;
    // for(auto i: trans) printf("%d %d %d\n", i.len, i.tl, i.tr);
    // printf("%d %d\n", cnt[0], cnt[1]);
    memset(memo, -1, sizeof memo);
    printf("Case #%d: %d\n", cas, go() + t);
  }
  return 0;
}