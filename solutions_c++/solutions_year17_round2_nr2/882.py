#include <iostream>
#include <string>
#include <algorithm>

using namespace std;
int main()
{
  int N; cin >> N;
  for (int ii = 1; ii <= N; ii++)
  {
    int n, r, o, y, g, b, v; 
    cin >> n >> r >> o >> y >> g >> b >> v;
    // y-v-y r-g-r b-o-b 
    string res = "";

    if (!r && !g && !b && !o)
    {
      if (y == v)
      {
        for (int i = 0; i < y; i++)
        {
          res += "YV";
        }
      }
      else
      {
        res = "IMPOSSIBLE";
      }
    }
    else if (!y && !v && !b && !o)
    {
      if (r == g)
      {
        for (int i = 0; i < r; i++)
        {
          res += "RG";
        }
      }
      else
      {
        res = "IMPOSSIBLE";
      }
    }
    else if (!r && !g && !y && !v)
    {
      if (b == o)
      {
        for (int i = 0; i < b; i++)
        {
          res += "BO";
        }
      }
      else
      {
        res = "IMPOSSIBLE";
      }
    }
    else
    {
      // y-v-y r-g-r b-o-b 
      if ((!v || v < y) && (!g || g < r) && (!o || o < b))
      {
        y -= v; r -= g; b -= o;
        if (y <= r+b && r <= y+b && b <= r+y)
        {
          if (r >= b && r >= y)
          {
            for (int i=0; i<r; i++)
            {
              res += "R";
              while (g > 0)
              {
                res += "GR"; g--;
              }
              if (i < y)
              {
                res += "Y";
                while (v > 0)
                {
                  res += "VY"; v--;
                }
              }
              if (r - 1 - i < b)
              {
                res += "B";
                while (o > 0)
                {
                  res += "OB"; o--;
                }
              }
            }
          }
          //-------------------------
          else if (b >= r && b >= y)
          {
            for (int i=0; i<b; i++)
            {
              res += "B";
              while (o > 0)
              {
                res += "OB"; o--;
              }
              if (i < y)
              {
                res += "Y";
                while (v > 0)
                {
                  res += "VY"; v--;
                }
              }
              if (b - 1 - i < r)
              {
                res += "R";
                while (g > 0)
                {
                  res += "GR"; g--;
                }
              }
            }
          }
          //-------------------------
          else if (y >= b && y >= r)
          {
            for (int i=0; i<y; i++)
            {
              res += "Y";
              while (v > 0)
              {
                res += "VY"; v--;
              }
              if (i < r)
              {
                res += "R";
                while (g > 0)
                {
                  res += "GR"; g--;
                }
              }
              if (y - 1 - i < b)
              {
                res += "B";
                while (o > 0)
                {
                  res += "OB"; o--;
                }
              }
            }
          }
        }
        else
        {
          res = "IMPOSSIBLE";
        }
      }
      else
      {
        res = "IMPOSSIBLE";
      }
    }
    cout << "Case #" << ii << ": " << res << endl;
  }
  return 0;
}