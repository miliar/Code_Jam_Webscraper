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

bool flip(string& pancakes, size_t idx, size_t k)
{
  size_t numFlipped = 0;
  for (size_t i = idx; i < pancakes.length(); i++)
  {
    pancakes[i] = (pancakes[i] == '-' ? '+' : '-');
    if (++numFlipped == k) break;
  }
  //cout << "idx " << idx << " k " << k << " numFlipped " << numFlipped << endl;
  return numFlipped == k;
}

int main(int argc, char** argv)
{
  ifstream input(argv[1]);

  size_t T;
  input >> T;

  for (size_t t = 1; t <= T; t++)
  {
    string pancakes;
    size_t k;
    input >> pancakes;
    input >> k;

    size_t numFlips = 0;
    bool impossible = false;
    for (size_t i = 0; i < pancakes.length(); i++)
    {
      if (pancakes[i] == '+') continue;
      if (!flip(pancakes, i, k))
      {
        impossible = true;
        break;
      }
      numFlips++;
    }

    if (impossible)
    {
      cout << "Case #" << t << ": IMPOSSIBLE" << endl;
      continue;
    }
    cout << "Case #" << t << ": " << numFlips << endl;
  }

  return 0;
}
