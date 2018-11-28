#include <bits/stdc++.h>
using namespace std;

int n, d;
pair <int,int> horses[1010];

int ok(double v)
{
  for (int i = 0; i < n; i++)
    if (v > horses[i].second)
      if (horses[i].first / (v - horses[i].second) * v < d)
        return 0;
  return 1;
}

int main()
{
  int test;
  cin >> test;
  for (int iTest = 1; iTest <= test; iTest++)
  {
    cerr << "Running test " << iTest << endl;
    cin >> d >> n;
    for (int i = 0; i < n; i++)
      cin >> horses[i].first >> horses[i].second;
    sort(horses, horses + n);

    double low = 0, high = 1e20;
    for (int i = 0; i <= 100; i++)
    {
      double mid = (low + high) / 2;
      if (ok(mid)) low = mid;
      else high = mid;
    }

    cout << fixed << setprecision(9) << "Case #" << iTest << ": " << low << endl;
  }
}