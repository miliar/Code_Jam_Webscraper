#include <iostream>
#include <fstream>
#include <string>
using namespace std;


int main()
{
    int T;
    cin >> T;
    string strN;
    string strOut;
    int nListlen;
    int bPass = 1;
    int Fidx;
    for (int Tidx=0; Tidx<T; Tidx++) {
       cin >> strN;
       nListlen = strN.length();
       strOut.clear();
       bPass = 1;
       for(int Pidx=1;Pidx<nListlen;Pidx++) {
            if (strN[Pidx]>=strN[Pidx-1])
               continue;
            else {
                bPass = 0;
                Fidx = Pidx-1;
                while(Fidx>0) {
                    if (strN[Fidx]-1>=strN[Fidx-1])
                        break;
                    else
                        Fidx--;
                }
                break;
            }
       }
       if (bPass)
            strOut = strN;
       else {
           if (Fidx == 0) {// first char
                if (strN[0]>'1')
                    strOut += strN[0]-1;
                for (int idx = 0;idx<nListlen-1;idx++)
                    strOut += '9';
           }
           else {
                for (int idx = 0;idx<Fidx;idx++)
                    strOut += strN[idx];
                strOut += strN[Fidx]-1;
                for (int idx = Fidx+1;idx<nListlen;idx++)
                    strOut += '9';
           }
       }
       cout << "Case #" << Tidx+1 << ": ";
       cout << strOut;
       cout << endl;
    }

    return 0;
}
