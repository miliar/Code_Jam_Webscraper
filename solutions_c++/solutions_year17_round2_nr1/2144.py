#include <iostream>
#include <string>
#include <set>
#include <map>
#include <iomanip>      // std::setprecision

using namespace std;

int main() {
  int t;
  cin >> t;

  for (int i = 0; i < t; i++) {
    int d, n;
    cin >> d >> n;

    double maxTime = 0;
    for (int j = 0; j < n; j++) {
      int k, s;
      cin >> k >> s;

      int dist = d - k;
      double time = ((double)dist) / ((double)s);
      if (time > maxTime)
        maxTime = time;
    }

    double speed = ((double)d) / maxTime;
    cout << setprecision(15);
    cout << "Case #" << i + 1 << ": " << speed << endl;
  }
}
