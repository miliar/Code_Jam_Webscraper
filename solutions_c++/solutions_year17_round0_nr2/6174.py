#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

void tidy(vector<int>& s);

int main()
{
  int cases;
  cin >> cases;

  for (int theCase = 1; theCase <= cases; theCase++)
  {
    string str;
    cin >> str;

    vector<int> s;

    for (size_t i = 0; i < str.size(); i++)
      s.push_back(str[i] - '0');

    tidy(s);

    cout << "Case #" << theCase << ": ";
    for (size_t i = 0; i < s.size(); i++)
      if (s[i] != 0) cout << s[i];
    cout << "\n";
  }

  return 0;
}

void tidy(vector<int>& s)
{
  if (s.size() == 1)
    return;

  for (size_t i = s.size() - 1; i > 0; i--)
  {
    if (s[i - 1] > s[i])
    {
      s[i - 1] = s[i - 1] - 1;

      for (size_t k = i; k < s.size(); k++)
        s[k] = 9;
    }
  }
}

