#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <math.h>
#include <fstream>
#include <thread>
#include <assert.h>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <array>
#include <sstream>
#include <set>
#include <map>
#include <list>
#include <time.h>
#include <iomanip>
#include <forward_list>

using namespace std;

int main(int argc, const char * argv[]) {
  freopen("/Users/efimovmichael/Downloads/b1.txt","r",stdin);
  freopen("/Users/efimovmichael/b.out","w",stdout);

  int t;
  cin >> t;
  for (int tc = 1; tc <= t; ++tc) {
    int N, R, O, Y, G, B, V;
    cin >> N >> R >> O >> Y >> G >> B >> V;
    string s;
    while(1) {
      if (G > R) {
        break;
      }
      if (G == R && G > 0) {
        if (O == 0 && Y == 0 && B == 0 && V == 0) {
          while (G > 0 && R > 0) {
            s += "RG";
            --G;
            --R;
          }
        }
        break;
      }
      if (V > Y) {
        break;
      }
      if (V == Y && V > 0) {
        if (O == 0 && R == 0 && B == 0 && G == 0) {
          while (Y > 0 && V > 0) {
            s += "YV";
            --Y;
            --V;
          }
        }
        break;
      }
      if (O > B) {
        break;
      }
      if (O == B && O > 0) {
        if (Y == 0 && R == 0 && V == 0 && G == 0) {
          while (B > 0 && O > 0) {
            s += "BO";
            --B;
            --O;
          }
        }
        break;
      }
      while (R > 0 || Y > 0 || B > 0) {
        char maxc = 0;
        int count = 0;
        if (s.empty() || s.back() != 'R') {
          if (count < R) {
            count = R;
            maxc = 'R';
          }
        }
        if (s.empty() || s.back() != 'Y') {
          if (count < Y) {
            count = Y;
            maxc = 'Y';
          }
        }
        if (s.empty() || s.back() != 'B') {
          if (count < B) {
            count = B;
            maxc = 'B';
          }
        }
        if (maxc == 'R') {
          --R;
          s += 'R';
        }
        if (maxc == 'Y') {
          --Y;
          s += 'Y';
        }
        if (maxc == 'B') {
          --B;
          s += 'B';
        }
        if (maxc == 0) {
          s.clear();
          break;
        }
      }
      if (!s.empty() && s.front() == s.back()) {
        if (s.size() > 2) {
          if (s[s.size() - 3] != s[s.size() - 2] && s[s.size() - 3] != s[s.size() - 1]) {
            char tmp = s[s.size() - 2];
            s[s.size() - 2] = s[s.size() - 1];
            s[s.size() - 1] = tmp;
            break;
          }
        }
        s.clear();
      }
      if (!s.empty()) {
        char prev = 0;
        for (char c : s) {
          if (c == prev) {
            cout<< "Bad";
          }
          prev = c;
        }
      }
      break;
    }
    if (s.empty()) {
      s = "IMPOSSIBLE";
    }
    cout << "Case #" << tc << ": " << s << endl;
  }

  fclose(stdin);
  fclose(stdout);
  return 0;
}
