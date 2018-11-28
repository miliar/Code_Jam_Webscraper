#include <iostream>
#include <string>
#include <set>

using namespace std;

int find_first(string &s) {
  for (int i = 0; i < s.length(); i++) {
    if (s[i] == '-')
      return i;
  }

  return -1;
}

char flip_char(char c) {
  if (c == '-')
    return '+';

  return '-';
}


int main() {
  int t;
  cin >> t;

  for (int i = 0; i < t; i++) {
    string s;
    int k;
    cin >> s >> k;

    int first;
    int count = 0;
    set<string> previous_steps;
    while ((first = find_first(s)) != -1) {
      int pos = first;
      if (first > s.length() - k) {
        pos = s.length() - k;
      }
      //cout << first << " " << pos << endl;

      for (int j = 0; j < k; j++) {
        s[pos + j] = flip_char(s[pos + j]);
      }

      ////cout << s << endl;
      if (previous_steps.find(s) != previous_steps.end()) {
        break;
      }

      previous_steps.insert(s);

      count++;
    }

    cout << "Case #" << i + 1 << ": ";
    if (find_first(s) == -1)
      cout << count << endl;
    else
      cout << "IMPOSSIBLE" << endl;

    // --++++
    //
    // ---+-++-
    // ++++-++-
    // +++++---
    // ++++++++
    //
    // -+-+-
    // +-++- -++-+ --+--
    // +---+ +---+ ++---
    // +++++
  }
}
