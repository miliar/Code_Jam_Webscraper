#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef vector <long long int>::iterator vlli;

int main() {
  ios_base::sync_with_stdio(0);
  long long int T;
  cin >> T;
  for (long long int t = 1; t <= T; t++) {
    long long int n, k;
    cin >> n >> k;
    vector<long long int> v;
    v.push_back(n);
    while (k > 1) {
      vlli it = max_element(v.begin(), v.end());
      long long int max = *it;
      v.erase(it);
      long long int l, r;
      l = (max - 1) / 2;
      r = max - 1 - l;
      v.push_back(l);
      v.push_back(r);
      k--;
    }
    long long int max, min;
    max = *max_element(v.begin(), v.end());
    int r, l;
    l = (max - 1) / 2;
    r = max - 1 - l;
    printf("Case #%lld: %d %d\n", t, r, l);
  }
  return 0;
}