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

typedef pair<size_t, size_t> Range;

int main(int argc, char** argv)
{
  ifstream input(argv[1]);

  size_t T;
  input >> T;

  for (size_t t = 1; t <= T; t++)
  {
    size_t N, K;
    input >> N >> K;

    map<size_t, set<size_t>> spaceLenToRangeSetMap;

    spaceLenToRangeSetMap[N].insert(1);

    size_t Ls = 0;
    size_t Rs = 0;
    for (size_t k = 0; k < K; k++)
    {
      auto iter = spaceLenToRangeSetMap.rbegin();
      auto spaceLen = iter->first;
      auto& rangeSet = iter->second;

      assert(!rangeSet.empty());

      auto rangeStart = *(rangeSet.begin());
      rangeSet.erase(rangeStart);

      if (rangeSet.empty()) spaceLenToRangeSetMap.erase(iter->first);

      Range rangePicked = make_pair(rangeStart, rangeStart + spaceLen - 1);
      size_t newStallIdx = rangePicked.first + ((rangePicked.second - rangePicked.first) / 2);

      if (newStallIdx > rangePicked.first)
        spaceLenToRangeSetMap[(newStallIdx - rangePicked.first)].insert(rangePicked.first);

      if (newStallIdx < rangePicked.second)
        spaceLenToRangeSetMap[(rangePicked.second - newStallIdx)].insert(newStallIdx + 1);

      Ls = newStallIdx - rangePicked.first;
      Rs = rangePicked.second - newStallIdx;
    }

    cout << "Case #" << t << ": " << max(Ls, Rs) << " " << min(Ls, Rs) << endl;
  }

  return 0;
}
