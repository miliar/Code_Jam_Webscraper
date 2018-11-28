#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

vector<int> split_number(long long num)
{
  vector<int> rnum_vec;

  while (num > 0) {
    rnum_vec.push_back(num % 10);
    num /= 10;
  }

  return vector<int>(rnum_vec.rbegin(), rnum_vec.rend());
}

long long join_number(vector<int> &num_vec)
{
  long long order = pow(10, num_vec.size() - 1);
  long long num = 0;

  for (auto &v: num_vec) {
    num += (long long)v * order;
    order /= 10LL;
  }
  return num;
}

void reset(vector<int> &digits, int i)
{
  for (; i < digits.size(); ++i) {
    digits[i] = 9;
  }
}

void largest_tidy(vector<int> &digits, int i)
{
    if (i >= digits.size() - 1) {
      return; // base case. Always tidy
    }

    largest_tidy(digits, i + 1);
    if (digits[i] <= digits[i + 1]) {
      return; // this suffix is tidy
    } else {
      --digits[i]; // we will never do this for 0
      reset(digits, i + 1);
    }
}

long long solve_test(long long num)
{
  if (num == 0) {
    return 0;
  }
  
  auto num_vec = split_number(num);
  largest_tidy(num_vec, 0);
  return join_number(num_vec);
}

int main(int argc, char **argv)
{
  string line;
  ifstream in_file(argv[1]);

  getline(in_file, line);
  int test_num = stoi(line);

  for (int i = 0; i < test_num; ++i) {
    getline(in_file, line);
    cout << "Case #" << i + 1 << ": " << solve_test(stol(line)) << endl;
  }
}
