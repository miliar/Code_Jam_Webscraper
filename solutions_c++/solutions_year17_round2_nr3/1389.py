#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>

using namespace std;

double mem[110][110];

double howfast(const vector<vector<int> >& dd, const vector<pair<int, int> >& h, int ch, int to, double adj) {

  if (to == dd.size())
    return 0;


  double dist = 0;
  for (int i = ch; i < to; ++i) {
    dist += dd[i][i+1];
  }
  if (dist > h[ch].first) {
    return INFINITY;
  }

  double dupa = dist/h[ch].second;
  return dupa+min(howfast(dd, h, ch, to+1, dupa), howfast(dd,h,to, to+1,0)) - adj;
  
}

double doit() {
  for (int i = 0; i < 110; ++i) {
    for (int j = 0; j < 110; ++j) {
      mem[i][j] = INFINITY;
    }
  }

  int N, Q;
  cin >> N >> Q;
  vector<pair<int, int> >h (N);
  for (int i = 0; i < N; ++i) {
    cin >> h[i].first >> h[i].second;
  }

  vector<vector<int> > dd(N, vector<int>(N));
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < N; ++j) {
      cin >> dd[i][j];
    }
  }

  {
    int d1, d2;
    cin >> d1 >> d2;
  }

  return howfast(dd, h, 0, 1,0);
}

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t)
    printf("Case #%d: %.9f\n", t, doit());
}
