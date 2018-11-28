//
// Created by pierre on 08.04.17.
//

#include <iostream>
#include <vector>

using namespace std;

int backFlip[1009];

int main()
{
  int ilez;
  cin >> ilez;
  for (int aa = 0; aa < ilez; aa++)
  {
    string s;
    cin >> s;
    int n = s.size();
    int flipperSize;
    cin >> flipperSize;

    vector<int> vec;
    for (int i = 0; i < n; i++)
      vec.push_back(s[i] == '+' ? 1 : 0);

    int res = 0;
    int isFlipping = 0;
    int dasie = 1;

    for (int i = 0; i < n; i++)
      backFlip[i] = 0;

    for (int i = 0; i < n; i++)
    {
      if (!(isFlipping ^ vec[i]))
      {
        if (i + flipperSize - 1 >= n)
        {
          dasie = 0;
          break;
        }
        res++;
        isFlipping = (isFlipping + 1) % 2;
        backFlip[i + flipperSize - 1] = 1;
      }
      isFlipping = (isFlipping + backFlip[i]) % 2;
    }

    cout << "Case #" << aa + 1 << ": ";
    if (dasie)
      cout << res;
    else
      cout << "IMPOSSIBLE";
    cout << endl;
  }
}