#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <map>
#include <queue>
#include <ctime>
#include <cmath>

using namespace std;

#define forn(I,N) for (int I=0; I<N; I++)
#define fornd(I,N) for (int I=N-1; I>=0; I--)
#define forab(I,A,B) for (int I=A; I<=B; I++)
#define forabd(I,A,B) for (int I=B; I>=A; I--)
#define FOREACH(I,A) for (__typeof__(A)::iterator I=A.begin(); I<A.end(); I++)
#define pb push_back
#define mp make_pair

typedef long long int ll;

int main() {
  int T;
  cin >> T;

  cout << fixed << setprecision(8);

  forn (i, T) {
    int N, K;
    cin >> N >> K;

    double core;
    cin >> core;

    vector<double> p(N);
    forn (j, N) {
      cin >> p[j];
    }
    p.pb(1.0);

    sort(p.begin(), p.end());

    //forn(j, N) cout << p[j] << " ";
    //cout << endl;
    forn (j, N) {
      if (p[j] < p[j + 1]) {
        double dist = min (core / (j + 1), p[j + 1] - p[j]);
        core -= dist * (j + 1);
        forn (k, j + 1) {
          p[k] += dist;
        }
      }
    }

    double ans = 1.0;
    forn(j, N) {
      ans *= p[j];
    }
    cout << "Case #" << i + 1 << ": " << ans << endl;
  }

  return 0;
}
