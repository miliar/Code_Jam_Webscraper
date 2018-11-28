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

vector<long long unsigned> decompose(long long unsigned n, long long unsigned b)
{
  vector<long long unsigned> d;

  while(n>0)
  {
    d.push_back(n%b);
    n /= b;
  }

  return d;
}

long long unsigned kapow(long long unsigned b, long long unsigned e)
{
  long long unsigned r = 1;
  while(e)
  {
    if(e & 1) r *= b;
    e >>= 1;
    b *= b;
  }

  return r;
}

void solve_case(long long unsigned N)
{
  auto d = decompose(N, 10);

  for(int i=0; i<d.size()-1;)
  {
    if(d[i+1]>d[i])
    {
      for(int j=i; j>=0; --j)
        N -= d[j]*kapow(10, j);
      N -= 1;
      d  = decompose(N, 10);
    }
    else
      ++i;
  }

  cout << N;
}

int main(int argc, char **argv)
{
  // get number of cases
  unsigned t;
  cin >> t;

  for(unsigned i=1; i<=t; ++i)
  {
    long long unsigned N;
    cin >> N;

    cout << "Case #" << i << ": ";
    solve_case(N);
    cout << '\n';
  }

  return 0;
}
