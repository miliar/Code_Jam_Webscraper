#include <stdio.h>
#include <string>
#include <algorithm>

using namespace std;

int n, r, o, y, g, b, v;

char str[1024];

int main() {
  int T;
  scanf("%d", &T);

  for (int t = 1; t <= T; t++) {
    printf("Case #%d: ", t);
    scanf("%d%d%d%d%d%d%d", &n, &r, &o, &y, &g, &b, &v);

    string result;

    if (r == g && !y && !v && !b && !o) {
      for (int i = 0; i < r; i++) {
        result.insert(0, "RG");
      }
    }
    if (y == v && !r && !g && !b && !o) {
      for (int i = 0; i < y; i++) {
        result.insert(0, "YV");
      }
    }
    if (b == o && !r && !g && !y && !v) {
      for (int i = 0; i < b; i++) {
        result.insert(0, "BO");
      }
    }

    if (r + o + y + g + b + v == 1) {
      char c;
      if (r) {
        c = 'R';
      } else if (o) {
        c = 'O';
      } else if (y) {
        c = 'Y';
      } else if (g) {
        c = 'G';
      } else if (b) {
        c = 'B';
      } else if (v) {
        c = 'V';
      }
      printf("%c\n", c);
      continue;
    }

    if (result.length()) {
      printf("%s\n", result.c_str());
      continue;
    }

    if ((g && r <= g) || (v && y <= v) || (o && b <= o)) {
      printf("IMPOSSIBLE\n");
      continue;
    }

    r -= g;
    y -= v;
    b -= o;

    if (r > y + b ||
        y > r + b ||
        b > y + r) {
      printf("IMPOSSIBLE\n");
      continue;
    }

    int most = max(r, max(y, b));

    int *big, *small, *little;
    char *letters;
    if (r == most) {
      big = &r;
      small = &y;
      little = &b;
      letters = "RYB";
    } else if (y == most) {
      big = &y;
      small = &b;
      little = &r;
      letters = "YBR";
    } else if (b == most) {
      big = &b;
      small = &r;
      little = &y;
      letters = "BRY";
    }

    result.insert(0, *big, letters[0]);
    for (int i = 0; i < *small; i++) {
      result.insert(i * 2 + 1, 1, letters[1]);
    }
    for (int i = 0; i < *little; i++) {
      result.insert(result.length() - 2 * i, 1, letters[2]);
    }

    if (g) {
      size_t pos = result.find('R');
      for (int i = 0; i < g; i++) {
        result.insert(pos, "RG");
      }
    }
    if (v) {
      size_t pos = result.find('Y');
      for (int i = 0; i < v; i++) {
        result.insert(pos, "YV");
      }
    }
    if (o) {
      size_t pos = result.find('B');
      for (int i = 0; i < o; i++) {
        result.insert(pos, "BO");
      }
    }

    printf("%s\n", result.c_str());
  }

  return 0;
}
