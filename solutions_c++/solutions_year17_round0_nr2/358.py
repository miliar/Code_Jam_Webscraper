#include <iostream>
#include <vector>
#include <string>

using std::vector;
using std::string;
using std::cout;
using std::cin;
using std::endl;

int main ()
{
  int T;
  std::cin >> T;
  string buf;

  for (int t=1; t<=T; t++)
  {
    std::cin >> buf;
    std::vector<int> digits;
    for (char c : buf) {
      digits.push_back(int(c-'0'));
    }
    int min = digits.back();
    int last = digits.size();

    for (unsigned i = digits.size(); i-- > 0; ) {
      int next = digits[i];
      if (next > min) {
        last = i;
        min = next-1;
      } else {
        min = next;
      }
    }

    std::cout << "Case #" << t << ": ";
    std::cout << buf.substr(0,last);
    if (last < digits.size() && digits[last] > 1)
      std::cout << digits[last] - 1;
    // std::cout << "|";
    if (last+1 < digits.size()) {
      std::cout << string(digits.size()-last-1, '9');
    }
    std::cout << endl;
  }
  return 0;
}
