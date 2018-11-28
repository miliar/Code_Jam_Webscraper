#include <iostream>
#include <map>
#include <algorithm>
using namespace std;

int main() {
  long long t, n, k, l, r, c;
  std::map<long long, long long>::reverse_iterator x;
  cin >> t;
  for(int nr = 1; nr <= t; nr ++) {
    map<long long, long long> m;
    cin >> n >> k;
    m[n] = 1;
    int g = 0;
    while(k > 0) {
      g ++;
      x = m.rbegin();
      c = x->second;
      l = (x->first - 1) / 2;
      r = x->first - l - 1;
      m.erase(x->first);
      k -= c;
      m[l] = m[l] + c;
      m[r] = m[r] + c;
      
    }
    cout << "Case #" << nr <<": " << max(l, r) << " " << min(l, r) << endl;
  }
  
}
