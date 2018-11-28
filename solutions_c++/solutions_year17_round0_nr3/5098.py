#include <cstdio>
#include <vector>
#include <cstring>
#include <cassert>
#include <queue>

using namespace std;

typedef pair<long long int, long long int> pll;

struct Compare
{
  bool operator()(const pll &L, const pll &R) const
  {
    if (L.first < R.first)
      return true;
    if (R.first < L.first)
      return false;
    return (L.second > R.second);
  }
};

void EvenOp(priority_queue<pll, std::vector<pll>, Compare> &Eq,
            priority_queue<pll, std::vector<pll>, Compare> &Oq,
            long long int &mx, long long int &mi)
{
  assert(!Eq.empty());
  pll P = Eq.top(); Eq.pop();
  mx = P.first / 2; mi = mx - 1;

  if (mi != 0)
  {
    if (mi % 2 == 0)
      Eq.push(make_pair(mi, P.second));
    else
      Oq.push(make_pair(mi, P.second));
  }

  if (mx % 2 == 0)
    Eq.push(make_pair(mx, P.second + mi + 1));
  else
    Oq.push(make_pair(mx, P.second + mi + 1));
}

void OddOp(priority_queue<pll, std::vector<pll>, Compare> &Eq,
           priority_queue<pll, std::vector<pll>, Compare> &Oq,
           long long int &mx, long long int &mi)
{
  assert(!Oq.empty());
  pll P = Oq.top(); Oq.pop();
  mx = mi = P.first / 2;

  if (P.first != 1)
  {
    if (mx % 2 == 0)
    {
      Eq.push(make_pair(mx, P.second));
      Eq.push(make_pair(mx, P.second + mx + 1));
    }
    else
    {
      Oq.push(make_pair(mx, P.second));
      Oq.push(make_pair(mx, P.second + mx + 1));
    }
  }
}

int main()
{
  int T; scanf("%d\n", &T);
  for (int ii = 1; ii <= T; ++ii)
  {
    long long int N, K;
    scanf("%lld %lld\n", &N, &K);

    priority_queue<pll, std::vector<pll>, Compare>
        Eq((Compare())), Oq((Compare()));

    if (N % 2 == 0) Eq.push(make_pair(N, 0));
    else Oq.push(make_pair(N, 0));

    long long int mx = 0, mi = 0;
    for (int i = 0; i < K; ++i)
    {
      if (Eq.empty())
        OddOp(Eq, Oq, mx, mi);
      else if (Oq.empty())
        EvenOp(Eq, Oq, mx, mi);
      else
      {
        pll Po = Oq.top(); pll Pe = Eq.top();
        if (Po.first > Pe.first)
          OddOp(Eq, Oq, mx, mi);
        else
          EvenOp(Eq, Oq, mx, mi);
      }
    }

    printf("Case #%d: %lld %lld\n", ii, mx, mi);
  }
}
