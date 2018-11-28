#include <algorithm>
#include <cassert>
#include <cmath>
#include <deque>
#include <iostream>
#include <iterator>
#include <limits>
#include <map>
#include <numeric>
#include <queue>
#include <vector>

enum Colors { R, O, Y, G, B, V };

std::vector<char> COLORS = {'R', 'O', 'Y', 'G', 'B', 'V'};

constexpr size_t NC = 6;

int maxColorIndx(size_t* color, size_t notColor) {
  size_t max = 0;
  size_t maxIdx = 0;
  for (size_t i = 0; i < NC; ++i) {
    if (i == notColor) continue;

    if (color[i] > max) {
      max = color[i];
      maxIdx = i;
    }
  }
  return maxIdx;
}

bool solve(int testcase, size_t* colors, std::vector<int>& order) {
  // distance(colors, std::max_element(colors, colors + NC));

  /*std::cerr << "Enter solve";
  for (size_t i = 0; i < NC; ++i) {
    std::cerr << colors[i] << " ";
  }
  std::cerr << "\n";*/

  int prevColor = NC;
  if (order.size() > 0) prevColor = order.back();

  size_t numRemainingColors = std::accumulate(colors, colors + NC, 0);

  if (numRemainingColors == 0) {
    if (prevColor == order[0]) {
      // std::cerr << "Col with end\n";
      return false;
    } else {
      return true;
    }
  }

  std::array<int, NC> colorsSorted = {{R, O, Y, G, B, V}};
  std::sort(colorsSorted.begin(), colorsSorted.end(),
            [colors](int l, int r) { return colors[l] > colors[r]; });

  {
    auto maxColor = colors[colorsSorted[0]];
    if (order.size() > 0 && order.front() == colorsSorted[0]) {
      if (colors[colorsSorted[0]] > (numRemainingColors - 1) / 2) {
        /*std::cerr << " " << colorsSorted[0] << " rem: " << numRemainingColors
                  << "\n";*/
        return false;
      }
    } else {
      if (colors[colorsSorted[0]] > (numRemainingColors + 1) / 2) {
        /*std::cerr << " " << colorsSorted[0] << " rem: " << numRemainingColors
                  << "\n";*/
        return false;
      }
    }
  }

  for (auto maxElemIdx : colorsSorted) {
    if (maxElemIdx == prevColor) continue;
    // auto maxElemIdx = maxColorIndx(colors, prevColor);

    // std::cerr << "Max colors in " << maxElemIdx << ": " << colors[maxElemIdx]
    //<< "\n";

    if (colors[maxElemIdx] == 0) {
      /* std::cout << "Case #" << testcase << ": "
                << "IMPOSSIBLE"
                << "\n";*/
      // std::cerr << "No color left\n";
      break;
    }

    // prevColor = maxElemIdx;
    order.push_back(maxElemIdx);
    colors[maxElemIdx]--;
    if (solve(testcase, colors, order)) return true;
    // std::cerr << "Exit solve\n";
    order.pop_back();
    colors[maxElemIdx]++;
  }

  return false;
}

int main() {
  std::cout.setf(std::ios::unitbuf);  // unbuffered output

  uint64_t numberOfTestcases;
  std::cin >> numberOfTestcases;
  for (size_t i = 1; i <= numberOfTestcases; ++i) {
    size_t colors[NC];
    size_t N;
    std::cin >> N;
    for (size_t i = 0; i < NC; ++i) {
      std::cin >> colors[i];
    }
    std::vector<int> order;
    order.reserve(N);
    if (solve(i, colors, order)) {
      std::cout << "Case #" << i << ": ";
      for (auto c : order) {
        std::cout << COLORS[c];
      }
      std::cout << "\n";
    } else {
      std::cout << "Case #" << i << ": "
                << "IMPOSSIBLE"
                << "\n";
    }
  }
  return 0;
}
