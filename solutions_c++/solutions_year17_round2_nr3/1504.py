#include <iostream>
#include <fstream>
#include <iomanip>

#include <algorithm>
#include <vector>
#include <queue>
#include <string>

int main() 
  {
  std::wstring test_name = L"1AC_Third";

  std::istream& in = std::ifstream(test_name + L"_input.txt"); 
  std::ostream& out = std::ofstream(test_name + L"_output.txt");
  //std::istream& in = std::cin; 
  //std::ostream& out = std::cout;

  int tests_number;
  in >> tests_number;
  for (int test_i = 1; test_i <= tests_number; ++test_i)
    {
    // INPUT
    long n, posts;
    in >> n >> posts;
    std::vector<std::pair<double, double>> horses(n);
    for (long i = 0; i < n; ++i)
      in >> horses[i].first >> horses[i].second;
    std::vector<double> distances(n, 0);
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < n; ++j)
        {
        long cur_dist;
        in >> cur_dist;
        if (i + 1 == j)
          distances[i] = cur_dist;
        }

    long start, end;
    in >> start >> end;

    // ALGO
    std::vector<double> times(n, std::numeric_limits<double>::max());
    times[0] = 0.0;
    for (int i = 1; i < n; ++i)
      {
      for (int j = 0; j < i; ++j)
        {
        double distance_from_j_to_i = 0;
        for (int k = j; k < i; ++k) 
          distance_from_j_to_i += distances[k];
        if (distance_from_j_to_i > horses[j].first)
          continue;
        const double possible_time = distance_from_j_to_i / horses[j].second + times[j];
        if (possible_time < times[i])
          times[i] = possible_time;
        }
      }

    // OUTPUT
    out << "Case #" << test_i << ": ";
    out << std::setprecision(20) << times[n - 1];
    out << std::endl;
    }

  return 0;
  }