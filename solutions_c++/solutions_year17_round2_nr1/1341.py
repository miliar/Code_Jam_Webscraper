#include <algorithm>
#include <iomanip>
#include <iostream>
#include <limits>
#include <vector>

struct Horse {
  long double position;
  long double speed;
};

using HorseSeq = std::vector<Horse>;

struct Problem {
  long double destination;
  HorseSeq horses;
};

Problem ReadProblem(std::istream* istream) {
  Problem result;
  *istream >> result.destination;
  size_t numberOfHorses;
  *istream >> numberOfHorses;
  result.horses.resize(numberOfHorses);
  for (auto& horse : result.horses) {
    *istream >> horse.position >> horse.speed;
  }
  return result;
}

long double FindAverageSpeed(const Problem& problem) {
  long double time = 0.0;
  for (const auto& horse : problem.horses) {
    if (horse.position < problem.destination) {
      time =
          std::max(time, (problem.destination - horse.position) / horse.speed);
    }
  }
  return problem.destination / time;
}

int main() {
  int numberOfCases;
  std::cin >> numberOfCases;
  for (int caseNo = 0; caseNo < numberOfCases; ++caseNo) {
    const auto problem = ReadProblem(&std::cin);
    const auto result = FindAverageSpeed(problem);
    std::cout << "Case #" << caseNo + 1 << ": " << std::fixed
              << std::setprecision(10) << result << '\n';
  }
  return 0;
}
