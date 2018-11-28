#include <iostream>
#include <vector>
#include <string>
#include <list>

using namespace std;
std::string tidy(std::string n);

int main() {
  int t;
  string n;

  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cin >> n;
    string result = tidy(n);
    cout << "Case #" << i << ": " << result << endl;
  }

  return 0;
}


std::string tidy(std::string n) {
  if (n.length() == 1)
    return n;

  list<char> tidyList;
  for (int i = n.length()-1; i >= 0 ; i--) {
    char curr = n[i];

    if (tidyList.empty())
      tidyList.push_front(curr);
    else if (tidyList.front() < curr) {
      for (auto iter = tidyList.begin(); iter != tidyList.end(); iter++)
        (*iter) = '9';
      tidyList.push_front(curr-1);
    } else {
      tidyList.push_front(curr);
    }
  }

  if (tidyList.front() == '0')
    tidyList.pop_front();

  string result;
  for (auto iter = tidyList.begin(); iter != tidyList.end(); iter++) {
    result += (*iter);
  }
  return result;

}
