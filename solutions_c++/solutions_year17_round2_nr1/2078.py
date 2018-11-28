// Author: Krzysztof Bochenek
// Email:  kpbochenek@gmail.com
// --------------------------------
#include <stdio.h>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <math.h>
#include <algorithm>
#include <string>
#include <iostream>
#include <iomanip>

typedef long long int ll;
typedef unsigned long long ull;

using namespace std;

int main() {

  int T;

  cin >> T;

  for (int t=1; t<=T; ++t) {
    long double D, N, ki, si;

    cin >> D >> N;

    vector<pair<int,int>> positions;
    for (int i=0; i<N; ++i) {
      cin >> ki >> si;
      positions.push_back(make_pair(ki, si));
    }

    long double left = 0;
    long double right = 10e50+10;

    long double prev_diff = -1;

    while ((right - left > 0.0000001)) {
      long double diff = right-left;
      if (prev_diff == diff) break;
      prev_diff = diff;
      // cout << setprecision(12);
      // cout << left << " VS " << right << " -- > " << (right == left) << " eh " << right - left << endl;
      long double middle = (left + right) / 2;
      bool is_speed_ok = true;

      long double time_needed_me = D / middle;

      for (auto horse: positions) {
	long double hpos = horse.first;
	long double hspeed = horse.second;

	long double time_needed_horse = (D - hpos) / hspeed;

	if (time_needed_horse >= time_needed_me) {
	  is_speed_ok = false;
	  break;
	}
      }


      if (is_speed_ok) {
	left = middle;
      } else {
	right = middle;
      }
    }

    cout << setprecision(12);
    cout << "Case #" << t << ": " << ((left + right) / 2) << endl;
  }

  return 0;
}
