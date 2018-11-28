#include<iostream>
#include<sstream>
#include<vector>
#include<algorithm>
#include<cmath>
#include <iomanip>

using namespace std;

int main()
{
  cout.setf(ios::fixed);
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t)
  {
    int D, N;
    cin >> D >> N;
    vector<int> positions = vector<int>(N, 0);
    vector<int> speeds = vector<int>(N, 0);

    for (int i = 0; i < N; ++i) {
      cin >> positions[i];
      cin >> speeds[i];
    }

    // vector<int> ttt = vector<int>(N, 0);
    vector<double> tnc = vector<double>(N, 0);
    for (int i = 0; i < N; ++i) {
      tnc[i] = (double)((double) D * (double) speeds[i]) / (double)(D - positions[i]);
    }
    double minV = -1;
    for (int i = 0; i < N; ++i) {
      if (minV == -1) minV = tnc[i];
      if (minV > tnc[i]) minV = tnc[i];
    }

    double sol = minV;

    cout << setprecision(6) << "Case #" << t << ": " << sol << endl;
  }
  return 0;
}
