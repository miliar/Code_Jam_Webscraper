#include <iostream>
#include <sstream>

using namespace std;

void tidy(int &res) 
{
  int target;
  cin >> target;

  int last_tidy = 0;
  for (int i = 0; i <= target; i++) {
    ostringstream os;
    os << i;
    string digits = os.str();
    char biggest = digits[0];
    bool accept = true;
    for (char c : digits) {
      if (c < biggest) {
        accept = false;
        break;
      } else if (c > biggest) {
        biggest = c;
      }
    }

    if (accept) {
      last_tidy = i;
    }
  }

  res = last_tidy;

}

int main()
{
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    int res;
    tidy(res);
    cout << "Case #" << i << ": " << res << endl;
  }

  return 0;
}
