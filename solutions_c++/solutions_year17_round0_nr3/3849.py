#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

struct Space {
  unsigned long long l, r;

  bool operator() (const Space& left, const Space& right) const {
    if (left.distance() != right.distance()) {
      return left.distance() < right.distance();
    } else {
      return left.l < right.l;
    }
  }

  unsigned long long distance() const {
    return r - l;
  }
};


int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int t, i;
  cin >> t;
  string s;
  unsigned long long n, k, ans_max, ans_min, middle,ll,rr;
  Space space;
  for (int _case = 1; _case <= t; _case++) {
    priority_queue<Space, std::vector<Space>, Space> pq;
    cin >> n >> k;
    space.l = 1;
    space.r = n;
    pq.push(space);

    if (k == n) {
      ans_max = ans_min = 0;
    } else {
      Space l,r;
      for (int i = 0; i < k-1; i++) {
        space = pq.top();
        pq.pop();
        middle = space.l + (space.r - space.l)/ 2;
        l.l = space.l;
        l.r = middle-1;
        r.l = middle+1;
        r.r = space.r;
        if (l.l <= l.r) {
          pq.push(l);
        }
        if (r.l <= r.r) {
          pq.push(r);
        }
      }
      space = pq.top();
      middle = space.l + (space.r - space.l)/ 2;
      //cout << space.l << " " << middle << " " << space.r;
      ll = middle - space.l;
      rr = space.r - middle;

      ans_max = max(ll, rr);
      ans_min = min(ll, rr);
    }
    cout << "Case #" << _case << ": " << ans_max << " " << ans_min << "\n";
  }
  return 0;
}
