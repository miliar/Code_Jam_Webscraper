#include <iostream>
#include <string>
#include <algorithm>

void print(int caseNum, std::string output) {
  std::cout << "Case #" << caseNum << ": " << output << std::endl;
}

int main() {
  int T;
  scanf("%d", &T);

  for (int t = 1; t <= T; ++t) {
    int N;
    int R, O, Y, G, B, V;
    scanf("%d %d %d %d %d %d %d", &N, &R, &O, &Y, &G, &B, &V);

    char RYBcharArr[3];
    int RYBarr[3] = { R, Y, B };
    std::sort(RYBarr, RYBarr+3);

    std::string output;
    // if (R + Y < B || R + B < Y || B + Y < R) {
    if (RYBarr[0] + RYBarr[1] < RYBarr[2]) {
      output = "IMPOSSIBLE";
      print(t, output);
    } else {
      if (R >= Y && R >= B) {
        RYBcharArr[2] = 'R';
        if (Y >= B) { RYBcharArr[1] = 'Y'; RYBcharArr[0] = 'B'; }
        else { RYBcharArr[1] = 'B'; RYBcharArr[0] = 'Y'; }
      } else if (Y >= R && Y >= B) {
        RYBcharArr[2] = 'Y';
        if (R >= B) { RYBcharArr[1] = 'R'; RYBcharArr[0] = 'B'; }
        else { RYBcharArr[1] = 'B'; RYBcharArr[0] = 'R'; }
      } else if (B >= R && B >= Y) {
        RYBcharArr[2] = 'B';
        if (R >= Y) { RYBcharArr[1] = 'R'; RYBcharArr[0] = 'Y'; }
        else { RYBcharArr[1] = 'Y'; RYBcharArr[0] = 'R'; }
      }

      for (int i = 0; i < RYBarr[0] + RYBarr[1] - RYBarr[2]; ++i) {
        output += RYBcharArr[2];
        output += RYBcharArr[1];
        output += RYBcharArr[0];
      }
      for (int i = 0; i < RYBarr[2] - RYBarr[0]; ++i) {
        output += RYBcharArr[2];
        output += RYBcharArr[1];
      }
      for (int i = 0; i < RYBarr[2] - RYBarr[1]; ++i) {
        output += RYBcharArr[2];
        output += RYBcharArr[0];
      }

      print(t, output);
    }
  }

  return 0;
}
