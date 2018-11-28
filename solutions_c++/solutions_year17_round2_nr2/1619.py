#include <algorithm>
#include <fstream>
#include <iostream>
#include <stdio.h>
#include <string.h>
#include <unordered_set>
#include <vector>

struct slot {
  int R;
  int O;
  int Y;
  int G;
  int B;
  int V;
};

enum utype { red = 1, yellow = 2, blue = 4 };

int main(int argc, char** argv) {
  if (argc <= 2) return -1;

  std::ifstream ifs(argv[1]);
  std::ofstream ofs(argv[2]);
  int nCase = 0;
  ifs >> nCase;
  std::cout << "#Cases: " << nCase << std::endl;
  char result[1001];
  for (size_t i = 0; i < nCase; ++i) {
    int N, R, O, Y, G, B, V;
    ifs >> N >> R >> O >> Y >> G >> B >> V;

    std::cout << "Case #" << i + 1 << ": ";
    ofs << "Case #" << i + 1 << ": ";

    if (R + B < Y || R + Y < B || Y + B < R) {
      std::cout << "IMPOSSIBLE" << std::endl;
      ofs << "IMPOSSIBLE" << std::endl;
    } else {
      int cur_pos = 0;
      do {
        if (R > 0) {
          result[cur_pos++] = 'R';
          R--;
        }
        int remaining_slots = R;

        utype last_placed = utype::red;
        while (Y + B > remaining_slots) {
          switch (last_placed) {
          case utype::red:
            if (Y >= B) {
              result[cur_pos++] = 'Y';
              last_placed = utype::yellow;
              Y--;
            } else {
              result[cur_pos++] = 'B';
              last_placed = utype::blue;
              B--;
            }
            break;
          case utype::yellow:
            result[cur_pos++] = 'B';
            last_placed = utype::blue;
            B--;
            break;
          case utype::blue:
            result[cur_pos++] = 'Y';
            last_placed = utype::yellow;
            Y--;
            break;
          default:
            break;
          }
        }
      } while (R > 0);
      result[cur_pos++] = 0;
      std::string sresult(result);
      std::cout << sresult << std::endl;
      ofs << sresult << std::endl;
    }
  }
}
