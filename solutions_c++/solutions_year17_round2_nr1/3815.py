#include <vector>
#include <string>
#include <set>
#include <algorithm>
#include <map>
#include <iostream>
#include <fstream>
#include <unordered_map>
#include <queue>
#include <set>
#include <iomanip>
using namespace std;
typedef unsigned long long ull;

//ifstream fin("A-small-attempt2.in");
//ofstream fout("A-small.out");

ifstream fin("A-large.in");
ofstream fout("A-large.out");

void task() {
  double d = 0.;
  ull n = 0;
  fin >> d >> n;

  vector<vector<double>> v(n, vector<double>(3));

  for (ull i = 0; i < n; ++i) {
    fin >> v[i][0] >> v[i][1];
  }

  sort(v.begin(), v.end());
  double tmax = 0., t = 0.;

  for (ull i = 0; i < n; ++i) {

    tmax = max(tmax, abs(d - v[i][0]) / v[i][1]);
    t = tmax;
    for (ull j = i + 1; j < n; ++j) {
      double k1 = abs((d - v[i][0]) - (d - v[j][0]));
      double k2 = abs(v[j][1] - v[i][1]);
      if (v[j][1] != v[i][1])
        t = k1 / k2;
      double t2 = (d - (v[j][0] + v[j][1] * t)) / v[j][1];
      tmax = max(tmax, t + t2);
    }
  }

  double speed = d / tmax;

  fout << fixed << setprecision(6) << speed;
}

int main() {

  long long t = 0;
  fin >> t;

  for (long long i = 0; i < t; i++) {
    fout << "case #" << i + 1 << ": ";
    task();
    fout << endl;
    cout << i + 1 << endl;
  }
  fout.close();
  cout << "OK";
  return 0;
}