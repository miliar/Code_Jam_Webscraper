//
// Created by pierre on 08.04.17.
//

#include <iostream>

#define int long long

using namespace std;

main()
{
  int ilez;
  cin >> ilez;
  for (int aa = 0; aa < ilez; aa++)
  {
    int len, N;
    cin >> len >> N;

    double maxTime = 0;

    for (int i = 0; i < N; i++)
    {
      int pos, speed;
      cin >> pos >> speed;
      pos = len - pos;
      maxTime = max(maxTime, (double) pos / speed);

    }

    cout << "Case #" << aa + 1 << ": ";

    cout.precision(7);
    cout<<fixed << len / maxTime << endl;


  }
}