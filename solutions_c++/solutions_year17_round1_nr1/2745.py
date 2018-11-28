#include <iostream>
#include <cstring>
#include <strings.h>
#include <set>

#ifdef ALGO_DEBUG
#include "../test/debug.cpp"
#else

#define TRACE(message)
#define TRACE_LINE(message)
#define ASSERT(expr)
#define UNIT_TESTS()

#endif

class Mat {
 public:
  char* data;
  int R, C;
  std::set<char> alphabet;

  Mat(int r, int c) : R{r}, C{c}, data{new char[r * (c + 1) + 1]} {
    data[r * (c + 1)] = '\0';
  }

  ~Mat() {
    delete[] data;
  }

  bool verifyRegion(int r1, int c1, int r2, int c2, char letter) {
    for(int r = 0; r < R; ++r) {
      for(int c = 0; c < C; ++c) {
        if(r >= r1 && c >= c1 && r <= r2 && c <= c2) {
          if(data[r * (C + 1) + c] != letter) {
            return false;
          }
        } else {
          if(data[r * (C + 1) + c] == letter) {
            return false;
          }
        }
      }
    }
    return true;
  }

  bool whatever() {
    char* pos = index(data, '?');
    if(pos == NULL) {
      for(char c : alphabet) {
        char *start_c = index(data, c);
        char *end_c = rindex(data, c);
        int start = start_c - data;
        int end = end_c - data;
        if(!verifyRegion(start / (C + 1), start % (C + 1), end / (C + 1), end % (C + 1), c)) {
          return false;
        }
      }
      return true;
    } else {
      for(char c : alphabet) {
        *pos = c;
        if(whatever()) return true;
      }
      *pos = '?';
      return false;
    }
  }

  void putline(int r, char *line) {
    std::memcpy(data + (r * (C + 1)), line, C);
    data[(r + 1) * (C + 1) - 1] = '\n';
    for(int i = 0; i < C; ++i) {
      if(line[i] != '?') {
        alphabet.insert(line[i]);
      }
    }
  }
};

void solve(int t) {
  int r, c;
  std::cin >> r >> c;
  Mat mat{r, c};
  char line[c + 1];
  for(int i = 0; i < r; ++i) {
    std::cin >> line;
    mat.putline(i, line);
  }
  mat.whatever();
  std::cout << "Case #" << t << ":\n";
  std::cout << mat.data;
}

void unit_tests() {
}

int main() {
  UNIT_TESTS();
  int T;
  std::cin >> T;
  for(int t = 1; t <= T; ++t) {
    solve(t);
  }
  return 0;
}
