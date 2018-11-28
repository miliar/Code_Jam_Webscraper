#include <iostream>
#include <fstream>

#include <algorithm>
#include <vector>
#include <queue>
#include <string>

void find_stalls(long long& left, long long& right, long long stalls, long long users) 
  {
  std::vector<bool> free_stall(stalls + 2, true);
  free_stall[0] = false;
  free_stall[stalls + 1] = false;
  for (long long i = 1; i <= users; ++i)
    {
    long long best_stall = -1, min_l = -1, min_r = -1;
    for (long long j = 1; j <= stalls; ++j)
      if (free_stall[j])
        {
        long long cur_l = 0, cur_r = 0;
        while (free_stall[j - cur_l - 1])
          ++cur_l;
        while (free_stall[j + cur_r + 1])
          ++cur_r;
        long long cur_min = std::min(cur_l, cur_r);
        long long cur_max = std::max(cur_l, cur_r);
        long long min_min = std::min(min_l, min_r);
        long long min_max = std::max(min_l, min_r);
        if (cur_min > min_min
            || (cur_min == min_min && cur_max > min_max)
            || (cur_min == min_min && cur_max == min_max && cur_l < min_l))
          {
          min_l = cur_l;
          min_r = cur_r;
          best_stall = j;
          }
        }
    free_stall[best_stall] = false;
    if (i == users)
      {
      left = min_l;
      right = min_r;
      }
    }
  }

void find_stalls_fast(long long& left, long long& right, long long stalls, long long users)
  {
  long long factor = 1, all_users = 0, remain = 0;
  while (users > 0)
    {
    if (stalls % 2 == 0)
      remain += factor;
    if (stalls == 0)
      remain = 0;
    stalls = (stalls - 1) / 2;
    left = stalls + long long(remain - factor >= users);
    right = stalls + long long(remain >= users);
    users -= factor;
    factor *= 2;
    }
  }

int main() 
  {
  std::wstring test_name = L"0C_BathroomStalls";

  std::istream& in = std::ifstream(test_name + L"_input.txt"); 
  std::ostream& out = std::ofstream(test_name + L"_output.txt");
  //std::istream& in = std::cin; 
  //std::ostream& out = std::cout;

  int tests_number;
  in >> tests_number;
  for (int test_i = 1; test_i <= tests_number; ++test_i)
    {
    long long stalls, users;
    in >> stalls >> users;

    long long left, right;
    find_stalls_fast(left, right, stalls, users);

    out << "Case #" << test_i << ": ";
    out << right << " " << left;
    out << std::endl;
    }

  return 0;
  }