#include <algorithm>
#include <iomanip>
#include <ios>
#include <iostream>

int main() {

  int t, totalCases;
  std::cin >> t;

  totalCases = t;
  while (t--) {
    double d, n, ki, si;
    std::cin >> d >> n;

    double maxSpeed = 0;
    for (auto i = 1; i <= n; i++) {
      std::cin >> ki >> si;
      auto otherHorseTime = (d - ki) / si;

      //   maxSpeed = std::min(d / otherHorseTime, maxSpeed);
      if (maxSpeed == 0)
        maxSpeed = d / otherHorseTime;
      else
        maxSpeed = std::min(d / otherHorseTime, maxSpeed);
    }

    std::cout << "Case #" << totalCases - t << ": " << std::fixed
              << std::setprecision(6) << maxSpeed << '\n';
  }

  return 0;
}