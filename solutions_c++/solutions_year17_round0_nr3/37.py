#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <sstream>
using namespace std;

template<class P0, class P1> ostream &operator<<(ostream &os, const pair<P0, P1> &p) { return os << "(" << p.first << "," << p.second << ")"; }
template<class T> void dump(const T &t) { cerr << "["; for (auto it = t.begin(); it != t.end(); ++it) cerr << " " << *it; cerr << " ]" << "\n"; } 

#include <boost/multiprecision/cpp_int.hpp>
using namespace boost::multiprecision;
#define Integer cpp_int

int main(void) {
  int T; cin >> T;
  
  for (int iCase = 1; iCase <= T; ++iCase) {
    cout << "Case #" << iCase << ":";
    Integer i, n, k; cin >> n >> k;
    
    map<Integer, Integer> blockCounts;
    blockCounts[-n] = 1;

    Integer left, right;
    while (k > 0) {
      Integer block = -blockCounts.begin()->first;
      Integer count = blockCounts.begin()->second;

      --block;
      right = block/2;
      left = block - right;

      Integer toSplit = count;
      if (toSplit > k) toSplit = k;
      k -= toSplit;

      blockCounts.begin()->second -= toSplit;
      if (blockCounts.begin()->second==0) blockCounts.erase(blockCounts.begin());

      map<Integer, Integer>::iterator it;

      it = blockCounts.find(-left);
      if (it==blockCounts.end())
	blockCounts[-left] = toSplit;
      else
	it->second += toSplit;

      it = blockCounts.find(-right);
      if (it==blockCounts.end())
	blockCounts[-right] = toSplit;
      else
	it->second += toSplit;
    }

    cout << " " << left << " " << right;

    cout << "\n";
  }

  return 0;
}
