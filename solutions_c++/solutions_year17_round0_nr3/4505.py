#include <bits/stdc++.h>

using namespace std;

typedef long long L;

#define X first
#define Y second

class compare {
  public:
  bool operator () (const pair <L, L> A, const pair <L, L> B) {
    L l1 = A.Y - A.X;
    L l2 = B.Y - B.X;

    if (l1 != l2) return l1 > l2;
    return A.X < B.X;
  }
};

set <pair <L, L>, compare> S;

int main()
{
  int tt;
  scanf("%d", &tt);

  for (int _t = 1; _t <= tt; ++_t) {
    L n, k;
    S.clear();
    scanf("%lld %lld", &n, &k);
    
    S.insert({1, n});
    L mn = -1, mx = -1;
    while (k--) {
      assert(!S.empty());
      pair <L, L> now = *S.begin();
      L mid = (now.X + now.Y) >> 1;
      L ls = mid - now.X;
      L rs = now.Y - mid;

      mx = max(ls, rs);
      mn = min(ls, rs);

      S.erase(S.begin());
      if (mid - 1 >= now.X) {
        S.insert({now.X, mid - 1});
      }
      if (now.Y >= mid + 1) {
        S.insert({mid + 1, now.Y});
      }
    }

    printf("Case #%d: %lld %lld\n", _t, mx, mn);
  }
  return(0);
}
