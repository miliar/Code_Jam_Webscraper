#include <iostream>
#include <fstream>
#include <iomanip>

#include <algorithm>
#include <vector>
#include <queue>
#include <string>

int main() 
  {
  std::wstring test_name = L"1CC_Third";

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
    double x;
    in >> n >> k >> x;
    std::vector<double> prob(n);
    for (long i = 0; i < n; ++i)
      in >> prob[i];
    
    // ALGO
    sort(prob.begin(), prob.end());

    for (long i = 0; i < n; ++i)
      {
      if (x <= 0)
        break;
      double next_prob = 1.0;
      long cores = 1;
      for (; cores < n; ++cores)
        if (prob[cores] > prob[0])
          {
          next_prob = prob[cores];
          break;
          }
      double core_dif = next_prob - prob[0];
      double need_train = core_dif * cores;
      if (need_train > x)
        core_dif = x / cores;
      for (long jj = 0; jj < cores; ++jj)
        prob[jj] += core_dif;
      x -= core_dif * cores;
      }

    double res = 1.0;
    for (long i = 0; i < n; ++i)
      res *= prob[i];

    // OUTPUT
    out << "Case #" << test_i << ": ";
    out << std::setprecision(20) << res;
    out << std::endl;
    }

  return 0;
  }