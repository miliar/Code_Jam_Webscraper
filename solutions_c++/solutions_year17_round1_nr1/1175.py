#include <iostream>
#include <algorithm>
#include <string>
#include <queue>
#include <vector>

int T;
int R, C;
typedef unsigned long long int ullong;
char matrix[30][30];

int main(int argc, const char* argv[]) {

  std::cin >> T;
  for (int t = 1; t <= T; t++) {
     std::cin >> R >> C;
     int count = 0;
     int blank = 0;
     for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
           std::cin >> matrix[i][j];
           if (matrix[i][j] != '?')
              ++count;
        }
     }
     std::cout << "Case #" << t << ": " << std::endl;
     int beginR = 0;
     for (int i = 0; i < R; i++) {
        if (beginR >= R) 
           break;
        int filled = 0;
        std::vector<int> pos;
        for (int j = 0; j < C; j++)
           if (matrix[i][j] != '?') {
              ++filled;
              pos.push_back(j);
           }
        if (filled == 0)
           continue;
        count = count - filled;
        int endR, beginC, endC;
        if (count == 0)
           endR = R - 1;
        else 
           endR = i;
        for (int j = 0; j < pos.size(); j++) {
           if (j == 0) 
              beginC = 0;
           else
              beginC = pos[j];
           if (j == pos.size() - 1)
              endC = C - 1;
           else 
              endC = pos[j+1] - 1;
           char current = matrix[i][pos[j]];
           for (int r = beginR; r <= endR; r++)
              for (int c = beginC; c <= endC; c++)
                 matrix[r][c] = current;
        }
        beginR = endR + 1;
     }
     for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++)
           std::cout << matrix[i][j];
        std::cout << std::endl;
     }
  }
  return 0;
}

