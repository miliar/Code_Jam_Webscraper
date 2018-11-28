
#include <iostream>
#include <iomanip>

#define INF -1000000000

using namespace std;

int main(){
  ios::sync_with_stdio(false);
  int t;
  cin >> t;

  for(int c = 1; c <= t; c++){
    int d, n;
    cin >> d >> n;

    double tMax = INF;
    double k, s;

    for(int i = 0; i < n; i++){
      cin >> k >> s;
      tMax = max(tMax, (d - k) / s);
    }

    cout << fixed << setprecision(7) << "Case #" << c << ": " << d / tMax << endl;
  }

  return 0;
}
