#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

string solve() {
    int R, O, Y, G, B, V, N;
    scanf("%d %d %d %d %d %d %d", &N, &R, &O, &Y, &G, &B, &V);
    if (O > 0 && O >= B) {
        if (O == B && O + B == N) {
            string ans = "";
            for (int i = 0; i < N; i+=2) ans += "OB";
                return ans;
        }
        return "IMPOSSIBLE";
    }
    if (V > 0 && V >= Y) {
        if (V == Y && V + Y == N) {
            string ans = "";
            for (int i = 0; i < N; i+=2) ans += "VY";
            return ans;
        }
        return "IMPOSSIBLE";
    }
    if (G > 0 && G >= R) {
        if (G == R && G + R == N) {
            string ans = "";
            for (int i = 0; i < N; i+=2) ans += "GR";
            return ans;
        }
        return "IMPOSSIBLE";
    }
    int eb = B - O;
    int er = R - G;
    int ey = Y - V;
    if (eb > er + ey) return "IMPOSSIBLE";
    if (er > eb + ey) return "IMPOSSIBLE";
    if (ey > eb + er) return "IMPOSSIBLE";
    string ans = "";
    while (eb + er + ey > 0) {
        int nb = (ans.size() == 0 || ans[ans.size()-1] != 'B') ? 2*eb : -2;
        int nr = (ans.size() == 0 || ans[ans.size()-1] != 'R') ? 2*er : -2;
        int ny = (ans.size() == 0 || ans[ans.size()-1] != 'Y') ? 2*ey : -2;
        if (ans.size() > 0) {
            if (ans[0] == 'B') nb++;
            if (ans[0] == 'Y') ny++;
            if (ans[0] == 'R') nr++;
        }
//        printf("%d -> %d %d %d\n", eb+er+ey, nb, ny, nr);
        if (nb >= std::max(nr, ny)) {
            ans += 'B';
            eb--;
            while (O > 0) {
                ans += "OB";
                O--;
            }
        } else if (nr >= ny) {
            ans += 'R';
            er--;
            while (G > 0) {
                ans += "GR";
                G--;
            }
        } else {
            ans += 'Y';
            ey--;
            while (V > 0) {
                ans += "VY";
                V--;
            }
        }
    }
    return ans;
}

int main() {
  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    cout << "Case #" << t << ": ";
    cout << solve();
    cout << "\n";
  }
  return 0;
}
