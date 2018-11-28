#include <iostream>
#include <vector>
#include <cmath>
#include <bitset>
#include <string>

using namespace std;

pair<long,long> f(long long N, long long K) {
  if (N == K) return make_pair(0,0);

  long long high = ceil((N-1)/2.);
  long long low = floor((N-1)/2.);
  if (K == 1) {
    return make_pair(high, low);
  } else {
    if (K % 2 == 0) {
      return f(high, K/2);
    } else {
      return f(low, (K-1)/2);
    }
  }
}

void compute()
{
  long long N,K;
  cin >> N >> K;

  auto res = f(N,K);
  cout << res.first << " " << res.second << endl;
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
