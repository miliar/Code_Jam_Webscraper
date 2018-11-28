#include <iostream>
#include <algorithm>
#include <string>
#include <queue>
#include <vector>
#include <iomanip>

int T;
typedef unsigned long long int ullong;

ullong D, N;
ullong S[1003], K[1003];

int main(int argc, const char* argv[]) {

  std::cin >> T;
  for (int i = 1; i <= T; i++) {
     std::cin >> D >> N;
     for (int j = 0; j < N; j++)
        std::cin >> K[j] >> S[j];
     double max = -1;
     for (int j = 0; j < N; j++) {
        double tmp = ((double) (D - K[j])) / ((double) S[j]);
        if (max < tmp)
           max = tmp;
     }
     std::cout << "Case #" << i << ": " ;
     std::cout << std::setprecision(10) << ((double) D)/max << std::endl;
  }
  return 0;
}

