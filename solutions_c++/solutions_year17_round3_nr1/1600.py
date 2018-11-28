#include <algorithm>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <vector>

const double PI = acos(-1);

int main() {
  size_t T;
  std::cin >> T;
  for (size_t t = 1; t <= T; ++t) {
    size_t N, K;
    std::cin >> N >> K;

    std::vector<std::pair<double, double> > cakes;

    for (size_t i = 0; i < N; ++i) {
      std::pair<double, double> cake;
      std::cin >> cake.first >> cake.second;
      cakes.emplace_back(cake);
    }
    
    std::sort(cakes.begin(), cakes.end());

    double max_area = 0;

    for (size_t base = K - 1; base < N; ++base) {
      
      std::vector<double> areas;
      for (size_t i = 0; i < base; ++i) {
        areas.emplace_back(cakes[i].first * cakes[i].second);
      }
      std::sort(areas.begin(), areas.end());

      double area = cakes[base].first * cakes[base].second + 0.5 * cakes[base].first * cakes[base].first;

      for (size_t i = 1; i < K; ++i) {
        area += areas[areas.size() - i];
      }

      area = area * 2 * PI;

      max_area = std::max(max_area, area);
    }

    std::cout << "Case #" << t << ": " << std::fixed << std::setprecision(8) << max_area << "\n";

  }
  return 0;
}
