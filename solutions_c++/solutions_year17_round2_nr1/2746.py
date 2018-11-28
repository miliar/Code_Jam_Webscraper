#include <bits/stdc++.h>
using namespace std;

int main()
{
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  int T;
  cin >> T;
  for (int test_case = 1; test_case <= T; test_case++)
  {
    int d, n;
    cin >> d >> n;

    pair<int, int> horses[10000];
    for (int i = 0; i < n; i++)
      cin >> horses[i].first >> horses[i].second;
 
    sort(horses, horses + n);
    reverse(horses, horses + n);

    double max_time = 0;
    for (int i = 0; i < n; i++)
    {
      double dist = d - horses[i].first;
      double time = dist / horses[i].second;

      max_time = max(max_time, time); 
    }

    double cruise_speed = d / max_time;

    cout.precision(20);
    cout << "Case #" << test_case << ": " << fixed << cruise_speed << '\n';
  }
}
