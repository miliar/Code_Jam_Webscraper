
#include <iostream>
#include <map>

using namespace std;

static void Calculate(long long N, long long K, long long& y, long long& z) {
  map<long long, long long> counts;
  counts.insert(make_pair(N, 1));
  while (true) {
    map<long long, long long>::reverse_iterator rit;
    rit = counts.rbegin();
    if (rit->second >= K) {
      long long a = rit->first - 1;
      z = a / 2;
      y = a - z;
      break;
    }
    long long num = rit->second;
    long long a = rit->first - 1;
    long long left = a / 2;
    long long right = a - left;
    map<long long, long long>::iterator it;
    counts.erase(--rit.base());
    if ((it = counts.find(left)) != counts.end()) {
      it->second += num;
    } else {
      counts.insert(make_pair(left, num));
    }
    if ((it = counts.find(right)) != counts.end()) {
      it->second += num;
    } else {
      counts.insert(make_pair(right, num));
    }
    K -= num;
  }
}

int main() {
  //{
  //  long long y = 0, z = 0;
  //  Calculate(4, 2, y, z);
  //}
  int T = 0;
  long long N = 0, K = 0;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    cin >> N >> K;
    long long y = 0, z = 0;
    Calculate(N, K, y, z);
    cout << "Case #" << (i + 1) << ": " << y << " " << z << endl;
  }
  return 0;
}