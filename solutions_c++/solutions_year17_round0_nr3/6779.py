#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <numeric>
using namespace std;

int main() {
    int caseN = 0;
    cin >> caseN;
    for (int tcas = 1; tcas <= caseN; ++tcas) {
      int N, K;
      cin >> N >> K;
      map<int, int> counts;
      counts.insert(make_pair(N, 1));
      int A, B;
      while (K) {
        auto large = --counts.end();
        int reduce = min(large->second, K);
        counts[large->first] -= reduce;
        K -= reduce;
        if (large->first & 1) {
          counts[large->first / 2] += 2 * reduce;
          A = B = large->first / 2;
        } else {
          counts[large->first / 2] += reduce;
          counts[large->first / 2 - 1] += reduce;
          A = large->first / 2;
          B = A - 1;
        }
        if (large->second == 0) {
          counts.erase(large);
        }
      }
      cout << "Case #" << tcas << ": " << A << " " << B << endl;
    }

}
