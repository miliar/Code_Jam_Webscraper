#include <iostream>
#include <algorithm>
#include <map>
#include <string>
#include <set>
#include <vector>
#include <list>
#include <iomanip>

#define TRACE(x) cerr << #x << " = " << x << endl
#define _ << " _ " << 

using namespace std;

int main() {
  int t;
  cin >> t;
  for (int tt=0; tt<t; tt++) {
    int d, n;
    cin >> d >> n;
    vector<int> k(n);
    vector<int> s(n);
    for (int i=0; i<n; i++)
      cin >> k[i] >> s[i];
    double best = 1e100;
    for (int i=0; i<n; i++) {
      double x = d/double(d-k[i])*s[i];
      best = min(best, x);
    }
    
    cout << "Case #" << tt+1 << ": " << setprecision(10) << best << endl;
  }
  return 0;
}
