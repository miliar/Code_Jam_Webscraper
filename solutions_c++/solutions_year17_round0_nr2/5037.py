#include <iostream>
#include <vector>
#include <cmath>
#include <bitset>
#include <string>

using namespace std;

#define debug(x) cout << #x << ": " << x << endl;

bool ok(const unsigned long long input) {
  string t = to_string(input);
  for (int i = 1; i < t.size(); ++i) {
    if (t.at(i) < t.at(i-1)) return false;
  }
  return true;
}

void compute()
{
  unsigned long long  input;
  cin >> input;

  while (true) {
    string t = to_string(input);
    bool all_good = true;

    for (int i = t.size() - 1; i > 0; --i) {
      if (t.at(i) < t.at(i-1)) {
        string substr = t.substr(i+1);
        unsigned long long temp = stoull(substr != "" ? substr : "0");
        input -= temp + 1;
        all_good = false;
        break;
      }
    }
    if (all_good) break;
  };

  cout << input << endl;
}

int main()
{
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i)
  {
    cout << "Case #" << i << ": "; compute();
  }
}
