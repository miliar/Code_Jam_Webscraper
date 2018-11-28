#include <algorithm>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <tuple>
#include <vector>

struct Pancake {
  double radius;
  double height;
};

struct Problem {
  size_t orderSize;
  std::vector<Pancake> pancakes;
};

Problem ReadProblem(std::istream* istream) {
  size_t n;
  *istream >> n;
  Problem result;
  *istream >> result.orderSize;
  result.pancakes.resize(n);
  for (auto& pancake : result.pancakes) {
    *istream >> pancake.radius >> pancake.height;
  }
  return result;
}

double FindMaximalOrderArea(const Problem& problem) {
  const double kPi = 4.0 * std::atan(1.0);
  struct PancakeArea {
    double topArea;
    double sideArea;
  };
  std::vector<PancakeArea> pancakeAreas;
  for (const auto& pancake : problem.pancakes) {
    pancakeAreas.push_back({
        kPi * pancake.radius * pancake.radius,
        2.0 * kPi * pancake.radius * pancake.height,
    });
  }
  std::sort(pancakeAreas.begin(), pancakeAreas.end(),
            [](const auto& left, const auto& right) {
              return std::tie(left.sideArea, left.topArea) >
                     std::tie(right.sideArea, right.topArea);
            });
  double bestResult = 0.0;
  for (const auto& basePancake : pancakeAreas) {
    double result = basePancake.topArea + basePancake.sideArea;
    size_t counter = problem.orderSize - 1;
    for (const auto& pancake : pancakeAreas) {
      if (&pancake == &basePancake) {
        continue;
      }
      if (counter == 0) {
        break;
      }
      if (pancake.topArea <= basePancake.topArea) {
        result += pancake.sideArea;
        --counter;
      }
    }
    if (counter == 0) {
      bestResult = std::max(bestResult, result);
    }
  }
  return bestResult;
}

int main() {
  int numberOfCases;
  std::cin >> numberOfCases;
  for (int caseNo = 0; caseNo < numberOfCases; ++caseNo) {
    const auto problem = ReadProblem(&std::cin);
    const auto result = FindMaximalOrderArea(problem);
    std::cout << "Case #" << caseNo + 1 << ": " << std::fixed
              << std::setprecision(10) << result << '\n';
  }
  return 0;
}
