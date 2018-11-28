#include <cmath>
#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <sstream>
#include <iostream>
using namespace std;

fstream in, out;

int T;
int N, P;
vector<int> sizes;
vector<int> mods;
int ans;

int min(int x, int y) { if (x < y) { return x;} return y;}
int max(int x, int y) { if (x > y) { return x;} return y;}

int main() {
  in.open("A-small-attempt0.in", fstream::in);
  out.open("proba-small0.out", fstream::out);

  in >> T;
  for (int i = 0; i < T; ++i) {
    ans = 0;
    sizes.clear();
    mods.clear();
    mods.resize(4, 0);
    in >> N >> P;
    for (int j = 0; j < N; ++j) {
      int temp;
      in >> temp;
      sizes.push_back(temp);
      ++mods[temp % P];
    }

    if (P == 2) {
      ans = mods[0] + (mods[1] + 1) / 2;
    } else if (P == 3) {
      ans += mods[0];
      ans += min(mods[1], mods[2]);
      ans += (max(mods[1], mods[2]) - min(mods[1], mods[2]) + 2) / 3;
    } else if (P == 4) {
      ans += mods[0];
      int min13 = min(mods[1], mods[3]);
      ans += min13;
      mods[1] -= min13;
      mods[3] -= min13;
      ans += mods[2] / 2;
      mods[2] = mods[2] % 2;
      int rem = mods[1] + mods[3];
      if (mods[2] > 0 && rem >= 2) {
        ++ans;
        rem -= 2;
      }
      ans += (rem + 3) / 4;        
    }
    

    out << "Case #" << i + 1 << ": " << ans << endl;
  }
    
  in.close();
  out.close();
  return 0;
}
