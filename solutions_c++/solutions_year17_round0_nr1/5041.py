#include <iostream>
#include <vector>
#include <bitset>
#include <string>

using namespace std;

#define debug(x) cout << #x << ": " << x << endl;

void compute()
{
  string input;
  int S;
  cin >> input >> S;
  int count = 0;
  bool neg = true;

  for (int i = 0; i < input.size() - S + 1; i++)
  {
    if (input.at(i) == '-') {
      count++;
      for (int j = 0; j < S; ++j) {
        if (input.at(i+j) == '+') input.at(i+j) = '-';
        else if (input.at(i+j) == '-') input.at(i+j) = '+';
      }
    }
  }

  for (int i = 0; i < input.size(); i++)
  {
    if (input.at(i) == '-') {
      cout << "IMPOSSIBLE" << endl;
      return;
    }
  }


  cout << count << endl;
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
