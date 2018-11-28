#include <iostream>
#include <string>
#include <vector>

// true: sunny side, false: blank
std::vector<bool> pancake_positions;

unsigned check_pancake(unsigned start_idx, const std::vector<bool>& pancake_positions)
{
  while(start_idx < pancake_positions.size())
  {
    if (!pancake_positions[start_idx])
      break;
    ++start_idx;
  }
  return start_idx;
}

void flip_pancakes(std::vector<bool>& pancake_positions, unsigned start_idx, unsigned count)
{
  for(unsigned idx = 0; idx < count; ++idx)
  {
    pancake_positions[start_idx + idx] = !pancake_positions[start_idx + idx];
  }
}

unsigned find_flipper_usage(std::vector<bool>& pancake_positions, 
          unsigned flipper_size, unsigned &usage_count)
{
  unsigned check_idx = 0;
  for(usage_count = 0; usage_count <= pancake_positions.size() - flipper_size; ++usage_count)
  {
    check_idx = check_pancake(check_idx, pancake_positions);
    if (check_idx >= pancake_positions.size())
    {
      return true;
    }
    else if (check_idx > (pancake_positions.size() - flipper_size))
    {
      return false;
    }
    // flip from check_idx to check_idx + flipper_size
    flip_pancakes(pancake_positions, check_idx, flipper_size);
  }
  if (check_pancake(0, pancake_positions) >= pancake_positions.size())
  {
    return true;
  }

  return false;
}

int main()
{
  unsigned int num_tests = 0;
  std::cin >> num_tests;
  for(unsigned idx = 1; idx <= num_tests; ++idx)
  {
    std::string pancake_positions_str;
    unsigned flipper_size = 1;

    std::cin >> pancake_positions_str >> flipper_size;

    pancake_positions.resize(pancake_positions_str.size(), false);
    for(unsigned int idx = 0; idx < pancake_positions_str.size() ; ++idx)
      pancake_positions[idx] = (pancake_positions_str[idx] == '+');

    unsigned usage_count = 0;

    std::cout << "Case #" << idx << ": ";

    if (find_flipper_usage(pancake_positions, flipper_size, usage_count))
    {
      std::cout << usage_count;
    }
    else
    {
      std::cout << "IMPOSSIBLE";
    }
    std::cout << std::endl;
  }
}
