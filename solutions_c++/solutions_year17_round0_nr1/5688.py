/*
Input:
3
---+-++- 3
+++++ 4
-+-+- 4

Output:
Case #1: 3
Case #2: 0
Case #3: IMPOSSIBLE
*/
#include <iostream>
#include <string>

using namespace std;

int
main() {
  int T;

  cin >> T;

  for(int c = 1; c <= T; c++) {
    string s;
    int w;
    cin >> s >> w;

    int n = 0;

    cout << "Case #" << c << ": ";
    char* cs = (char*)s.c_str();
    char* cs0 = cs;

    while(((*cs) != 0) && (n != -1)) {
      if((*cs) == '-') {
        n++;

        int i = w;
        char* cs2 = cs;
        while((i > 0) && ((*cs2) != 0)) {
          (*cs2) = (*cs2) == '-' ? '+' : '-';
          i--;
          cs2++;
        }
        if(i != 0) {
          n = -1;
        }

      }
      cs++;
    }

    if(n < 0) {
      cout << "IMPOSSIBLE";
    } else {
      cout << n;
    }

    cout << endl;
  }
}
