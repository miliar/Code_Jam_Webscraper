#include <cassert>
#include <iostream>

using namespace std;

int main (int argc, char *argv[])
{
  int tests;
  cin >> tests;
  for (int test = 1; test <= tests; test++) {
    cout << "Case #" << test << ": ";
    string s;
    cin >> s;
    int n = s.length(), j = n;
    for (int i = n-2; i >= 0; --i) if (s[i] > s[i+1]) s[i]--, j = i+1;
    for (int i = j; i < n; ++i) s[i] = '9';
    for (int i = 0; i < n; ++i) if (s[i] > '0') cout << s[i];
    cout << endl;
  }
  return 0;
}
