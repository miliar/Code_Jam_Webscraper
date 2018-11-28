#include <algorithm>
#include <cassert>
#include <cmath>
#include <iostream>
#include <map>
#include <vector>
#include <set>
#include <string>

using namespace std;

int T, N, R, O, Y, G, B, V;
char relation[3];
char s2l[256];

const string kImp = "IMPOSSIBLE";

int get_index(string& ans, int index, char c) {
  if (c == 'R') {
    if (G > 0) {
      for (int i = 0; i < G; i++) {
        ans[index++] = 'R';
        ans[index++] = 'G';
      }
      G = 0;
    }
    ans[index++] = 'R';
  } else if (c == 'Y') {
    if (V > 0) {
      for (int i = 0; i < V; i++) {
        ans[index++] = 'Y';
        ans[index++] = 'V';
      }
      V = 0;
    }
    ans[index++] = 'Y';
  } else if (c == 'B') {
    if (O > 0) {
      for (int i = 0; i < O; i++) {
        ans[index++] = 'B';
        ans[index++] = 'O';
      }
      O = 0;
    }
    ans[index++] = 'B';
  }
  return index;
}

string solve() {
  int r, y, b;

  if (O == 1 && N == 1) {
    return "O";
  }
  if (G == 1 && N == 1) {
    return "G";
  }
  if (V == 1 && N == 1) {
    return "V";
  }

  if (O > 0 && B < O ||
      G > 0 && R < G ||
      V > 0 && Y < V) {
    return kImp;
  }

  string ans(N, ' ');

  if (O > 0 && B == O) {
    if (N == B + O) {
      for (int i = 0; i < N; i+=2) {
        ans[i] = 'B';
        ans[i+1] = 'O';
      }
      return ans;
    }
    return kImp;
  }

  if (G > 0 && R == G) {
    if (N == R + G) {
      for (int i = 0; i < N; i+=2) {
        ans[i] = 'R';
        ans[i+1] = 'G';
      }
      return ans;
    }
    return kImp;
  }

  if (V > 0 && Y == V) {
    if (N == Y + V) {
      for (int i = 0; i < N; i+=2) {
        ans[i] = 'Y';
        ans[i+1] = 'V';
      }
      return ans;
    }
    return kImp;
  }

  R -= G;
  Y -= V;
  B -= O;

  if (R >= max(Y, B)) {
    relation[0] = 'R';
    r = R;
    if (Y >= B) {
      y = Y;
      b = B;
      relation[1] = 'Y';
      relation[2] = 'B';
    } else {
      y = B;
      b = Y;
      relation[1] = 'B';
      relation[2] = 'Y';
    }
  } else if (Y >= max(R, B)) {
    relation[0] = 'Y';
    r = Y;
    if (R >= B) {
      y = R;
      b = B;
      relation[1] = 'R';
      relation[2] = 'B';
    } else {
      y = B;
      b = R;
      relation[1] = 'B';
      relation[2] = 'R';
    }
  } else {
    relation[0] = 'B';
    r = B;
    if (R >= Y) {
      y = R;
      b = Y;
      relation[1] = 'R';
      relation[2] = 'Y';
    } else {
      y = Y;
      b = R;
      relation[1] = 'Y';
      relation[2] = 'R';
    }
  }

  if (r > y + b) {
    return "IMPOSSIBLE";
  }

  int y_c = r - b;
  int b_c = r - y;
  int c_c = (y + b) - r;

  int index = 0;
  while (index < N) {
    //cout << "index=" << index << " N=" << N << " c_c=" << c_c << " y_c=" << y_c << " b_c=" << b_c << endl;

    if (c_c > 0) {
      c_c--;
      index = get_index(ans, index, relation[0]);
      index = get_index(ans, index, relation[1]);
      index = get_index(ans, index, relation[2]);
      continue;
    }

    if (y_c > 0) {
      y_c--;
      index = get_index(ans, index, relation[0]);
      index = get_index(ans, index, relation[1]);
      continue;
    }

    if (b_c > 0) {
      b_c--;
      index = get_index(ans, index, relation[0]);
      index = get_index(ans, index, relation[2]);
      continue;
    }

    assert(false);
  }
  assert(ans[N - 1] != ' ');
  return ans;
}

int main() {
  cin >> T;
  for (int i = 1; i <= T; i++) {
    cin >> N >> R >> O >> Y >> G >> B >> V;
    cout << "Case #" << i << ": " << solve() << endl;
  }
  return 0;
}
