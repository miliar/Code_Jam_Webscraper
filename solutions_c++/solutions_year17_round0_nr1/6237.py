#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <unordered_map>
#include <numeric>
#include <deque>


template<typename T>
std::vector<T> space_split_string(std::string& input)
{
  std::stringstream ss(input);
  std::vector<T> return_value;
  T value;
  while (ss >> value)
  {
    return_value.push_back(value);
  }
  return return_value;
}

template<typename T>
std::string print_results(const std::vector<T>& results)
{
  std::stringstream output;
  int case_number = 1;
  for (auto result : results) {
    output << "Case #" << case_number << ": " << result << std::endl;
    case_number++;
  }
  return output.str();
}

std::vector<int> feasibility(const std::vector<int>& pancakes, int level = 1)
{
  std::vector<int> return_value;
  if (pancakes.size() < level) 
    return return_value;
  if ((pancakes[0] - pancakes[level])/2 >= level) {
    // Perform split
    printf("Split!\n");
    return_value.push_back(pancakes[level - 1]);
    return return_value;
  } else {
    return_value = feasibility(pancakes, level + 1);
    if (return_value.size() > 0)
      return_value.push_back(pancakes[level - 1]);
    return return_value;
  }
}

bool find_minimal_time(std::deque<int>& pancakes, int& time_spent)
{
  std::vector<int> durations;
  int half_max = int(std::ceil(double(pancakes[0]) * 0.5));
  for (size_t i = 1; i < pancakes.size(); i++) {
    durations.push_back(std::max(pancakes[i], half_max) + i);
  }
  auto it = std::min_element(durations.begin(), durations.end());
  if (*it >= pancakes[0]) {
    return false;
  } else {
    for (int i = 0; i < it - durations.begin() + 1; i++) {
      int num_pancakes = pancakes[i];
      pancakes[i] = (num_pancakes/2);
      pancakes.push_back(num_pancakes - num_pancakes/2);
    }
    time_spent = it - durations.begin() + 1;
    return true;
  }
}


int flip_pancakes(std::string& pancake_row, int K)
{
  int num_flips = 0;
  for (int i = 0; i < pancake_row.size() - K + 1; i++)
  {
    if (pancake_row[i] == '+')
    {
      continue;
    }
    else
    {
      for (int k = i; k < i + K; k++)
      {
        if (pancake_row[k] == '+') pancake_row[k] = '-';
        else pancake_row[k] = '+';
      }
      num_flips++;
    }
    printf("%s\n", pancake_row.c_str());
  }
  return num_flips;
}

int main(int argc, char** argv)
{
  if (argc < 2) {
    return -1;
  }
  std::ifstream input_file(argv[1]);
  if (!input_file.is_open()) {
    return -1;
  }
  std::string num_cases_str;
  std::getline(input_file, num_cases_str);
  int num_cases = std::stoi(num_cases_str);

  std::vector<std::string> result;
  for (int i = 0; i < num_cases; i++) {
    std::string pancake_row;
    std::getline(input_file, pancake_row);
    auto pancake_vec = space_split_string<std::string>(pancake_row);
    pancake_row = pancake_vec[0];
    int K = std::stoi(pancake_vec[1]);

    auto orig_pancake_row = pancake_row;
    int num_flips = flip_pancakes(pancake_row, K);
    bool all_correct = 
      std::all_of(pancake_row.begin(), pancake_row.end(), [](char p)
          {
            return p == '+';
          });
    if (!all_correct)
    {
      std::reverse(orig_pancake_row.begin(), orig_pancake_row.end());
      num_flips = flip_pancakes(orig_pancake_row, K);
      all_correct = 
        std::all_of(orig_pancake_row.begin(), orig_pancake_row.end(), [](char p)
            {
              return p == '+';
            });
    }


    printf("Test %d, flips %d, all correct %d\n", i, num_flips, all_correct);

    if (all_correct)
    {
      result.push_back(std::to_string(num_flips));
    }
    else
    {
      result.push_back("IMPOSSIBLE");
    }

  }

  std::string result_str = print_results(result);

  std::ofstream output_file(argv[2]);
  if (output_file.is_open())
  {
    output_file << result_str;
    output_file.close();
  }

  return 0;
}
