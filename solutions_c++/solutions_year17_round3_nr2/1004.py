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

  forn (i, T) {
    int ac, aj;
    cin >> ac >> aj;

    vector <int> from(ac + aj), to(ac + aj);
    forn(j, ac + aj) {
      cin >> from[j] >> to[j];
    }

    cout << "Case #" << i + 1 << ": ";

    if (ac + aj <= 1) {
      cout << 2 << endl;
    } else {
      if (ac == 1 && aj == 1) {
        cout << 2 << endl;
      } else {
        int t1 = min(from[0], from[1]);
        int t2 = 1440 - max(to[0], to[1]);
        int t3 = from[0] > from[1] ? from[0] - to[1] : from[1] - to[0];
        // cout << t1 << " " << t2 << " " << t3 << endl;
        if (t1 + t2 >= 720 || t3 >= 720) {
          cout << 2 << endl;
        } else {
          cout << 4 << endl;
        }
      }
    }
  }

  return 0;
}
