#include <iostream>
#include <iomanip>

using namespace std;

using bigint = unsigned long long;

int main() {
  unsigned int numCases;
  std::cin >> numCases;
  for (unsigned int i = 0; i < numCases; ++i) {
    double finishPos;
    std::cin >> finishPos;
    unsigned numHorses;
    std::cin >> numHorses;

    double currentLongestTime = 0;
    for (unsigned int j = 0; j < numHorses; ++j) {
      double horseStartPos;
      std::cin >> horseStartPos;
      double horseSpeed;
      std::cin >> horseSpeed;

      double timeHours = (finishPos - horseStartPos) / horseSpeed;
      if (timeHours > currentLongestTime) {
        currentLongestTime = timeHours;
      }
    }

    double speed = finishPos / currentLongestTime;

    std::cout << std::setprecision(10);
    cout << "Case #" << i + 1 << ": " << speed;
    cout << endl;
  }
  return 0;
}
