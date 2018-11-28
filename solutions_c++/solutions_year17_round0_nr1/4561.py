#include <iostream>
#include <vector>
#include <cassert>
#include <cstdio>
#include <limits>
#include <set>
#include <string>
#include <cstring>
#include <fstream>

using namespace std;

void invert(string& s, int from, int cnt){
  while (cnt) {
    if (s[from] == '-') {
      s[from] = '+';
    }
    else {
      s[from] = '-';
    }
    from++;
    --cnt;
  }
}

int solve(int k, string str) {
  int ans = 0;
  for (int i = 0; i <= str.length()-k; ++i) {
    if (str[i] == '+') {
      continue;
    } else {
      invert(str, i, k);
      ans++;
    }
  }
  for (int i = 0; i < k; ++i) {
    if (str[str.length() - k + i] == '-') ans = -1;
  }
  return ans;
}

int main() {
  ifstream in("input.txt");
  ofstream out("output.txt");
  int T;
  in >> T;
  for (int t_case = 1; t_case <= T; t_case++) {
    string str;
    int k;
    in >> str >> k;
    int ans = solve(k, str);
    out << "Case #" << t_case << ": " <<( (ans > -1) ? std::to_string(ans) : string("IMPOSSIBLE") ) << endl;
  }
  out.close();
  return 0;
}
