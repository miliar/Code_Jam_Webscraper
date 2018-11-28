/* GCJ 2017 Round 1A Problem A */

#include <iostream>
#include <vector>
#include <set>

using namespace std;

#define DEBUG0
// #define DEBUG
#define ITER(typ,it,foo) for (typ::iterator it = foo.begin(); it != foo.end(); it++)

void print_cake(vector<string> &cake) {
  for (unsigned i = 0; i < cake.size(); i++) {
    cerr << "[" << cake[i] << "]" << endl;
  }
}

bool all_qs(vector<string> &cake, int i_top, int i_bot, int jj) {
  for (unsigned ii = i_top; ii <= i_bot; ii++)
    if (cake[ii][jj] != '?') return false;
  return true;
}

void fill_col(vector<string> &cake, int i_top, int i_bot, int jj, char initial) {
  for (unsigned ii = i_top; ii <= i_bot; ii++) {
#ifdef DEBUG
    if (cake[ii][jj] != '?') cerr << "BUG in fill_col" << endl;
#endif
    cake[ii][jj] = initial;
  }
}

void testcase(int case_no)
{
  int R, C; cin >> R >> C; // -- rows and columns of the cake
  vector<string> cake;
  for (unsigned i = 0; i < R; i++) {
    string row; cin >> row;
    cake.push_back(row);
  }
#ifdef DEBUG0
  cerr << "Raw cake #" << case_no << ":" << endl;
  print_cake(cake);
#endif

  // Greedy strategy. [Manually corrected bug where it doesn't work]
  // Collect initials:
  set<char> seen_initials;
  for (unsigned i = 0; i < R; i++) {
    for (unsigned j = 0; j < C; j++) {
      if (cake[i][j] != '?') {
        char initial = cake[i][j];
        if (seen_initials.count(initial) > 0) continue;
        seen_initials.insert(initial);

        // Expand up:
        int ii, jj, i_top, i_bot;
        for (ii = i-1; ii >= 0; ii--)
          if (cake[ii][j] == '?')
            cake[ii][j] = initial;
          else break;
        i_top = ii+1;

        // Expand down:
        for (ii = i+1; ii < R; ii++)
          if (cake[ii][j] == '?')
            cake[ii][j] = initial;
          else break;
        i_bot = ii-1;

        // Expand left:
        for (jj = j-1; jj >= 0; jj--)
          if (all_qs(cake, i_top, i_bot, jj))
            fill_col(cake, i_top, i_bot, jj, initial);
          else break;

        // Expand right:
        for (jj = j+1; jj < C; jj++)
          if (all_qs(cake, i_top, i_bot, jj))
            fill_col(cake, i_top, i_bot, jj, initial);
          else break;
#ifdef DEBUG
      cerr << "Expanded '" << initial << "':" << endl;
      print_cake(cake);
#endif
      }
    }
  }

  cout << "Case #" << case_no << ": " << endl;
  for (unsigned i = 0; i < R; i++) {
    cout << cake[i] << endl;
  }
}

int main()
{
  int T; cin >> T;
  for (int i = 0; i < T; i++)
    testcase(i+1);
  return 0;
}
