#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

void solve_case(unsigned D, unsigned N, vector<unsigned> K, vector<unsigned> S)
{
  double time = 0;

  for(unsigned i=0; i<N; ++i)
  {
    const double t = double(D-K[i])/S[i];
    if(t>time) time = t;
  }

  cout << fixed << D/time << '\n';
}

int main(int argc, char **argv)
{
  // get number of cases
  unsigned t;
  cin >> t;

  for(unsigned i=1; i<=t; ++i)
  {
    unsigned D, N;
    cin >> D >> N;

    vector<unsigned> K(N), S(N);
    for(unsigned i=0; i<N; ++i)
      cin >> K[i] >> S[i];

    cout << "Case #" << i << ": ";
    solve_case(D, N, K, S);
  }

  return 0;
}
