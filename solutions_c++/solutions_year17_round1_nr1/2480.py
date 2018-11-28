#include <iostream>
#include <string>
#include <set>
#include <vector>
#include <map>
#include <algorithm>
#include <queue>
#include <stack>
#include <cmath>
#include <sstream>
#include <fstream>
#include <limits>
#include <cassert>

using namespace std;

#define FORi(_n_) for (size_t i = 0; i < _n_; i++)
#define FORj(_n_) for (size_t j = 0; j < _n_; j++)
#define FORk(_n_) for (size_t k = 0; k < _n_; k++)

typedef long long ll;
typedef unsigned long long ull;
typedef size_t szt;

int main(int argc, char** argv)
{
  ifstream input(argv[1]);

  size_t T;
  input >> T;

  for (size_t t = 1; t <= T; t++)
  {
    size_t R, C;
    input >> R >> C;

    // Read input
    map<char, tuple<szt, szt, szt, szt>> charToBBoxMap;
    map<char, szt> charCountMap;
    map<size_t, map<size_t, char>> cake;
    for (szt r = 0; r < R; r++)
    {
      string row;
      input >> row;
      for (szt c = 0; c < row.length(); c++)
      {
        cake[r][c] = row[c];
        charCountMap[row[c]]++;
        if (charToBBoxMap.count(row[c]))
        {
          auto& bbox = charToBBoxMap[row[c]];
          get<0>(bbox) = min(get<0>(bbox), r);
          get<1>(bbox) = min(get<1>(bbox), c);
          get<2>(bbox) = max(get<2>(bbox), r);
          get<3>(bbox) = max(get<3>(bbox), c);
        }
        else
        {
          charToBBoxMap[row[c]] = make_tuple(r, c, r, c);
        }
      }
    }

    // Handle rectangular case
    for (szt r = 0; r < R; r++)
    {
      auto& row = cake[r];
      for (szt c = 0; c < C; c++)
      {
        if (row[c] == '?') continue;
        if (charCountMap[row[c]] == 1) continue;

        auto& bbox = charToBBoxMap[row[c]];

        for (szt ri = get<0>(bbox); ri <= get<2>(bbox); ri++)
        {
          for (szt ci = get<1>(bbox); ci <= get<3>(bbox); ci++)
          {
            cake[ri][ci] = row[c];
            charCountMap[row[c]]++;
          }
        }
      }
    }

    for (szt r = 0; r < R; r++)
    {
      auto& row = cake[r];
      for (szt c = 0; c < C; c++)
      {
        if (row[c] == '?') continue;
        if (charCountMap[row[c]] == 1) continue;

        auto& bbox = charToBBoxMap[row[c]];
        get<0>(bbox) = min(get<0>(bbox), r);
        get<1>(bbox) = min(get<1>(bbox), c);
        get<2>(bbox) = max(get<2>(bbox), r);
        get<3>(bbox) = max(get<3>(bbox), c);
      }
    }


    // Handle remaining
    for (szt r = 0; r < R; r++)
    {
      auto& row = cake[r];
      for (szt c = 0; c < C; c++)
      {
        if (row[c] == '?') continue;

        auto& bbox = charToBBoxMap[row[c]];
        szt xl = get<0>(bbox);
        szt yl = get<1>(bbox);
        szt xh = get<2>(bbox);
        szt yh = get<3>(bbox);

        {
          // Go low
          int x = (int)xl-1;
          while (x >= 0)
          {
            bool allQ = true;
            for (szt y = yl; y <= yh; y++)
            {
              if (cake[(szt)x][y] == '?') continue;
              allQ = false;
              break;
            }
            if (!allQ) break;;
            for (szt y = yl; y <= yh; y++)
            {
              cake[(szt)x][y] = row[c];
              charCountMap[row[c]]++;
            }
            x--;
          }

          // Go high
          x = (int)xh+1;
          while (x < R)
          {
            bool allQ = true;
            for (szt y = yl; y <= yh; y++)
            {
              if (cake[(szt)x][y] == '?') continue;
              allQ = false;
              break;
            }
            if (!allQ) break;
            for (szt y = yl; y <= yh; y++)
            {
              cake[(szt)x][y] = row[c];
              charCountMap[row[c]]++;
            }
            x++;
          }

        }
      }
    }

    for (szt r = 0; r < R; r++)
    {
      auto& row = cake[r];
      for (szt c = 0; c < C; c++)
      {
        if (row[c] == '?') continue;
        if (charCountMap[row[c]] == 1) continue;

        auto& bbox = charToBBoxMap[row[c]];
        get<0>(bbox) = min(get<0>(bbox), r);
        get<1>(bbox) = min(get<1>(bbox), c);
        get<2>(bbox) = max(get<2>(bbox), r);
        get<3>(bbox) = max(get<3>(bbox), c);
      }
    }

    for (szt r = 0; r < R; r++)
    {
      auto& row = cake[r];
      for (szt c = 0; c < C; c++)
      {
        if (row[c] == '?') continue;

        auto& bbox = charToBBoxMap[row[c]];
        szt xl = get<0>(bbox);
        szt yl = get<1>(bbox);
        szt xh = get<2>(bbox);
        szt yh = get<3>(bbox);

        {
          // Go low
          int y = (int)yl-1;
          while (y >= 0)
          {
            bool allQ = true;
            for (szt x = xl; x <= xh; x++)
            {
              if (cake[x][(szt)y] == '?') continue;
              allQ = false;
              break;
            }
            if (!allQ) break;
            for (szt x = xl; x <= xh; x++)
            {
              cake[x][(szt)y] = row[c];
              charCountMap[row[c]]++;
            }
            y--;
          }

          // Go high
          y = (int)yh+1;
          while (y < (int)C)
          {
            bool allQ = true;
            for (szt x = xl; x <= xh; x++)
            {
              if (cake[x][(szt)y] == '?') continue;
              allQ = false;
              break;
            }
            if (!allQ) break;
            for (szt x = xl; x <= xh; x++)
            {
              cake[x][(szt)y] = row[c];
              charCountMap[row[c]]++;
            }
            y++;
          }
        }
      }
    }
    cout << "Case #" << t << ":" << endl;
    for (szt r = 0; r < R; r++)
    {
      auto& row = cake[r];
      for (szt c = 0; c < C; c++)
        cout << row[c];
      cout << endl;
    }
  }

  return 0;
}
