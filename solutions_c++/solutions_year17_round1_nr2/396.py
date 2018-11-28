#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <string>
#include <utility>

using namespace std;
typedef long long ll;

template<typename T> T next() { T tmp; cin >> tmp; return tmp; }

struct pnt {
  ll b;
  int t;
  int num;
  int tp;
  bool operator<(pnt const & rhs) const {
    if (b == rhs.b) {
      if (t == rhs.t) {
        return num < rhs.num;
      }
      return t > rhs.t;
    }
    return b < rhs.b;
  }
};


void solve() {
  int n = next< int >();
  int p = next< int >();
  vector< ll > r(n);
  generate(r.begin(), r.end(), next<long long>);
  vector< pnt > events;
  vector< ll > qq(p);
  for (int i = 0; i < n; ++i) {
    
    generate(qq.begin(), qq.end(), next<ll>);
    sort(qq.begin(), qq.end());
    for (int j = 0; j < p; ++j) {
      ll left = (10 * qq[j] + 11 * r[i] - 1) / (11 * r[i]);
      ll right = (10 * qq[j]) / (9 * r[i]);
      if (left > right) {
        continue;
      }
      pnt b = {left, +1, j, i};
      pnt e = {right, -1, j, i};
      events.push_back(b);
      events.push_back(e);
      //cout << b.b << " " << e.b << " | ";
    }
    //cout << endl;
  }

  sort(events.begin(), events.end());
  int val = 0;
  vector<set< int >> story(n);
  for (auto pnt: events) {
    //cout << pnt.b << " " << pnt.t << " " << pnt.num << " " << pnt.tp << endl;
    if (pnt.t == -1) {
      if (story[pnt.tp].find(pnt.num) != story[pnt.tp].end()) {
        story[pnt.tp].erase(pnt.num);
      }
    } else {
      story[pnt.tp].insert(pnt.num);
      bool status = true;
      for (int i = 0; i < n; ++i) {
        status &= !story[i].empty();
      }
      if (status) {
        for (int i = 0; i < n; ++i) {
          int el = *story[i].begin();
          story[i].erase(el);
        } 
        val++;
      }
    }
  }
  cout << val << endl;


}

int main() {
  int n = next<int>();
  for (int i = 1; i <= n; ++i) {
    cout << "Case #" << i << ": ";
    solve();
  } 
  return 0;
}
