#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <math.h>
#include <algorithm>
#include <gmpxx.h>

using namespace std;

void flip(vector<double>& S, int P, int K)
{
  for(unsigned i=0; i<K; ++i)
    S[P+i] = not S[P+i];
}

void solve_case(vector<double> S, int K)
{
  unsigned count = 0;

  for(unsigned i=0; i<=S.size()-K; ++i)
  {
    if(not S[i])
    {
      flip(S, i, K);
      ++count;
    }
  }

  for(auto s : S)
  {
    if(not s)
    {
      cout << "IMPOSSIBLE";
      return;
    }
  }

  cout << count;
}

int main(int argc, char **argv)
{
  // get number of cases
  unsigned t;
  cin >> t;

  for(unsigned i=1; i<=t; ++i)
  {
    string s;
    int K;
    cin >> s >> K;

    vector<double> S(s.size());
    for(unsigned i=0; i<s.size(); ++i)
      S[i] = (s[i]=='+');

    cout << "Case #" << i << ": ";
    solve_case(S, K);
    cout << '\n';
  }

  return 0;
}
