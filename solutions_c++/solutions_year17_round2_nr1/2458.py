#include <iostream>
#include <iomanip>
#include <cmath>
#include <vector>
#include <bitset>
#include <string>

using namespace std;

#define debug(x) cout << #x << ": " << x << endl;

void compute()
{
  int D, N;
  cin >> D >> N;

  double maxT = 0;;
  for (int i = 0; i < N; ++i) {
    int Ki, Si;
    cin >> Ki >> Si;
    maxT = max(static_cast<double>(D-Ki)/static_cast<double>(Si), maxT);
  }
  cout << setprecision(99) << D / maxT << endl;
}

int main()
{
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i)
  {
    cout << "Case #" << i << ": "; compute();
  }
}
