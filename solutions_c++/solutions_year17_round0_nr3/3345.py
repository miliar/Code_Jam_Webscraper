#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <map>
#include <utility>
#include <algorithm>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

typedef unsigned long long u64;

class Bathroom {
public:
  pair<u64, u64> split(u64 origin) {
    u64 half = origin/2;
    if (origin % 2) {
      //odd
      return make_pair(half, half);
    }
    else {
      // even
      return make_pair(half-1, half);
    }
  }

  string findStall(u64 numStall, u64 numPeople) {
    map<u64, u64> stalls;
    stalls[numStall]++;
    pair<u64, u64> result;
    while (numPeople) {
      // cout << numPeople << endl;
      map<u64, u64>::iterator it = stalls.end();
      it--;
      u64 maxR = it->first;
      u64 numR = it->second;
      stalls.erase(it);
      // if (it->second > 1) {
      //   (it->second)--;
      // }
      // else {
      //   stalls.erase(it);
      // }
      result = split(maxR);
      if (result.first) {
        stalls[result.first] += numR;
      }
      if (result.second) {
        stalls[result.second] += numR;
      }

      if (numPeople > numR) {
        numPeople -= numR;
      }
      else {
        break;
      }
    }
    return to_string(max(result.first, result.second))+" "+to_string(min(result.first, result.second));    
  }
};

int main() {
  int t;
  string number;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  u64 numStall = 0;
  u64 numPeople = 0;
  Bathroom bath;
  for (int i = 1; i <= t; ++i) {
    cin >> numStall >> numPeople;
    cout << "Case #" << i << ": " << bath.findStall(numStall, numPeople) << endl;
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
    // out put
    // Case #x: y
  }
}