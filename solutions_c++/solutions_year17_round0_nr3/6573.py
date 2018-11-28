#include <iostream>
#include <utility>
#include <vector>
#include <cstring>
#include <map>

using namespace std;

int get_max(int a, int b) {
  return a >= b ? a : b;
}

int get_min(int a, int b) {
  return a <= b ? a : b;
}

std::pair<int, int> get_ls_rs(std::string str, int index) {
  int ls = 0, rs = 0;
  while (str[index - ls] != '0' || str[index + rs] != '0') {
    if (str[index - ls] != '0') ls++;
    if (str[index + rs] != '0') rs++;
  }
  return std::make_pair(ls - 1, rs - 1);
}

std::pair<int, int> get_pair(std::string str,int last_number) {
  std::pair<int, int> ret;
  for (int i = 0; i < last_number; i++) {
    std::vector<std::pair<int, std::pair<int, int> > > pairs;
    for (int j = 1; j < str.size() - 1; j++) {
      int start = j, end;
      if (str[j] == '0') continue;
      while(str[j] != '0') j++;
      end = j - 1;
      pairs.push_back(std::make_pair(j - start, std::make_pair(start, end)));
    }
    int max_index = 0;
    for (int j = 1; j < pairs.size(); j++) {
      if (pairs[j].first > pairs[max_index].first)
        max_index = j;
    }
    int index_fill = (pairs[max_index].second.first + pairs[max_index].second.second) / 2;
    ret = get_ls_rs(str, index_fill);
    str[index_fill] = '0';
  }
  return ret;
}

int main(int argc, char **args) {
  int test_cases = 0;
  cin >> test_cases;
  for (int i = 1; i <= test_cases; i++) {
    int length, last_number;
    cin >> length;
    cin >> last_number;
    std::string str = "0";
    for (int i = 0; i < length; i++) str += '.';
    str += '0';
    std::pair<int, int> pai = get_pair(str, last_number);
    cout << "Case #" << i << ": " << max(pai.first, pai.second) << " " << min(pai.second, pai.first) << endl;
  }
  return 0;
}
