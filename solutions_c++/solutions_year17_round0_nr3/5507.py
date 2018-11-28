#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

void solve_case(long long unsigned N, long long unsigned K)
{
  vector<long long unsigned> stalls {N};
  stalls.reserve(K);

  for(;K>1; --K)
  {
    auto& s = stalls.back();
    if(s>1)
    {
      stalls.push_back((s-1)/2);
      s /= 2;
    }
    else s=0;

    sort(begin(stalls), end(stalls));
  }

  const auto& s = stalls.back();
  if(s>1) cout << s/2 << ' ' << (s-1)/2;
  else cout << "0 0";
}

int main(int argc, char **argv)
{
  // get number of cases
  unsigned t;
  cin >> t;

  for(unsigned i=1; i<=t; ++i)
  {
    long long unsigned N, K;
    cin >> N >> K;

    cout << "Case #" << i << ": ";
    solve_case(N, K);
    cout << '\n';
  }

  return 0;
}
