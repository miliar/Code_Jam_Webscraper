#include <iostream>
#include <cstring>

#include <string>
#include <vector>
#include <algorithm>

#include <cassert>

using namespace std;

#define SZ(a) int((a).size())
#define REP(i,n) for(int i=0,_n=(n);i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)

typedef long long llong;
typedef vector<int> VI;
typedef vector<VI> VVI;

int R, C;
vector< string > B;

void solve() {
   int r = 0;
   while (true) {
      if (B[r].find_first_not_of("?") != string::npos)
         break;
      ++r;
      assert(r < R);
   }

   const int startr = r;
   for (; r < R; ++r) {
      size_t startc = B[r].find_first_not_of("?");
      if (startc == string::npos) {
         B[r] = B[r-1];
         continue;
      }
      char lastch = B[r][startc];
      for (int c = startc+1; c < C; ++c) {
         if (B[r][c] == '?') {
            B[r][c] = lastch;
         }
         else {
            lastch = B[r][c];
         }
      }
      for (int c = int(startc)-1; c >= 0; --c) {
         B[r][c] = B[r][startc];
      }
   }

   for (r = startr-1; r >= 0; --r)
      B[r] = B[startr];
}

int main(int argc, char* argv[]) {
   ios_base::sync_with_stdio(false); 
   cin.tie(NULL);

   int TC;
   cin >> TC;
   FOR(tc, 1, TC) {
      cin >> R >> C;
      B = vector<string>(R);
      REP(r, R)
         cin >> B[r];
      cout << "Case #" << tc << ":\n";
      solve();
      REP(r, R)
         cout << B[r] << '\n';
   }

   return 0;
}
