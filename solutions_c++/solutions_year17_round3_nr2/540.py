#include <iostream>
#include <cmath>
#include <cstdio>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cstring>

using namespace std;

const int N = 300;
int Ac, Aj;
struct range
{
  int l, r, m;
}R[N];

bool operator<(const range&a, const range&b)
{
  return a.l < b.l;
}

void init()
{
  cin >> Ac >> Aj;
  for (int i=1; i<=Ac; ++i)
  {
    cin >> R[i].l >> R[i].r;
    R[i].m = 0;
  }
  for (int i=1; i<=Aj; ++i)
  {
    cin >> R[i+Ac].l >> R[i+Ac].r;
    R[i+Ac].m = 1;
  }
}

int work()
{
  int ans = 0;
  sort(R+1, R+Ac+Aj+1);
  int t[2];
  t[0] = 720;
  t[1] = 720;
  R[0] = R[Ac+Aj];
  R[0].l -= 24*60;
  R[0].r -= 24*60;

  vector<int> free[2];
  for (int i=1; i<=Ac+Aj; ++i)
  {
    t[R[i].m] -= R[i].r-R[i].l;
    if (R[i].m != R[i-1].m)
      ++ans;
    else
      free[R[i].m].push_back(R[i].l-R[i-1].r);
  }
  for (int i=0; i<2; ++i)
  {
    sort(free[i].begin(), free[i].end());
    for (int f : free[i])
      if (f <= t[i])
        t[i] -= f;
      else
        ans += 2;
  }
  return ans;
}

int main()
{
  //freopen("B-small-attempt1.in", "r", stdin);
  //freopen("B.out", "w", stdout);
  freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w", stdout);
  //freopen("in", "r", stdin);
  //freopen("out", "w", stdout);
  int T;
  cin >> T;
  for (int i=1; i<=T; ++i)
  {
    cout << "Case #" << i << ": ";
    init();
    printf("%d\n", work());
  }
}
