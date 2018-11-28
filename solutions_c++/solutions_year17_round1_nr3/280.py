#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <cstdlib>
#include <map>
#include <set>
#include <queue>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int tc;
	cin >> tc;
  for (int tt=1; tt<=tc; tt++)
  {
    int hd,ad,hk,ak,b,d;
    int minturn = 10000;
    cin >> hd >> ad >> hk >> ak >> b >> d;
    for (int nd = 0; nd <= (d==0?0:ak); nd++)
      for (int nb = 0; nb <= (b==0?0:hk); nb++)
      {
        int failure=0;
        int chd=hd, cad=ad, chk=hk, cak=ak, rb=nb, rd=nd, turn=0;
        while (chk>0)
        {
          turn++;
          if (turn == 10000)
            break;
          if (cad >= chk)
            break;
          if (chd <= cak-d*(rd>0))
            chd = hd;
          else
          {
            if (rd > 0)
            {
              cak -= d;
              rd --;
            }
            else if (rb > 0)
            {
              cad += b;
              rb--;
            }
            else
              chk -= cad;
          }
          chd -= cak;
          if (chd <= 0)
          {
            failure = 1;
            break;
          }
        }
        if ((!failure) && turn < minturn)
          minturn = turn;
      }
    cout << "Case #" << tt << ": " ;
    if (minturn == 10000)
      cout << "IMPOSSIBLE" << endl;
    else
      cout << minturn << endl;
  }
}
