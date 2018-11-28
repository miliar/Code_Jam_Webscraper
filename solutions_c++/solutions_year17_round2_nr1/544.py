#include <algorithm>
#include <iostream>
#include <iterator>
#include <vector>

using namespace std;

struct Horse {
  int64_t k, s;

  double timeTo(int64_t d) const {
    return (d - k) / double(s);
  }

};

istream& operator >> (istream& is, Horse& horse) {
  return is >> horse.k >> horse.s;
}

void solve() {
  int d, n;
  cin >> d >> n;
  vector<Horse> horses(n);
  copy_n(istream_iterator<Horse>(cin), n, horses.begin());
  double timeNeeded = 0;
  for(const Horse& horse: horses){
    timeNeeded = max(timeNeeded, horse.timeTo(d));
  }
  cout << d / timeNeeded << endl;
}

int main() {
  cout.setf(ios::fixed);
  cout.precision(12);
  int tests;
  cin >> tests;
  for(int test = 1; test <= tests; ++test){
    cout << "Case #" << test << ": ";
    solve();
  }
}
