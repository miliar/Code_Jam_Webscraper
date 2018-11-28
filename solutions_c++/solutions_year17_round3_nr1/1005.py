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
const double pi = 3.14159265358979323846;

int main() {
  int T;
  cin >> T;

  cout << fixed << setprecision(8);

  forn (i, T) {
    int n, K;
    cin >> n >> K;

    vector<ll> r(n), h(n);
    forn (j, n) {
      cin >> r[j] >> h[j];
    }

    ll best = 0;
    forn (j, n) {
      ll rad = r[j];
      ll area = r[j] * r[j] + (ll) 2 * r[j] * h[j];
      //cout << area << endl;

      vector<ll> tArea;
      forn(k, n) if (j != k && r[k] <= r[j]) {
        tArea.pb((ll) 2 * r[k] * h[k]);
      }
      if ((int)tArea.size() >= K - 1 && K - 1 > 0) {
        //cout << (int) tArea.size() - K + 1<< endl;
        //cout << K - 1 << endl;
        //cout << area << endl;
        sort(tArea.begin(), tArea.end());
        for(int k = (int)tArea.size() - K + 1; k <= (int) tArea.size() - 1; k++) {
          area += tArea[k];
        }
      }
      if (best < area) {
        best = area;
      }
    }

    // cout << best << endl;
    cout << "Case #" << i + 1 << ": " << (double) best * pi << endl;
  }

  return 0;
}
