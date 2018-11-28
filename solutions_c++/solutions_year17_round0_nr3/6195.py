#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;

int main() {
  int t;
  cin >> t;
  for (int a = 0; a < t; a ++) {
    long long n,k;
    cin >> n >> k;

    vector<long long> space(k);
    make_heap(space.begin(), space.end());

    space.push_back(n);
    push_heap(space.begin(), space.end());

    for (long long i = 0; i < k; i++) {
      long long sp = space.front();
      // cout << i << "/" << sp << endl;
      pop_heap(space.begin(), space.end());
      space.pop_back();

      long long small = (sp - 1) / 2;
      long long big = sp - 1 - small;
      // cout << small << ":" << big << endl;
      if (i == k - 1) {
        cout << "Case #" << a+1 << ": " << big << " " << small <<endl;
        space.clear();
      } else {
        space.push_back(small);
        push_heap(space.begin(), space.end());
        space.push_back(big);
        push_heap(space.begin(), space.end());
      }
    }
  }
  return 0;
}
