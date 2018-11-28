#include <iomanip>
#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
#include <functional>

using namespace std;

bool catchUpWith(unsigned long p,
                 unsigned long s,
                 unsigned long D,
                 unsigned long sp,
                 double ss,
                 double sd) {
  double cT = (D - p) / (double)s;
  double sT = (sd - sp) / ss;
  return cT < sT;
}

double calc(unsigned long sp,
            double ss,
            double sd) {
  return sd / (sd - sp) * ss;
}

int main() {
  int num;
  cin >> num;
  for (int i = 1; i <= num; i++) {
    unsigned long D, N;
    unsigned long p, s;
    unsigned long sp;
    double ss, sd;
    double res = numeric_limits<double>::max();
    cin >> D >> N;
    vector<pair<unsigned long, unsigned long> > arr;
    sp = sd = D;
    ss = 1;
    for (int j = 0; j < N; j++) {
      cin >> p >> s;
      arr.push_back(make_pair(p, s));
    }
    sort(arr.begin(), arr.end(), [](pair<unsigned long, unsigned long>& a, pair<unsigned long, unsigned long>& b) {
      return a.first > b.first;
    });

    for (auto c : arr) {
      p = c.first;
      s = c.second;
      if (catchUpWith(p, s, D, sp, ss, sd)) {
        double t = (sp - p) / (s - ss);
        if (t < 0) {
          throw new runtime_error("t should not be less than 0");
        }
        sp = p;
        ss = s;
        sd = sp + t * ss;
      } else {
        sp = p;
        ss = s;
        sd = D;
      }
      res = min(res, calc(sp, ss, sd));
    }
    cout << fixed << setprecision(6);
    cout << "Case #" << i << ": " << res << endl;
  }
  return 0;
}
