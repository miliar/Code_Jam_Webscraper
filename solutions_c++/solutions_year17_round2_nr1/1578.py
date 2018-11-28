#include <iostream>
#include <fstream>
#include <iomanip>

#include <algorithm>
#include <vector>
#include <queue>
#include <string>

int main() 
  {
  std::wstring test_name = L"1AA_First";

  std::istream& in = std::ifstream(test_name + L"_input.txt"); 
  std::ostream& out = std::ofstream(test_name + L"_output.txt");
  //std::istream& in = std::cin; 
  //std::ostream& out = std::cout;

  

  int tests_number;
  in >> tests_number;
  for (int test_i = 1; test_i <= tests_number; ++test_i)
    {
    // INPUT
    double dest;
    long long n;
    in >> dest >> n;
    std::vector<std::pair<double, double>> horses(n);
    for (long long i = 0; i < n; ++i)
      in >> horses[i].first >> horses[i].second;

    // ALGO
    std::sort(horses.begin(), horses.end());
    double best_speed = 0.0;
    double max_time = 0.0;
    for (long i = 0; i < n; ++i)
      {
      std::vector<std::pair<double, double>> intersections;
      intersections.push_back(horses[i]);
      intersections.push_back(std::pair<double, double>(dest, 0.0));
      for (long j = i + 1; j < n; ++j)
        {
        double intersection = dest + 1;
        if (horses[i].second > horses[j].second)
          {
          double time_before_intersection = (horses[j].first - horses[i].first) / (horses[i].second - horses[j].second);
          intersection = horses[i].first + horses[i].second * time_before_intersection;
          }
        if (intersection < dest)
          intersections.push_back(std::pair<double, double>(intersection, horses[j].second));
        }
      std::sort(intersections.begin(), intersections.end());

      double time = 0.0;
      for (int j = 0; j < intersections.size() - 1; ++j)
        time += (intersections[j + 1].first - intersections[j].first) / intersections[j].second;
      if (time > max_time)
        max_time = time;
      }
    best_speed = dest / max_time;

    // OUTPUT
    out << "Case #" << test_i << ": ";
    out << std::setprecision(20) << best_speed;
    out << std::endl;
    }

  return 0;
  }