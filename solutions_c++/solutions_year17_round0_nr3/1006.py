#include <iostream>
#include <map>
using namespace std;

int main() {
  int t; cin >> t;
  for (int c = 1; c <= t; c++) {
    long long n, k; cin >> n >> k;
    map<long long, long long> m; m[-n] = 1;
    long long y, z;
    while (k > 0) {
      map<long long, long long>::iterator it = m.begin();
      long long s = it->first, v = it->second;

      y = (-s-1)/2; m[-y] += v;
      z = -s/2; m[-z] += v;

      m.erase(it);
      k -= v;
    }
    cout << "Case #" << c << ": " << z << " " << y << endl;
  }
  return 0;
}
