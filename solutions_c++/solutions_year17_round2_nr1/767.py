#include <bits/stdc++.h>

using namespace std;

long double solve()
{
  int D, N;
  cin >> D >> N;

  long double maxt = 0;
  for (int i = 0; i < N; i++) {
    int K, S;
    cin >> K >> S;
    long double t = (long double)(D - K) / S;
    maxt = max(maxt, t);
  }

  return D / maxt;
}

int main()
{
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    cout << "Case #" << i << ": " << fixed << setprecision(6) << solve()
	 << endl;
  }    
  return 0;
}
