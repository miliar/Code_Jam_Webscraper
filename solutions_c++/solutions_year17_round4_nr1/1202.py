#include <bits/stdc++.h>

#define MOD 1000000007

using namespace std;

typedef long long int lld;
typedef pair<int, int> pii;
typedef pair<pii, pii> line;

#define F first
#define S second

int main()
{
  int T, t;
  scanf("%d", &T);
  
  for (t = 1; t <= T; t++)
  {
    int ans = 0, n, p;
    scanf("%d %d", &n, &p);

    if (p == 2)
    {
      int a0 = 0, a1 = 0, vl;
      for (int i = 0; i < n; i++)
      {
        scanf("%d", &vl);
        if (vl % 2 == 0) a0++;
        else a1++;
      }

      ans = a0 + (a1 + 1) / 2;
    }
    else if (p == 3)
    {
      int a0 = 0, a1 = 0, a2 = 0, vl;
      for (int i = 0; i < n; i++)
      {
        scanf("%d", &vl);
        if (vl % 3 == 0) a0++;
        else if (vl % 3 == 1) a1++;
        else a2++;
      }

      int ls = 0;
      while (a0 + a1 + a2 > 0)
      {
        ans += (ls % 3 == 0);

        if (a0)
        {
          a0--;
          ls = 0;
          continue;
        }

        if (a1 && a2)
        {
          a1--;
          a2--;
          ls = 0;
          continue;
        }

        if (a1)
        {
          a1--;
          ls = (ls + 1) % 3;
        }

        if (a2)
        {
          a2--;
          ls = (ls + 2) % 3;
        }
      }

/*      ans = a0;

      int tmp = min(a1, a2);
      ans += tmp;
      a1 -= tmp;
      a2 -= tmp;

      ans += (a1 + 2) / 3 + (a2 + 2) / 3;*/
    }
    else if (p == 4)
    {
      int a0 = 0, a1 = 0, a2 = 0, a3 = 0, vl;
      for (int i = 0; i < n; i++)
      {
        scanf("%d", &vl);
        if (vl % 4 == 0) a0++;
        else if (vl % 4 == 1) a1++;
        else if (vl % 4 == 2) a2++;
        else a3++;
      }

      int ls = 0;
      while (a0 + a1 + a2 + a3 > 0)
      {
        ans += (ls % 4 == 0);

        if (a0)
        {
          a0--;
          ls = 0;
          continue;
        }

        if (a2 > 1)
        {
          a2 -= 2;
          ls = 0;
          continue;
        }

        if (a1 && a3)
        {
          a1--;
          a3--;
          ls = 0;
          continue;
        }

        if (a1 && ls == 3)
        {
          a1--;
          ls = 0;
          continue;
        }

        if (a2 && ls == 2)
        {
          a2--;
          ls = 0;
          continue;
        }

        if (a3 && ls == 1)
        {
          a3--;
          ls = 0;
          continue;
        }

        if (a1)
        {
          a1--;
          ls = (ls + 1) % 4;
          continue;
        }

        if (a3)
        {
          a3--;
          ls = (ls + 3) % 4;
          continue;
        }

        if (a2)
        {
          a2--;
          ls = (ls + 2) % 4;
          continue;
        }
      }

/*      ans = a0;

      int tmp = min(a1, a3);
      ans += tmp;
      a1 -= tmp;
      a3 -= tmp;

      ans += a2 / 2;
      a2 = a2 % 2;

      if (a1 > 2 && a2 > 0)
      {
        a1 -= 2;
        a2--;
        ans++;
      }

      if (a3 > 2 && a2 > 0)
      {
        a3 -= 2;
        a2--;
        ans++;
      }

      ans += (a1 + 3) / 4 + (a2 + 3) / 4 + (a3 + 3) / 4;*/
    }

    printf("Case #%d: %d\n", t, ans);
  }

  return 0;
}
