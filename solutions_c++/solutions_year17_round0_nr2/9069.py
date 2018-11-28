#include <iostream>
#include <sstream>
using namespace std;

string last_tidy_number(string N) {
  int breakpoint = -1;
  for (int i = 1; i < N.size(); i++) {
    if (N[i - 1] > N[i]) {
      breakpoint = i;
      break;
    }
  }

  if (breakpoint > 0) {
    while (N[breakpoint - 1] == '0') {
      breakpoint -= 1;
    }

    N[breakpoint - 1] = N[breakpoint - 1] - 1;

    stringstream ss;

    if (breakpoint != 1 || N[breakpoint - 1] != '0') {
      ss << N.substr(0, breakpoint);
    }

    for (int i = breakpoint; i < N.size(); i++) {
      ss << '9';
    }

    return last_tidy_number(ss.str());
  } else {
    return N;
  }
}

int main(int argc, char** argv) {
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    string N;
    cin >> N;

    cout << "Case #" << i << ": " << last_tidy_number(N) << endl;
  }
  return 0;
}
