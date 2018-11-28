#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>
#include <cmath>
#include <algorithm>
using namespace std;

typedef unsigned char uc;
typedef unsigned int  ui;
typedef unsigned long ul;
typedef unsigned long long ull;

template <class T>
void print_out(int l, T L, T R) {
  cout << "Case #" << l << ": " << L << " " << R << endl;
}

struct range {
  ull size;
  ull start;
  range(ull size0, ull start0) : size(size0), start(start0) {}
  
  bool operator< (const range& other) const {
    if (size == other.size) {
      return start < other.start;
    }
    return size > other.size;
  }
};

int main(void) {
  int T; cin >> T; cin.ignore();
  for (int l = 1; l <= T; ++l) {
    /* DO PROBLEM STUFF HERE --> */
    int N; cin >> N; cin.ignore();
    int K; cin >> K; cin.ignore();

    // range size to starting index
    set<range> ranges;
    ranges.insert(range(N,0));

    for (int k = 1; k <= K; ++k) {
      // biggest and leftmost range      
      auto it = ranges.begin();
      
      ull Ls = (it->size-1)/2;
      ull Rs = (it->size) - Ls - 1;
      
      //cerr <<Ls<<" "<<Rs<<" "<<it->size<<" "<<it->start<<endl;
      
      // print last chosen
      if (k == K) {
        print_out(l, max(Ls,Rs), min(Ls,Rs));
      }
      
      //update ranges
      ranges.erase(it);
      if (Ls != 0) {
        ranges.insert(range(Ls, it->start));
      }
      if (Rs != 0) {
        ranges.insert(range(Rs, Ls+it->start+1));
      }
    }
    //cerr<<endl;
    
    /* <-- DO PROBLEM STUFF HERE */
  }
  return 0;
}



