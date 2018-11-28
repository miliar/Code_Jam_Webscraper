#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;

int main()
{
  fstream cin("A-large.in.txt", fstream::in);
  fstream cout("A-large-output.txt", fstream::out);
  int t; cin >> t;
  for (int c = 1; c <= t; c++) {
    int d, n; cin >> d >> n;
    double maxt = 0;
    for (int i = 0; i < n; i++) {
        int ki, si; cin >> ki >> si;
        double ti = d - ki;
        ti /= si;
        maxt = max(maxt, ti);
    }
    double out = ((double)d)/maxt;
    cout << "Case #" << c << ": " << setprecision(12) << showpoint << fixed << out << endl;
  }
}
