#include<iostream>
#include<sstream>
#include<vector>
#include<algorithm>
#include<cmath>
#include<iomanip>

using namespace std;

double calcTopSurface(int r) {
  return M_PI*r*r;
}

double calcSideSurface(int r, int h) {
  return 2*M_PI*r*h;
}

bool comp (pair<int, int> a, pair<int, int> b) {
  return (a.first > b.first);
}

bool comp2 (pair<int, int> a, pair<int, int> b) {
  // return (a.second > b.second);
  return (calcSideSurface(a.first, a.second) > calcSideSurface(b.first, b.second));
}

int main()
{
  cout.setf(ios::fixed);
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t)
  {
    int N, K;
    cin >> N >> K;
    vector<int> r = vector<int>(N);
    vector<int> h = vector<int>(N);
    vector<pair<int, int> > p = vector<pair<int, int> > (N);
    for (int i = 0; i < N; ++i) {
      cin >> p[i].first >> p[i].second;
    }
    double totalSurface = -1.0;

    vector<double> sol = vector<double>(N - K + 1, 0);


    sort(p.begin(), p.end(), comp);


    for (int i = 0; i < N - K + 1; ++i) {
      sol[i] = calcTopSurface(p[i].first);
      sol[i] += calcSideSurface(p[i].first, p[i].second);
      if (i == N - 1) continue;
      vector<pair<int, int > >::const_iterator first = p.begin() + i + 1;
      vector<pair<int, int > >::const_iterator last = p.end();
      vector<pair<int, int > > validPancakes(first, last);

      sort(validPancakes.begin(), validPancakes.end(), comp2);
      for (int j = 0; j < K - 1; ++j) {
        sol[i] += calcSideSurface(validPancakes[j].first, validPancakes[j].second);
      }
    }

    for (int i = 0; i < N - K + 1; ++i) {
      if (sol[i] > totalSurface) totalSurface = sol[i];
    }
    cout << setprecision(9) << "Case #" << t << ": " << totalSurface << endl;
  }
  return 0;
}
