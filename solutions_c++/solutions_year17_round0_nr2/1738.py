#include <iostream>
#include <string>

using namespace std;

string lastTidy(string &num);

int main()
{
  int num_tests;
  cin >> num_tests;
  for (int test = 1; test <= num_tests; test++) {
    string num;
    cin >> num;
    cout << "Case #" << test << ": " << lastTidy(num) << '\n';
  }
  return 0;
}

string lastTidy(string &num)
{
  string final = num;
  if (num.size() <= 1)
    return num;
  for (int i = 0; i < num.size() - 1; i++) {
    string repeat = string(num.size() - 1 - i, num[i]);
    if (repeat > num.substr(i + 1)) {
      final[i]--;
      for (int j = i + 1; j < final.size(); j++)
	final[j] = '9';
      if (final[0] == '0')
	final = final.substr(1);
      return final;
    }
  }
  if (final[0] == '0')
    final = final.substr(1);
  return final;
}

