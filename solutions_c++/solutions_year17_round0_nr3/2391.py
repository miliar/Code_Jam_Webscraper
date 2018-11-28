#include <cmath>
#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <map>
using namespace std;

fstream in, out;

int T;
long long N, K;
long long next_K;

struct comp {
  bool operator() (const long long &a, const long long & b) const {return a > b;}
};

map<long long, long long, comp> sizes;

int main() {
  in.open("C-large.in", fstream::in);
  out.open("probc-large.out", fstream::out);

  in >> T;
  for (int i = 0; i < T; i++) {
    in >> N >> K;
    next_K = 0;
    sizes.clear();
    sizes[N] = 1;

    long long ans;
    while (next_K < K) {
      auto it = sizes.begin();
      long long num = it->first;
      long long size = it->second;
      next_K += size;
      //      cout << num << " " << size << " " << next_K << endl;

      if (next_K >= K) {
        ans = num;
      } else {
        sizes.erase(it);
        if (num % 2 == 0) {
          if (sizes.count(num / 2) == 0) {
            sizes[num / 2] = size;
          } else {
            sizes[num / 2] = sizes[num/2] + size;
          }

          if (sizes.count(num / 2 - 1) == 0) {
            sizes[num / 2 - 1] = size;
          } else {       
            sizes[num / 2 - 1] = sizes[num / 2] + size;
          }
        } else {
          if (sizes.count(num / 2) == 0) {
            sizes[num / 2] = 2 * size;
          } else {
            sizes[num / 2] = sizes[num/2] + 2 * size;
          }
        }
      }
    }

    long long ans1 = ans / 2;
    long long ans2;
    if (ans % 2 == 0) {
      ans2 = ans / 2 - 1;
    } else {
      ans2 = ans / 2;
    }

    //    cout << "AAA " << i << " " << ans << " " << ans1 << " " << ans2 << endl;
    
    out << "Case #" << i + 1 << ": " << ans1 << " " << ans2 << endl;
  }
    
  in.close();
  out.close();
  return 0;
}
