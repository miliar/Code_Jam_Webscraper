#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main () {
  long long t;
  cin >> t;
  double d, n;
  for (int k = 0; k < t; k++) {
    cin >> d >> n;
    double pos, spe;
    double maxtime = 0, curtime = 0;
    for (int j = 0; j < n; j++) {
      cin >> pos >> spe;
      curtime = (d - pos) / spe;
      if (curtime > maxtime) {
	maxtime = curtime;
      }
    }
    printf("Case #%d: %.6lf\n", k+1, d/maxtime);
  }
  return 0;
}