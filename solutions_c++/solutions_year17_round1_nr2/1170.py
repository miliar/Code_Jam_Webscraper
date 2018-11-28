#include <iostream>
#include <algorithm>
#include <string>
#include <queue>
#include <vector>

int T;
typedef unsigned long long int ullong;

int matrix[100][100]; // N x P
int gram[100];
int N, P;
int swap[100];
int orginal[100];
int max = -1;

bool filled[100];
bool check(int a, int b);
int compute();
void process(int pos);

int main(int argc, const char* argv[]) {

  std::cin >> T;
  for (int c = 1; c <= T; c++) {
     std::cin >> N >> P;
     max = -1;
     for (int j = 0; j < N; j++)
        std::cin >> gram[j];
     for (int i = 0; i < N; i++) {
        for (int j = 0; j < P; j++)
           std::cin >> matrix[i][j];
     }
     for (int i = 0; i < P; i++) {
        filled[i] = false;
        orginal[i] = matrix[N - 1][i];
     }
     if (N == 1) {
        max = compute();
     }
     else {
        process(0);
     }
     
     std::cout << "Case #" << c << ": " << max << std::endl;
  }
  return 0;
}

bool check(int a, int b) {
   if ((90 * a <= 100 * b) && ( b * 100 <= 110 * a))
      return true;
   return false;
}

int compute() {
   int result = 0;
   for (int i = 0; i < P; i++) {
      // matrix[0..N-1][i]
      // gram[0..N-1]
      int num = matrix[0][i] / gram[0];
      int min_kit = 100 * matrix[0][i] / (110 * gram[0]);
      int max_kit = 100 * matrix[0][i] / (90 * gram[0]) + 1;
      for (int num_kits = min_kit; num_kits <= max_kit; num_kits++) {
         if (!check(gram[0] * num_kits, matrix[0][i]))
            continue;
         bool yes = true;
         for (int j  = 1; j < N; j++)
            if (!check(gram[j] * num_kits, matrix[j][i])) {
               yes = false;
               break;
            }
         if (yes) {
            ++result;
            break;
         }
      }
   }
   return result;
}

void process(int pos) {
   if (pos == P) {
      for (int i = 0; i <  P; i++) {
         matrix[N-1][i] = swap[i];
      }
      int result = compute();
      if (max < result) 
         max = result;
      return;
   }
   for (int i = 0; i < P; i++)
      if (!filled[i]) {
         swap[pos] = orginal[i];
         filled[i] = true;
         process(pos + 1);
         filled[i] = false;
      }
}



      



