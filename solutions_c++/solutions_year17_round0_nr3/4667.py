#include <cstdio>
#include <set>
#include <iostream>

using namespace std;

struct ts {
  int i, sz;
  ts() { }
  ts(int I, int SZ): i(I), sz(SZ) { }
  int max() const {
    return sz/2;
  }
  int min() const {
    return sz/2 - ((sz&1)?0:1);
  }
  int mid() const {
    return i+sz/2-((sz&1)?0:1);
  }
  bool operator<(const ts& rhs) const{
    return this->min() > rhs.min() || (this->min() == rhs.min() &&(this->max() > rhs.max() || (this->max() == rhs.max() && this->i < rhs.i)));
  }
};

int main() {
  set<ts> tt; int t;
  scanf("%d", &t);
  int n, k;
  for(int cas = 1; cas <= t; ++cas) {
    scanf("%d %d", &n, &k);
    tt.clear();
    tt.insert(ts(0, n));
    for(int i = 1; i < k; ++i) {
      ts top = *tt.begin();
      tt.erase(top);
      if(top.min()) tt.insert(ts(top.i, top.min()));
      if(top.max()) tt.insert(ts(top.mid()+1, top.max()));
    }
    printf("Case #%d: %d %d\n", cas, tt.begin()->max(), tt.begin()->min());
  }
}