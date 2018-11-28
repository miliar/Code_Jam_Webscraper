#include <bits/stdc++.h>
#include <iostream>

using namespace std;

int main() {
  int loops;
  cin >> loops;
  for(int loop = 1; loop <= loops; loop++) {
    long double dest;
    int nhorses;
    cin >> dest >> nhorses;
    long double longesttime = 0;

    for(int i = 0; i < nhorses; i++) {
      long double ki, si;
      cin >> ki >> si;
      longesttime = max(longesttime, (dest - ki) / si);
    }
    cout << "Case #" << loop << ": " << setprecision(10) << dest / longesttime << endl;
  }
}
