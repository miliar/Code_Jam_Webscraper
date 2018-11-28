#include <algorithm>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <stdio.h>
#include <string.h>
#include <vector>

int main(int argc, char** argv) {
  if (argc <= 2) return -1;

  std::ifstream ifs(argv[1]);
  std::ofstream ofs(argv[2]);
  int nCase = 0;
  ifs >> nCase;
  std::cout << "#Cases: " << nCase << std::endl;
  char cakes[1000];
  for (size_t i = 0; i < nCase; ++i) {
    int D, N;
    ifs >> D >> N;

    double time = 0;
    for (int j = 0; j < N; ++j) {
      double position, speed;
      ifs >> position >> speed;

      // calculate the arriving time
      time = std::max(time, ((double) D - position) / speed);
    }
    std::cout << "Case #" << i + 1 << ": ";
    ofs << "Case #" << i + 1 << ": ";
    std::cout << std::setprecision(std::numeric_limits<double>::digits10) << (double) D / time
              << std::endl;
    ofs << std::setprecision(std::numeric_limits<double>::digits10) << (double) D / time
        << std::endl;
  }
}
