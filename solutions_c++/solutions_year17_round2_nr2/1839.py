#include<iostream>
#include<string>
#include<vector>
using namespace std;

const int R = 0, O = 1, Y = 2, G = 3, B = 4, V = 5, NCOLORS = 6;
const char COLOR[NCOLORS] = {'R', 'O', 'Y', 'G', 'B', 'V'};
vector< vector<int> > COLLITIONS(NCOLORS);

int argmax(int ponies[], vector<int>& ignore, int first) {
  int res = -1;
  int max_val = 0;
  int j = 0;
  for (int i = 0; i < NCOLORS; ++i) {
    if (ponies[i] == 0) continue;
    while (j < (int)ignore.size() and i > ignore[j]) ++j;
    if (j < (int)ignore.size() and i == ignore[j]) continue;
    int val = 0;
    for (int k = 0; k < (int)COLLITIONS[i].size(); ++k) {
      val += ponies[COLLITIONS[i][k]];
      if (COLLITIONS[i][k] == first) ++val;
    }
    if (val > max_val) {
      max_val = val;
      res = i;
    }
  }
  return res;
}

int main() {
  int T;
  cin >> T;
  COLLITIONS[R] = {R, O, V};
  COLLITIONS[O] = {R, O, Y, G, V};
  COLLITIONS[Y] = {O, Y, G};
  COLLITIONS[G] = {O, Y, G, B, V};
  COLLITIONS[B] = {G, B, V};
  COLLITIONS[V] = {R, O, G, B, V};
  for (int cas = 1; cas <= T; ++cas) {
    int N;
    int ponies[NCOLORS];
    cin >> N;
    for (int i = 0; i < NCOLORS; ++i) {
      cin >> ponies[i];
    }
    bool possible = (ponies[R] <= N/2) and (ponies[Y] <= N/2) and (ponies[B] <= N/2);
      string sol = "";
    if (possible) {
      vector<int> collitions(0);
      int first = -1;
      for (int i = 0; i < N and possible; ++i) {
        int color = argmax(ponies, collitions, first);
        if (color == -1) {
          possible = false;
        }
        else {
          sol += COLOR[color];
          --ponies[color];
          collitions = COLLITIONS[color];
          if (first == -1) first = color;
        }
      }
    }
    
    cout << "Case #" << cas << ": ";
    if (possible) cout << sol;
    else cout << "IMPOSSIBLE";
    cout << endl;
  }
}
