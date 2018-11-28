#include <iostream>
#include <string>

using namespace std;

int main()
{
  cout.precision(20);
  uint nCase;
  cin >> nCase;
  for (auto iCase = 1; iCase <= nCase; ++iCase) {
    long long d;
    uint n;
    cin >> d >> n;

    double m = 0.0;
    for (auto i = 0; i < n; ++i) {
      long long k, s;
      cin >> k >> s;
      double t = (1.0 * (d-k)) / s;
      m = max(m, t);
    }

    double ans = d / m;

    cout << "Case #" << iCase << ": " << ans << endl;
  }

  return 0;
}
