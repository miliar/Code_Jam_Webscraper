#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;

int main () {
  int T;
  cin >> T;
  for(int tc=1; tc<=T; tc++) {
    int D, N;
    cin >> D >> N;
    vector<int> pos(N);
    vector<int> speed(N);
    double curmax = 0.0;
    for(int i=0; i<N; i++){
      cin >> pos[i] >> speed[i];
      curmax = max(((double)(D-pos[i]))/((double)speed[i]), curmax);
    }
    double res = ((double)D)/((double)curmax);
    printf("Case #%d: %.8lf\n", tc, res);
  }
}
