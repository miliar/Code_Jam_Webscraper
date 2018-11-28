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
    string N;
    input >> N;

    size_t changeIdx = N.length();
    for (int i = (int)(N.length()-1); i > 0; i--)
    {
      if (N[(size_t)i] >= N[(size_t)(i-1)]) continue;
      N[(size_t)(i-1)]--;
      changeIdx = (size_t)(i-1);
    }

    string newN;
    if (changeIdx < N.length())
    {
      for (size_t i = 0; i <= changeIdx; i++)
      {
        if (N[i] == '0') continue;
        newN.append(1, N[i]);
      }
      for (size_t i = changeIdx+1; i < N.length(); i++)
        newN.append(1, '9');
    }
    else
    {
      newN = N;
    }


    cout << "Case #" << t << ": " << newN << endl;
  }

  return 0;
}
