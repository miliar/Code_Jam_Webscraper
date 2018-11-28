#include <iostream>
#include <map>

using namespace std;

typedef map<long, long> mll;

int main() {
  int T;
  cin >> T;
  for (int t = 0; t < T; t++) {

    long N, K;
    cin >> N >> K;
    mll fs;
    fs[N] = 1;

    pair<long, long> p;
    for (long k = 0; k < K; ) {
      p = *fs.rbegin();
      if (p.first % 2) {
        fs[p.first / 2] += 2 * p.second;
      } else {
        fs[p.first / 2] += p.second;
        fs[p.first / 2 - 1] += p.second;
      }
      fs.erase(p.first);
      k += p.second;
    }

    long y = p.first / 2;
    long z = p.first % 2 ? y : y-1;

    cout << "Case #" << (t + 1) << ": " << y << " " << z << endl;
  }

  return 0;
}
