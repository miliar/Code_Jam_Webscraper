#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <utility>
using namespace std;

int main() {
  long long t;
  cin >> t;
  cout << setprecision(6) << fixed;
  for (long long i = 0; i < t; i++) {
    long long n,d;
    cin >> d >> n;
    vector<pair<long long,long long> > horses;
    for (int j = 0; j < n; j++) {
      int ki,si;
      cin >> ki >> si;
      horses.push_back(make_pair(ki, si));
    }
    double maxtime = -1;
    for (long long j = 0; j < n; j++) {
      maxtime = max(maxtime, (d - horses[j].first) * 1.0 / horses[j].second);
    }
    cout << "Case #" << i + 1 << ": " << d * 1.0/maxtime << endl;
  }
}
