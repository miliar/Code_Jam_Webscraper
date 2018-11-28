#include <iostream>
#include <vector>
#include <string>
#include <cstdint>
#include <sstream>
using namespace std;

string processCase(string cap) {
  int n = cap.size();
  int lastIndex = 0;
  int i;
  for(i = 0; i < n; i++) {
    if (cap[lastIndex] < cap[i]) {
      lastIndex = i;
    } else if (cap[lastIndex] > cap[i]) {
      break;
    }
  }

  if (i == n) {
    return cap;
  }


  string s = cap.substr(0, lastIndex);
  s += cap[lastIndex] - 1;
  if (s == "0") {
    s = "";
  }
  for (i = lastIndex + 1; i < n; i++) {
    s += '9';
  }

  return s;
}

int main(int args, char* argv[]) {
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    string N;
    cin >> N;
    string result = processCase(N);
    cout << "Case #" << t << ": " << result << endl;
  }
  return 0;
}

