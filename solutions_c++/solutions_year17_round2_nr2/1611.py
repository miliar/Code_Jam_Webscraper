#include <iostream>
#include <sstream>
#include <queue>
#include <utility>

using namespace std;

int T;
int N, color[6];

const static bool MX[6][6] = {
// R  O  Y  G  B  V  
  {0, 0, 1, 1, 1, 0}, // R
  {0, 0, 0, 0, 1, 0}, // O
  {1, 0, 0, 0, 1, 1}, // Y
  {1, 0, 0, 0, 0, 0}, // G
  {1, 1, 1, 0, 0, 0}, // B
  {0, 0, 1, 0, 0, 0}  // V
};

const static string cs = "ROYGBV";

string small_solve() {
  int mx = max(max(color[0], color[2]), color[4]);
  int mi = min(min(color[0], color[2]), color[4]);
  int md = N - mx - mi;
  if (mi + md < mx) {
    return "IMPOSSIBLE";
  }

  char res[N+1];
  res[N] = '\0';
  int last = -1; 
  for (int i = 0; i < N; ++i) {
    int tmp = 0, ix = -1;
    for (int j = 0; j < 6; j += 2) {
      if (last == j || color[j] == 0) {
        continue;
      }
      if (color[j] >= tmp) {
        tmp = color[j];
        ix = j;
      }
    }
    res[i] = cs[ix];
    color[ix]--;
    last = ix;
  }
  
  if (res[0] == res[N-1]) {
    for (int i = 1; i < N-1; ++i) {
      if (res[i] != res[N-1] && res[i-1] != res[N-1]) {
        for (int j = 0; i + j < N - 1 - j; ++j) {
          swap(res[i+j], res[N-1-j]);
        }
        return string(res);
      }
    }
    cerr << "wakaka" << endl;
    return "IMPOSSIBLE";
  }
  return string(res);
}

int main() {
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cin >> N;
    for (int i = 0; i < 6; ++i) {
      cin >> color[i];
    }
    cout << "Case #" << t << ": " << small_solve() << endl;
  }

  return 0;
}