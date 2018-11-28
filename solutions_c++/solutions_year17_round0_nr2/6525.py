//
// Created by pierre on 08.04.17.
//

#include <iostream>

using namespace std;

int main()
{
  int ilez;
  cin >> ilez;
  for (int aa = 0; aa < ilez; aa++)
  {
    string s;
    cin >> s;

    for (int i = 1; i < s.size(); i++)
    {
      if (s[i] < s[i - 1])
      {
        while (i > 0 && s[i] < s[i - 1])
        {
          i--;
          s[i]--;
        }

        for (i++; i < s.size(); i++)
        {
          s[i] = '9';
        }

        if (s[0] == '0')
        {
          s.erase(0, 1);
        }

        break;
      }
    }

    cout << "Case #" << aa + 1 << ": ";
    cout << s << endl;
  }
}