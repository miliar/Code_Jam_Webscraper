#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  int tests; cin >> tests;
  for(int test = 0; test<tests; ++test) {
    int n, k;
    cin >> n >> k;
    double u; cin >> u;
    vector<double> ps;
    for(int i = 0; i<n; ++i) {
      double p;
      cin >> p;
      ps.push_back(p);
    }
    sort(ps.begin(), ps.end());
    for(int i = 1; i<n; ++i) {
      if(u > (i * (ps[i] - ps[i-1]))) {
        // yay we won't run out of u yet
        u -= i * (ps[i] - ps[i-1]);
        for(int j = 0; j<i; ++j) {
          ps[j] += (ps[i] - ps[i-1]);
        }
      }
      else {
        // use up all of u
        for(int j = 0; j<i; ++j) {
          ps[j] += u / i;
        }
        u = 0;
      }
    }
    if(u > 0) {
      for(int j = 0; j<n; ++j) {
        ps[j] += u/n;
      }
    }

    double totalprob = 1;
    for(int i = 0; i<n; ++i) {
      totalprob *= ps[i];
    }

    cout << fixed << "Case #" << test+1 << ": " << totalprob << endl;
  }
}
