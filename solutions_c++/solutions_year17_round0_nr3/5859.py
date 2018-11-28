#include <cassert>
#include <cstdio>
#include <iostream>
#include <set>
#include <vector>

using namespace std;

int main() {
  int T = 0;
  cin >> T;
  int cases = 0;

  for(cases = 1; cases <= T; cases++) {
    int n, k;
    cin >> n >> k;
    set < int > s;
    // 0th and n+1 positions are already taken.
    s.insert(0);
    s.insert(n+1);
    for(int i = 0; i < k; i++) {

      int fd = -1;
      int fd_max = -1;
      int jpos = -1;
      for(int j = 1; j < n + 2; j++) {
        if (s.find(j) != s.end()) {
          continue;
        }
        // For each position, try to find the next bigger and smaller elements.
        int smaller = 0;
        int bigger = n+1;
        for(set<int>::iterator it = s.begin(); it != s.end(); it++) {
          int pos = *it;
          if(pos < j && pos > smaller) { 
            smaller = pos;
          }
          if(pos > j && pos < bigger) {
            bigger = pos;
          }
        }
   //     cout << j << " " << smaller << " " << bigger << endl; 
        // smaller, bigger are the closest neighbors of j.
        int jfd = min(j-smaller-1, bigger-j-1);
        int jfd_max = max(j-smaller-1, bigger-j-1);
        if (jfd == fd && jfd_max > fd_max) {
          fd_max = jfd_max;
          jpos = j;
        }
        else if(jfd > fd) {
          fd = jfd;
          fd_max = jfd_max;
          jpos = j;
        }  
      }
      assert(jpos != -1);
      if (i == k-1) {
        printf("Case #%d: %d %d\n",cases, fd_max, fd);
      } 
      s.insert(jpos);
    }


  
  }
}
