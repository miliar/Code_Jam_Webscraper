#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main()
{
  int cases;
  cin >> cases;

  for (int theCase = 1; theCase <= cases; theCase++)
  {
    string s;
    int K, count = 0;
    bool possible = true;

    cin >> s >> K;

    for (size_t i = 0; i <= s.size() - K; i++)
    {
      if (s[i] == '-')
      {
        for (size_t k = i; k < i + K; k++)
        {
          if (s[k] == '-')
            s[k] = '+';
          else
            s[k] = '-';
        }

        count++;
      }
    }

    for (size_t i = s.size() - K; i < s.size(); i++)
    {
      if (s[i] == '-')
      {
        possible = false;
        break;
      }
    }

    cout << "Case #" << theCase << ": ";
    
    if (!possible)
      cout << "IMPOSSIBLE\n";
    else
      cout << count << "\n";
  }

  return 0;
}
