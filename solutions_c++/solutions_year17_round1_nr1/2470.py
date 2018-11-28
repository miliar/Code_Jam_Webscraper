#include <iostream>
#include <vector>
#include <set>
using namespace std;
bool emptyRow(const auto & grid, const int & i, const int & start, const int & stop)
{
  if(i < 0 || i >= grid.size())
    return false;
  for(int j = start; j < stop; j++)
  {
    if(grid[i][j] != '?')
      return false;
  }
  return true;
}

void place(auto & grid, const int & i, const int & start, const int & stop, const char & c)
{
  for(int j = start; j < stop; j++)
  {
    grid[i][j] = c;
  }
}

void findRange(auto & grid, const int & i, const int & j, int & start, int & stop)
{
  int k;
  for(k = j - 1; k >= 0 && grid[i][k] == '?'; k--);
  start = k + 1;
  for(k = j + 1; k < grid[i].size() && grid[i][k] == '?'; k++);
  stop = k;
}

void solve(auto & grid)
{
  bool seen[127] = {false};
  for(int i = 0; i < grid.size(); i++)
  {
    char same = '?';
    for(int j = 0; j < grid[i].size(); j++)
    {
      if(grid[i][j] != '?' && !seen[grid[i][j]])
      {
        seen[grid[i][j]] = true;
        int start, stop, k;
        findRange(grid, i, j, start, stop);
        //cout << start << " " << stop << endl;
        place(grid, i, start, stop, grid[i][j]);
        k = i + 1;
        while(emptyRow(grid, k, start, stop))
        {
          place(grid, k, start, stop, grid[i][j]);
          k++;
        }
        k = i - 1;
        while(emptyRow(grid, k, start, stop))
        {
          place(grid, k, start, stop, grid[i][j]);
          k--;
        }
      }
    }
  }
}

void printGrid(const vector<string> & grid)
{
  for(int i = 0; i < grid.size(); i++)
  {
    cout << grid[i] << endl;
  }
}

int main()
{
  int T;
  int R, C;
  vector<string> grid;
  cin >> T;
  for(int i = 1; i <= T; i++)
  {
    cin >> R >> C;
    grid.resize(R);
    for(int j = 0; j < R; j++)
    {
      cin >> grid[j];
    }
    cout << "Case #" << i << ": " << endl;
    solve(grid);
    printGrid(grid);
    grid.clear();
  }
  return 0;
}