#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
#include <cfloat>
#include <iomanip>

#define REP(a,b) for(int a=0;a<(b);a++)
#define PER(a,b) for(int a=(b)-1;a>=0;a--)
#define ll long long

using namespace std;

int main() {
  int T;
  cin >> T;
  assert(cin);

  REP(tcase, T) {
    int D, N;
    assert(cin >> D);
    assert(cin >> N);

    double min = DBL_MAX;

    for (int i = 0; i < N; ++i) {
      int Ki, Si;
      assert(cin >> Ki);
      assert(cin >> Si);
      double speed = (Si * double(D)) / (D - Ki);
      if (speed < min)
        min = speed;
    }

    cout << "Case #" << tcase + 1 << ": "
         << std::fixed << std::setprecision(6) << min << std::endl;
  }

  return 0;
}
