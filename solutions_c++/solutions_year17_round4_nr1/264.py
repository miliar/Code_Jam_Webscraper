//
// Created by pierre on 13.05.17.
//

#include <iostream>
#include <vector>

using namespace std;

int main()
{
  int ilez;
  cin >> ilez;
  for (int aa = 0; aa < ilez; aa++)
  {
    int N, P;

    cin >> N >> P;

    int tmp;
    int tab[3];
    tab[0] = tab[1] = tab[2] = 0;

    for (int i = 0; i < N; i++)
    {
      cin >> tmp;
      tab[tmp % P]++;
    }

    cout << "Case #" << aa + 1 << ": ";

    int res;
    if (P == 2)
    {
      res = max(0, (tab[1] ) / 2);
    }
    else
    {
      int mini = min(tab[1], tab[2]);
      int maxi = max(tab[1], tab[2]);
      res = mini;
      maxi -= mini;
      res += (maxi * 2) / 3;
    }

    cout << N - res << endl;

  }
}
