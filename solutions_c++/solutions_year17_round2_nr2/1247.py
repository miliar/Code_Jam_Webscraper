#include <algorithm>
#include <array>
#include <boost/range/iterator_range.hpp>
#include <iostream>
#include <vector>
#include <numeric>
#include <set>

constexpr std::array<char, 3> kColorNames = {
    {'R', 'Y', 'B'}
};


struct Problem {
  size_t numberOfRedUnicorns;
  size_t numberOfYellowUnicorns;
  size_t numberOfBlueUnicorns;
};

Problem ReadProblem(std::istream* istream) {
  Problem result;
  size_t tmp;
  *istream >> tmp
           >> result.numberOfRedUnicorns >> tmp
           >> result.numberOfYellowUnicorns >> tmp
           >> result.numberOfBlueUnicorns >> tmp;
  return result;
}

std::string FindUnicornArrangement(const Problem& problem) {
  std::array<size_t, 3> colorCounters = {{ problem.numberOfRedUnicorns, problem.numberOfYellowUnicorns, problem.numberOfBlueUnicorns }};

  auto selectFirstColor = [&] {
      size_t bestCounter = 0;
      size_t bestColor = 0;
      for (size_t i = 0; i < colorCounters.size(); ++i) {
          if (bestCounter < colorCounters[i]) {
              bestCounter = colorCounters[i];
              bestColor = i;
          }
      }
      return bestColor;
  };

  auto selectSecondColor = [&](size_t firstColour) {
      size_t bestCounter = 0;
      size_t bestColor = (firstColour + 1) % 3;
      for (size_t i = 0; i < colorCounters.size(); ++i) {
          if (i != firstColour && bestCounter < colorCounters[i]) {
              bestCounter = colorCounters[i];
              bestColor = i;
          }
      }
      return bestColor;
  };
  
  size_t n = problem.numberOfRedUnicorns + problem.numberOfYellowUnicorns + problem.numberOfBlueUnicorns;
  std::string result;
  for (size_t i = 0; i < n; ) {
      size_t firstColor = selectFirstColor();
      if (colorCounters[firstColor] == 0) {
          std::cerr << result << '\n';
          throw std::logic_error("Unexpected situation.");
      }
      result += kColorNames[firstColor];
      --colorCounters[firstColor];
      --n;
      while (colorCounters[firstColor] > 0) {
          size_t secondColor = selectSecondColor(firstColor);
          if (colorCounters[secondColor] == 0) {
              return "";
          }
          result += kColorNames[secondColor];
          result += kColorNames[firstColor];
          --colorCounters[secondColor];      
          --colorCounters[firstColor];
          n -= 2;
      }
  }
  if (!result.empty() && *result.begin() == *result.rbegin()) {
      return "";
  }
  return result;
}

int main() {
  int numberOfCases;
  std::cin >> numberOfCases;
  for (int caseNo = 0; caseNo < numberOfCases; ++caseNo) {
    const auto problem = ReadProblem(&std::cin);
    const auto result = FindUnicornArrangement(problem);
    std::cout << "Case #" << caseNo + 1 << ": ";
    if (result.empty()) {
      std::cout << "IMPOSSIBLE\n";
    } else {
      std::cout << result << '\n';
    }
  }
  return 0;
}
