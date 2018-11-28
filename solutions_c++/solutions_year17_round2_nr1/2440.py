#include <iostream>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <cstdio>

using namespace std;

int main()
{
  int T;

  cin >> T;
  for (int i = 1; i <= T; ++i) {
    int D, N;

    cin >> D >> N;
    int Ki, Si;
    double timeI, timeMax = 0.0;
    while (N--) {
      cin >> Ki >> Si;
      timeI = (double) (D-Ki)/Si;
      if (timeI > timeMax)
        timeMax = timeI;
    }

    printf("Case #%d: %.6f\n", i, (double) D/timeMax);
  }

  return 0;
}
