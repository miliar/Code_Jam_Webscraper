#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <numeric>
#include <iomanip>

using namespace std;
typedef unsigned long long ull;
void problem() {
  int d, n;
  cin >> d >> n;
  //vector<pair<int, int>> v;
  vector<double> v(n);
  for (int i = 0; i < n; ++i) {
    double k, s;
    cin >> k >> s;
    v[i] = ((d - k)/s);
  }

  double mx = *max_element(v.begin(), v.end());
 // cout << d << " " << n << " " << mx << " ";
  cout << std::fixed << setprecision(6) << (d / mx) << endl;
}

int main() {
  ifstream in("../../in");
  cin.rdbuf(in.rdbuf());

  int n;
  cin >> n;
  for (int i = 0; i < n; ++i) {
    cout << "Case #" << (i + 1) << ": ";
    problem();
  }

  return 0;
}