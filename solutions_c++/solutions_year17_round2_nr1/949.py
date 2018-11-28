#include <iostream>
#include <sstream>
#include <climits>
#include <stdio.h>
#include <iomanip>
#include <list>
#include <map>
#include <unordered_map>
#include <algorithm>
#include <cmath>
#include <string>
#include <gmpxx.h>

using namespace std;

int T;

void solve(int t) {
  cerr << "test " << t << endl;
  int D;
  int N;
  cin >> D;
  cin >> N;
  double max_time = 0;
  int Ki;
  int Si;
  for(int i=0; i<N; i++) {
    cin >> Ki;
    cin >> Si;
    double distance = D - Ki;
    double time = distance/(1.0 * Si);
    max_time = max(max_time, time);
  }
  double speed = (1.0*D)/max_time;
  cout << setprecision(9);
  cout << "Case #" << t << ": " << speed << endl;
}

int main() {
  cin >> T;
  for(int t=0; t<T; t++) {
    solve(t+1);
  }
}
