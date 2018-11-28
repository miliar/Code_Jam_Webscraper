#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <vector>
using namespace std;  // since cin and cout are both in namespace std, this saves some text


string flip(string s, int k, int i)
{
  if (k + i > s.size()) return "";
  for (int j = i; j < i + k; j++)
  {
    if (s[j] == '-') 
    {
      s[j] = '+';
    } else {
      s[j] = '-';
    }
  }
  return s;
}

int processFlip(string s, int k)
{
  int result = 0;
  for (int i = 0; i < s.size(); i++)
  {
    if (s[i] == '-') {
      result++;
      s = flip(s, k, i);
      if (s == "") return -1;
    }
  }
  return result;
}

int main() {
  int t, n;
  string s;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; i++) {
    cin >> s;
    cin >> n;  // read n and then m.
    int result = processFlip(s, n);
    string answer;
    if (result == -1)
    {
      answer = "IMPOSSIBLE";
    } else {
      answer = to_string(result);
    }
    cout << "Case #" << i << ": " << answer << endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
}