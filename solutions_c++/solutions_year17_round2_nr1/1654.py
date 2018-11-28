#include "ba.h"



void BA() {
  int tests;
  std::cin >> tests;
  for (int i = 1; i <= tests; i++) {
    long long destination, horses;
    std::cin >> destination >> horses;
    double slowest = -1.0;
    for (int horse = 0; horse < horses; horse++) {
      long long start, speed;
      std::cin >> start >> speed;
      double time = double(destination - start) / speed;
      if (slowest == -1.0 || time > slowest) slowest = time;
    }
    std::cout.precision(20);
    std::cout << "Case #" << i << ": ";
    std::cout << (destination / slowest) << std::endl;
  }
}
