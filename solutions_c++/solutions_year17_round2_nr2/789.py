#include <iostream>

using namespace std;
int T, N, R, O, Y, G, B, V;

void imp(int t) {
  cout << "Case #" << t << ": IMPOSSIBLE\n";
}

void pr(char c1, char c2, int &x) {
  if (x == 0)
    cout << c1;
  else {
    for (int i = 0;i < x;++i) {
      cout << c1 << c2;
    }
    cout << c1;
  }
  x = 0;
}

void corner(int t, char c1, char c2, int x) {
  cout << "Case #" << t <<  ": ";

  for (int i = 0;i < x;++i) {
    cout << c1 << c2;
  }
  cout << "\n";
}

int main() {
  cin >> T;

  for (int t = 1;t <= T;++t) {
    cin >> N >> R >> O >> Y >> G >> B >> V;
    

    if (B == O && B + O == N) {
      corner(t, 'B', 'O', B);
      continue;
    }

    if (R == G && R + G == N) {
      corner(t, 'R', 'G', R);
      continue;
    }

    if (Y == V && Y + V == N) {
      corner(t, 'Y', 'V', Y);
      continue;
    }

    if ((B <= O && O > 0) || (R <= G && G > 0) || (Y <= V && V > 0)) {
      imp(t);
      continue;
    }

    B -= O;
    R -= G;
    Y -= V;
    char c1, c2, c3, c4, c5, c6;
    int a1, a2, a3, a4, a5, a6;

    if (B == max(max(B, R), Y)) {
      c1 = 'B';a1 = B;
      c2 = 'R';a2 = R;
      c3 = 'Y';a3 = Y;
      c4 = 'O';a4 = O;
      c5 = 'G';a5 = G;
      c6 = 'V';a6 = V;
    } else if (R == max(max(B, R), Y)) {
      c1 = 'R';a1 = R;
      c2 = 'B';a2 = B;
      c3 = 'Y';a3 = Y;
      c4 = 'G';a4 = G;
      c5 = 'O';a5 = O;
      c6 = 'V';a6 = V;
    } else {
      c1 = 'Y';a1 = Y;
      c2 = 'R';a2 = R;
      c3 = 'B';a3 = B;
      c4 = 'V';a4 = V;
      c5 = 'G';a5 = G;
      c6 = 'O';a6 = O;
    }
    if (a1 > a2 + a3) {
      imp(t);
      continue;
    }
    
    cout << "Case #" << t << ": ";
    int s = a2 + a3 - a1;

    for (int i = 0;i < s;++i) {
      pr(c1, c4, a4);
      pr(c2, c5, a5);
      pr(c3, c6, a6);
    }

    a2 -= s;
    a3 -= s;
    
    for (int i = 0;i < a2;++i) {
      pr(c1, c4, a4);
      pr(c2, c5, a5);
    }
    
    for (int i = 0;i < a3;++i) {
      pr(c1, c4, a4);
      pr(c3, c6, a6);
    }

    cout << "\n";
  }
  return 0;
}
