#include <iostream>
#include <string>
#include <vector>

using namespace std;

void processGrid(vector<string> &grid);

int main()
{
  int num_tests;
  cin >> num_tests;
  for (int test = 1; test <= num_tests; test++) {
    int num_rows, num_cols;
    cin >> num_rows >> num_cols;
    vector<string> grid(num_rows);
    for (int r = 0; r < grid.size(); r++)
      cin >> grid[r];

    processGrid(grid);

    cout << "Case #" << test << ":\n";
    for (int r = 0; r < grid.size(); r++)
      cout << grid[r] << '\n';
  }
  return 0;
}

void processGrid(vector<string> &grid)
{
  vector<bool> used(300, false);
  for (int r = 0; r < grid.size(); r++)
    for (int c = 0; c < grid[r].size(); c++)
      if (grid[r][c] != '?' && !used[grid[r][c]]) {
	used[grid[r][c]] = true;
	bool found;
	int cl, rt, cr, rb;
	
	for (cl = c - 1; cl >= 0; cl--)
	  if (grid[r][cl] != '?')
	    break;
	cl++;
	
	found = false;
	for (rt = r - 1; rt >= 0; rt--) {
	  for (int j = cl; j <= c; j++)
	    if (grid[rt][j] != '?') {
	      found = true;
	      break;
	    }
	  if (found)
	    break;
	  }
	rt++;
	
	found = false;
	for (cr = c + 1; cr < grid[0].size(); cr++) {
	  for (int i = rt; i <= r; i++)
	    if (grid[i][cr] != '?') {
	      found = true;
	      break;
	    }
	  if (found)
	    break;
	}
	cr--;

	found = false;
	for (rb = r + 1; rb < grid.size(); rb++) {
	  for (int j = cl; j <= cr; j++)
	    if (grid[rb][j] != '?') {
	      found = true;
	      break;
	    }
	  if (found)
	    break;
	}
	rb--;

	for (int i = rt; i <= rb; i++)
	  for (int j = cl; j <= cr; j++)
	    grid[i][j] = grid[r][c];
      }
  
  // int r, c;
  // bool did_first = false;
  // for (int i = grid.size() - 1; i >= 0; i--)
  //   for (int j = grid[i].size() - 1; j >= 0; j--)
  //     if (grid[i][j] != '?') {
  // 	r = i;
  // 	c = j;
  //     }
  // for (int i = 0; i <= r; i++)
  //   for (int j = 0; j <= c; j++)
  //     grid[i][j] = grid[r][c];
}

