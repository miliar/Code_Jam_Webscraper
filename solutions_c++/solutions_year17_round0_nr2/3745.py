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
void print_out(int l, T ret) {
  cout << "Case #" << l << ": " << ret << endl;
}

// non-increasing (decrease or equal) in reverse
bool istidy(ull N) {
  ull last = 9;
  while(N) {
    ull tmp = N%10;
    if (tmp > last) {
      return false;
    }
    N /= 10;
    last = tmp;
  }
    
  return true;
}

int main(void) {
  int T; cin >> T; cin.ignore();
  for (int l = 1; l <= T; ++l) {
    /* DO PROBLEM STUFF HERE --> */
    ull N; cin >> N; cin.ignore();
    
    //efficient
    vector<ui> nv;
    while(N) {
      nv.push_back(N%10);
      N /= 10;
    }
    
    for(auto rit = nv.rbegin(); rit != nv.rend();) {
      auto next = rit+1;
      
      if (*next < *rit) {
        --*rit;
        for(auto rit2 = next; rit2 != nv.rend(); ++rit2) {
          *rit2 = 9;
        }
        
        rit = nv.rbegin();
      }
      else {
        ++rit;
      }
    }

    N = 0;
    ull fact10 = 1;
    for (auto x : nv) {
      N += fact10*x;
      fact10 *= 10;
    }
    
    //brute
   /*
    while(!istidy(N)) {
      --N;
    }
    */
    
    print_out(l, N);
    
    /* <-- DO PROBLEM STUFF HERE */
  }
  return 0;
}



