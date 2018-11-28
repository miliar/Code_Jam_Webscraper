#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <limits>
#include <list>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <cmath>

using namespace std;

int INF = std::numeric_limits<int>().max();
double INFD = std::numeric_limits<double>().max();

double PI = acos(-1);

struct Range {
  Range(long long l, long long r) {
    L_s = l;
    R_s = r;
  }

  long long L_s, R_s;

  void Split(Range& left, Range& right) {
    if (L_s % 2) {  // odd amount of empty stalls on the left.
      left.L_s = left.R_s = (L_s - 1) / 2;
    } else {
      left.L_s = (L_s / 2) - 1;
      left.R_s = L_s / 2;
    }
    if (R_s % 2) {  // odd amount of empty stalls on the right.
      right.L_s = right.R_s = (R_s - 1) / 2;
    } else {
      right.L_s = (R_s / 2) - 1;
      right.R_s = R_s / 2;
    }
  }

  string ToString() {
    stringstream s;
    s << L_s << ", " << R_s;
    return s.str();
  }

  bool operator<(const Range& other) const {
    if (min(L_s, R_s) == min(other.L_s, other.R_s)) {
      return max(L_s, R_s) < max(other.L_s, other.R_s);
    }
    return min(L_s, R_s) < min(other.L_s, other.R_s);
  }
};

Range MahBFS(long long n, long long k) {
  priority_queue<Range> q;
  if (n % 2) {
    q.push(Range(n / 2, n / 2));
  } else {
    q.push(Range(n / 2 - 1, n / 2));
  }
  map<Range, long long> mem;
  mem[q.top()] = 1;
  while (true) {
    Range curr = q.top();
    //cerr << "At " << curr.ToString() << endl;
    q.pop();
    if (mem[curr] >= k) {
      return curr;
    }
    k -= mem[curr];
    Range l(0, 0), r(0, 0);
    curr.Split(l, r);
    if(!mem.count(l)) {
      q.push(l);
    }
    mem[l] += mem[curr];
    if(!mem.count(r)) {
      q.push(r);
    }
    mem[r] += mem[curr];
    //cerr << "\tGoing to Left: " << l.ToString()
         //<< " and Right: " << r.ToString() << endl;
    //mem.erase(curr);
  }
  return Range(0, 0);
}

int main() {
  ios::sync_with_stdio(false);
  int t = 0, q = 0;
  cin >> t;
  while (q < t) {
    long long n = 0, k = 0;
    cin >> n >> k;
    Range r = MahBFS(n, k);
    cout << "Case #" << ++q << ": " << max(r.L_s, r.R_s) << " "
         << min(r.L_s, r.R_s) << endl;
  }
  return 0;
}
