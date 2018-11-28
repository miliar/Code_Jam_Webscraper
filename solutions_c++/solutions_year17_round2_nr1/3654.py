#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iomanip>

using namespace std;

int main()
{  
  int T, D, N;

  cout << fixed;
  cout << setprecision(7);

  cin >> T;

  for(int i = 0; i < T; ++i) 
  {
    if((i+1) == 25)
      int y = 6;

      cin >> D >> N;

      float maxT = 0;

      for(int j = 0; j < N; j++)
      {
          long K, v;
          float t;

          cin >> K >> v;
          t = float(D - K) / v;

          maxT = t > maxT? t : maxT;
      }

      float maxV = D / maxT;

      cout << "CASE #" << i+1 << ": " << maxV << '\n';
  }

  cout.flush();

  return 0;
}