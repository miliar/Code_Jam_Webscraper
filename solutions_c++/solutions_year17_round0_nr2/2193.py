#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <iostream>
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

int max_depth = 18;

struct Node {
  void Span(int prev_largest, int depth) {
    if (depth == max_depth) {
      return;
    }
    while (prev_largest <= 9) {
      children['0' + prev_largest] = new Node();
      children['0' + prev_largest]->Span(prev_largest, depth + 1);
      prev_largest++;
    }
  }
  long long Count(bool not_first) {
    // if(s.size()) {
    // cout << s << endl;
    //}
    long long res = not_first;
    for (auto& c : children) {
      res += c.second->Count(true);
    }
    return res;
  }
  void Nice(set<long long>& nums, long long num) {
    if (num) {
      nums.insert(num);
    }
    for (auto& c : children) {
      c.second->Nice(nums, (num * 10) + (c.first - '0'));
    }
  }
  map<char, Node*> children;
};

int main() {
  ios::sync_with_stdio(false);
  set<long long> nums;
  {
    Node n;
    n.Span(1, 0);
    n.Nice(nums, 0);
  }
  int t = 0, q = 0;
  cin >> t;
  while (q < t) {
    long long x = 0;
    cin >> x;
    auto it = nums.upper_bound(x);
    --it;
    cout << "Case #" << ++q << ": " << *it << endl;
  }
  return 0;
}
