//
// Created by pierre on 13.05.17.
//

#include <iostream>
#include <map>
#include <vector>

using namespace std;


int H, W;

char tab[59][59];

map<pair<int, int>, int> guns;

vector<pair<int, int> > getGuns(int y, int x, int direction, int care);

bool outOfBounds(int y, int x);
int getDirection(pair<int, int> g, pair<int, int> p);
int dx[] = {0, 0, -1, 1};
int dy[] = {-1, 1, 0, 0};

int main()
{
  int ilez;
  cin >> ilez;
  for (int aa = 0; aa < ilez; aa++)
  {
    cin >> H >> W;

    for (int y = 0; y < H; y++)
    {
      for (int x = 0; x < W; x++)
      {
        cin >> tab[y][x];
        if (tab[y][x] == '-' || tab[y][x] == '|')
        {
          guns[make_pair(y, x)] = -1;
          tab[y][x] = 'g';
        }
      }
    }

    bool dasie = 1;

    for (int y = 0; y < H && dasie; y++)
    {
      for (int x = 0; x < W && dasie; x++)
      {
        if (tab[y][x] == 'g')
        {
          vector<pair<int, int>> left = getGuns(y, x, 0, 0);
          vector<pair<int, int>> right = getGuns(y, x, 1, 0);
          vector<pair<int, int>> up = getGuns(y, x, 2, 0);
          vector<pair<int, int>> down = getGuns(y, x, 3, 0);

          int hor = left.size() == 1 && right.size() == 1;
          int ver = up.size() == 1 && down.size() == 1;

          if (!hor && !ver)
          {
            dasie = 0;
            break;
          }
          if (hor ^ ver)
          {
            if (hor) guns[make_pair(y, x)] = 0;
            else guns[make_pair(y, x)] = 1;
          }
        }

      }
    }

//    for (int y = 0; y < H; y++)
//    {
//      for (int x = 0; x < W; x++)
//      {
//        if (tab[y][x] == 'g')
//        {
//          cout << guns[make_pair(y, x)];
//        }
//        else cout << tab[y][x];
//      }
//      cout << endl;
//    }

    bool zmieniloSie = 1;

    while (dasie && zmieniloSie)
    {
      zmieniloSie = 0;
      for (int y = 0; y < H && dasie; y++)
      {
        for (int x = 0; x < W && dasie; x++)
        {
          if (tab[y][x] == '.')
          {
            vector<pair<int, int> > g;

            for (int i = 0; i < 4; i++)
            {
              vector<pair<int, int> > n = getGuns(y, x, i, 1);
              for (int j = 0; j < n.size(); j++)
              {
                g.push_back(n[j]);
              }
            }

            if (g.size() == 0)
            {
              dasie = 0;
            }
            else if (g.size() == 1)
            {
              if (guns[g[0]] == -1) zmieniloSie = 1;
              guns[g[0]] = getDirection(g[0], make_pair(y, x));
            }

          }
        }
      }
    }

    cout << "Case #" << aa + 1 << ": ";

    if (dasie)
    {
      cout << "POSSIBLE" << endl;
      for (int y = 0; y < H; y++)
      {
        for (int x = 0; x < W; x++)
        {
          if (tab[y][x] == 'g')
          {
            cout << (guns[make_pair(y, x)] == 0 ? '|' : '-');
          }
          else cout << tab[y][x];
        }
        cout << endl;
      }
    }
    else
    {
      cout << "IMPOSSIBLE" << endl;
    }

  }
}

int getDirection(pair<int, int> g, pair<int, int> p)
{
  if (g.first == p.first) return 1;
  return 0;
}

vector<pair<int, int> > getGuns(int y, int x, int direction, int care)
{
  if (outOfBounds(y, x) || tab[y][x] == '#')
  {
    return vector<pair<int, int>>();
  }

  vector<pair<int, int>> res = getGuns(y + dy[direction], x + dx[direction], direction, care);
  if (tab[y][x] == 'g')
  {
    if (care)
    {
      if (guns[make_pair(y, x)] == direction / 2 || guns[make_pair(y, x)] == -1)
        res.push_back(make_pair(y, x));
    }
    else
    {
      res.push_back(make_pair(y, x));
    }
  }
  return res;
}

bool outOfBounds(int y, int x)
{
  return y < 0 || y >= H || x < 0 || x >= W;
}
