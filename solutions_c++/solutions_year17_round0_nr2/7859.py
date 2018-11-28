#include <iostream>
#include <string>
#include <sstream>
#include <cstdint>

using namespace std;

string to_str(const int64_t x)
{
  std::stringstream ss;
  ss << x;
  return ss.str();
}

bool is_tidy(const int64_t x)
{
  string str = to_str(x);
  int len = (int)str.size();

  for (int i = 0; i < len - 1; i++)
    if (str[i] > str[i + 1])
      return false;

  return true;
}

void solve(int idx)
{
  std::string row;
  int64_t res;
  cin >> res;

  for (int n_digits = 1; !is_tidy(res); n_digits++) {
    string res_str = to_str(res);

    if (n_digits >= res_str.size()) {
      throw std::runtime_error("fail");
    }

    for (int i = 0; i < n_digits; i++)
      res_str[res_str.size() - 1 - i] = '0';

    stringstream ss(res_str);
    ss >> res;
    res--;
  }

  cout << "Case #" << idx << ": ";
  cout << res;
  cout << endl;
}

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
      solve(i + 1);

    return 0;
}
