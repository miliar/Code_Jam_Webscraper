#include <algorithm>
#include <climits>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;

#define sz(X) (int)X.size()
#define mp(X,Y) make_pair(X,Y)
#define pp pair<double, int>

int main(){
  int T;
  cin >> T;
  for(int caso = 1; caso <= T; caso++) {
    int  n;
    double D, K[1010], S[1010];
    cin >> D >> n;
    for(int i=0;i<n;i++)
      cin >> K[i] >> S[i];
    double t = 0.0;
    for(int i=0;i<n;i++)
      t = max(t, (D-K[i])/S[i]);
    printf("Case #%d: %.8f\n", caso, D/t);
  }
  return 0;
}
