#include <iostream>
#include <iomanip>

using namespace std;
int main()
{
  int N; cin >> N;
  for (int ii = 1; ii <= N; ii++)
  {
    int d, n; cin >> d >> n;
    double si, vi;
    double ti, tmax = 0;
    for (int i = 0; i < n; i++)
    {
      cin >> si >> vi;
      ti = (d-si) / vi;
      if (ti > tmax) tmax = ti;
    }
    cout << "Case #" << ii << ": " << setprecision(12) << d / tmax << endl;
  }
  return 0;
}