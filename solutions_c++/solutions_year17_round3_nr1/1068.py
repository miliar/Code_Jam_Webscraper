#include <iostream>
#include <fstream>
#include <iomanip>

#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <xfunctional>

const double PI = 2 * acos(0.0);

int main() 
  {
  std::wstring test_name = L"1CA_First";

  std::istream& in = std::ifstream(test_name + L"_input.txt"); 
  std::ostream& out = std::ofstream(test_name + L"_output.txt");
  //std::istream& in = std::cin; 
  //std::ostream& out = std::cout;

  int tests_number;
  in >> tests_number;
  for (int test_i = 1; test_i <= tests_number; ++test_i)
    {
    // INPUT
    long n, k;
    in >> n >> k;
    std::vector<std::pair<double, long>> best(n);
    std::vector<std::pair<double, double>> cakes(n);
    double radius, height;
    for (long i = 0; i < n; ++i)
      {
      in >> radius >> height;
      cakes[i].first = radius;
      cakes[i].second = height;
      best[i] = std::pair<double, long>(2 * PI * radius * height, i);
      }

    double max_area = 0;
    // ALGO
    std::sort(best.begin(), best.end(), std::greater<std::pair<double, long>>());
    double max_rad = 0.0;
    for (long i = 0; i < k; ++i)
      {
      max_area += best[i].first;
      max_rad = std::max(max_rad, cakes[best[i].second].first);
      }

    double max_dif = 0.0;
    double area = max_rad * max_rad * PI;

    for (long i = k; i < n; ++i)
      {
      for (long j = 0; j < k; ++j)
        {
        double r1 = cakes[best[i].second].first;
        double r2 = cakes[best[j].second].first;
        double h1 = cakes[best[i].second].second;
        double h2 = cakes[best[j].second].second;
        double area1 = r1 * r1 * PI;
        double area2 = max_rad * max_rad * PI;
        double area_dif = area1 - area2;
        double height1 = 2 * PI * r1 * h1;
        double height2 = 2 * PI * r2 * h2;
        const double dif = area_dif + height1 - height2;
        if (max_dif <= dif)
          {
          area = area1 + height1 - height2;
          max_dif = dif;
          }
        }
      }

    max_area += area;

    // OUTPUT
    out << "Case #" << test_i << ": ";
    out << std::setprecision(40) << max_area;
    out << std::endl;
    }

  return 0;
  }