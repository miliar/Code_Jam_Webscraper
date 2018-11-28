#include <algorithm>
#include <cmath>
#include <deque>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <utility>
#include <vector>
#include <random>
#include <ctime>

using namespace std;

int n, m;
typedef pair<int8_t, int8_t> pcor;
int8_t field[101][101];
int8_t init_field[101][101];

struct figure
{
  figure(char c, int8_t px, int8_t py) : c(c), pos(px, py) {}
  char c;
  pcor pos;
};

std::vector<pcor> solve_crosses(const std::vector<pcor>& crosses)
{
  vector<pcor> res(n - crosses.size());
  if (!res.empty())
  {
    vector<bool> mask_x(n), mask_y(n);
    for (auto p : crosses)
    {
      mask_x[p.first - 1] = true;
      mask_y[p.second - 1] = true;
    }
    auto it_x = mask_x.begin();
    auto it_y = mask_y.begin();
    for (auto& el : res)
    {
      while(*it_x)
        ++it_x;
      while(*it_y)
        ++it_y;
      el = pcor{distance(mask_x.begin(), it_x++) + 1, distance(mask_y.begin(), it_y++) + 1};
    }
  }
  return res;
}

void set_plus(vector<vector<bool>>& f, int8_t x, int8_t y)
{
  int ss = x + y;
  for (int i = max(1, ss - n); i <= min(ss, n); ++i) {
    f[i][ss - i] = true;
  }
  int sb = x - y;
  for (int i = 1 + max(0, sb); i <= n + min(0, sb); ++i) {
    f[i][i - sb] = true;
  }
}

std::vector<pcor> solve_pluses(const std::vector<pcor>& pluses)
{
  vector<pcor> res;
  vector<vector<bool>> f(n + 1, vector<bool>(n+1));
  for(auto p : pluses)
  {
    set_plus(f, p.first, p.second);
  }
  for (int i = 1; i <=n; ++i)
    if(!f[i][1])
    {
      res.emplace_back(i,1);
      set_plus(f,i,1);
    }
  for (int i = 1; i <=n; ++i)
    if(!f[i][n])
    {
      res.emplace_back(i,n);
      set_plus(f,i,n);
    }
  for (int i = 1; i <=n; ++i)
    if(!f[1][i])
    {
      res.emplace_back(1,i);
      set_plus(f,1,i);
    }
  for (int i = 1; i <=n; ++i)
    if(!f[n][i])
    {
      res.emplace_back(n,i);
      set_plus(f,n,i);
    }
  return res;
}

int main()
{
    int tests;
    cin.sync_with_stdio(false);
    cin >> tests;
    char c;
    int px, py;
    for (auto t = 1; t <= tests; ++t)
    {
        memset(field, 0, sizeof(field));
        memset(init_field, 0, sizeof(field));
        cin >> n >> m;
        vector<pcor> crosses, pluses;
        crosses.reserve(m);
        pluses.reserve(m);
        for (auto i = 0; i < m; ++i)
        {
          cin >> c >> px >> py;
          switch (c)
          {
          case 'x': crosses.emplace_back(px, py),
                    init_field[px][py] = 1;
                    break;
          case '+': pluses.emplace_back(px, py),
                    init_field[px][py] = 2;
                    break;
          case 'o': crosses.emplace_back(px, py),
                    pluses.emplace_back(px, py),
                    init_field[px][py] = 3;
                    break;
          default: cout << "FAIL\n";
          }
        }
        auto add_cross = solve_crosses(crosses);
        auto add_plus = solve_pluses(pluses);
        for(auto p : add_cross)
        {
          field[p.first][p.second] ^= 1;
        }
        for(auto p : add_plus)
        {
          field[p.first][p.second] ^= 2;
        }
        int score = 0;
        vector<figure> output;
        int8_t val;
        for (auto i = 1; i <= n; ++i)
          for (auto j = 1; j <= n; ++j)
            if ((val = (field[i][j] | init_field[i][j]))) {
              score += (val + 1) / 2;
              switch(field[i][j])
              {
                case 1: output.emplace_back(init_field[i][j] ? 'o' : 'x',i,j); break;
                case 2: output.emplace_back(init_field[i][j] ? 'o' : '+',i,j); break;
                case 3: output.emplace_back('o',i,j); break;
              }
            }
        cout << "Case #" << t << ": ";
        cout << score  << " " << output.size() << endl;
        for (auto m : output)
            cout << m.c << " " << (short)m.pos.first << " " << (short)m.pos.second  << endl;
    }

    return 0;
}
