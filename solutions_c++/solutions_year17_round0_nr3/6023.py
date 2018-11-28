#include <queue>
#include <algorithm>
#include <iostream>
using namespace std;


struct tri {
  int lo, hi, size;
  bool operator <(const tri& src) const {
    return size < src.size;
  }
};

int main() {
  int T; cin >> T;
  for (int test = 1; test <= T; test++) {
    int N, K; cin >> N >> K;
    priority_queue<tri> q;
    
    q.push(tri {0, N + 1, N} );
    for (int k = 1; k < K; k++) {
      tri slot = q.top();
      if (slot.size <= 0) break;
      q.pop();
      int mid = (slot.lo + slot.hi) / 2;
      tri new_1 = tri { slot.lo, mid, mid - slot.lo - 1};
      tri new_2 = tri { mid, slot.hi, slot.hi - mid - 1};
      q.push(new_1);
      q.push(new_2);
    }
    tri slot = q.top();
    int mid = (slot.lo + slot.hi) / 2;
    int ls = mid - slot.lo - 1;
    int rs = slot.hi - mid - 1;
    cout << "Case #" << test << ": " << max(ls, rs) << " " << min(ls, rs) << endl;
  }
}