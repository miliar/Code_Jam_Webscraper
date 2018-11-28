#include <iostream>
#include <fstream>
#include <string>
using namespace std;


int main()
{
    int T;
    cin >> T;
    string strCakeList;
    int K;
    int nListlen, Pidx, nFlipCnt;
    int bPassFilp = 1;
    for (int Tidx=0; Tidx<T; Tidx++) {
       cin >> strCakeList >> K;
       nListlen = strCakeList.length();
       nFlipCnt = 0;
       bPassFilp = 1;
       for(Pidx = 0;Pidx<nListlen-K+1; Pidx++) {
            if(strCakeList[Pidx]=='-') {
                nFlipCnt++;
                for (int Fidx=Pidx;Fidx<Pidx+K;Fidx++) {
                    if (strCakeList[Fidx]=='-')
                        strCakeList[Fidx]='+';
                    else
                        strCakeList[Fidx]='-';
                }
            }
       }
       for(;Pidx<nListlen; Pidx++) {
            if (strCakeList[Pidx]=='-') {
                bPassFilp = 0;
                break;
            }
       }
       cout << "Case #" << Tidx+1 << ": ";
       if (bPassFilp)
            cout << nFlipCnt;
       else
            cout << "IMPOSSIBLE";
       cout << endl;
    }

    return 0;
}
