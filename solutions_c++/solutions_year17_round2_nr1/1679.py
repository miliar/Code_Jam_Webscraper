#include <iostream>
#include <cstdio>
using namespace std;


double solve() {
  int D,N;
  cin >> D >> N;
  double maxt = 0;
  for(int i=0;i<N;i++) {
    int K,S;
    cin >> K >> S;
    double t = (double)(D - K) / S;
    if (t >= maxt)
      maxt = t;
  }
  return (double)D/maxt;
}

int main() {
  int T;
  cin >> T;
  for(int i = 1;i<=T;i++) {
    cout << "Case #" << i << ": ";
    printf("%lf\n", solve());
  }
}
