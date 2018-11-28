#include <vector>
#include <iostream>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <queue>

using namespace std;

struct Seg {
  int l = 0;
  int r = 0;
  int len() {
    return r-l;
  }
  Seg(int l_, int r_) : l(l_), r(r_) {}
};

void solve(int i) {
  cout << "Case #" << i+1 << ": ";
  int n, k;
  cin >> n >> k;
  auto cmp = [](Seg left, Seg right) { return left.len() < right.len() || (left.len() == right.len() && left.l < right.l); };
  priority_queue<Seg, vector<Seg>, decltype(cmp)> pq(cmp);
  pq.push(Seg(0, n));
  int ra, ri;
  for (int i=0; i<k; i++) {
    Seg tmp = pq.top();
    pq.pop();

    if (tmp.len()%2) {
      pq.emplace(tmp.l, tmp.l+tmp.len()/2);
      pq.emplace(tmp.l+tmp.len()/2+1, tmp.r);
      ra = ri = tmp.len()/2;
    } else {
      pq.emplace(tmp.l, tmp.l+tmp.len()/2-1);
      pq.emplace(tmp.l+tmp.len()/2, tmp.r);
      ra = tmp.len()/2;
      ri = tmp.len()/2-1;
    }
  }
  cout << ra << ' ' << ri << endl;
}

int main() {
  int T;
  cin >> T;
  for (int k=0; k<T; k++) {
    solve(k);
  }
  return 0;
}
