#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>


struct stall
{
  int L = 0;
  int R = 0;
  bool oc = false;
};


bool operator<(stall const &s1, stall const &s2)
{
  int m1 = std::min(s1.L, s1.R);
  int m2 = std::min(s2.L, s2.R);
  if ( m1 == m2 )
  {
    return std::max(s1.L, s1.R) < std::max(s2.L, s2.R);
  }
  return m1 < m2;
}


using Stalls = std::vector<stall>;


void update(Stalls &S)
{
  int l = 0;
  for ( auto &s: S )
    if ( !s.oc )
      s.L = l++;
    else
    {
      l = 0;
      s.L = 0;
    }
  int r = 0;
  for ( size_t i = S.size(); i > 0; --i )
  {
    auto &s = S[i - 1];
    if ( !s.oc )
      s.R = r++;
    else
    {
      r = 0;
      s.R = 0;
    }
  }
}


std::pair<int, int> inc(Stalls &S)
{
  update(S);
  size_t bi = -1;
  for ( size_t i = 0; i != S.size(); ++i )
    if ( !S[i].oc )
    {
      if ( bi == size_t(-1) )
        bi = i;
      else if ( S[bi] < S[i] )
        bi = i;
    }
  if ( bi != size_t(-1) )
  {
    S[bi].oc = true;
    return std::make_pair(std::max(S[bi].L, S[bi].R),
        std::min(S[bi].L, S[bi].R));
  }
  return std::make_pair(-1, -1);
}


int main()
{
  int T;
  std::cin >> T;
  for ( int t = 1; t <= T; ++t )
  {
    int N, K;
    std::cin >> N >> K;
    Stalls S(N + 2);
    S[0].oc = true;
    S[N + 1].oc = true;
    int y = -1, z = -1;
    for ( int k = 1; k <= K; ++k )
      std::tie(y, z) = inc(S);
    std::cout << "Case #" << t << ": " << y << ' ' << z << '\n';
  }
  return 0;
}
