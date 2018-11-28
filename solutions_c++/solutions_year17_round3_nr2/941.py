#include <cassert>

#include <cmath>
#include <cstdio>
#include <vector>
#include <algorithm>

int main() {
  int T;
  scanf ("%d", &T);

  for (int t = 1; t <= T; t++)
  {
    int Ac, Aj;

    scanf ("%d %d", &Ac, &Aj);

    std::vector< std::pair <int, int> > CD (Ac);
    std::vector< std::pair <int, int> > JK (Aj);

    bool is2 = false;

    for (int i = 0; i < Ac; i++)
    {
      scanf ("%d %d", &CD[i].first, &CD[i].second);
    }

    for (int i = 0; i < Aj; i++)
    {
      scanf ("%d %d", &JK[i].first, &JK[i].second);
    }

    for (int i = 0; i < Ac; i++)
    {
      if ((CD[(i + 1) % Ac].first + 1440 - CD[i].second) % 1440 >= 720)
        is2 = true;
    }    

    for (int i = 0; i < Aj; i++)
    {
      if ((JK[(i + 1) % Aj].first + 1440 - JK[i].second) % 1440 >= 720)
        is2 = true;
    }    

    printf ("Case #%d: %d\n", t, is2 ? 2 : 4);
  }

  return 0;
}
