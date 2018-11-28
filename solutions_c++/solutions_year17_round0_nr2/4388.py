#include <bits/stdc++.h>
using namespace std;



int main()
{

    int tetC;

    cin >> tetC;

    for(int cnt = 0; cnt < tetC; cnt++) {

        string curVal;

        cin >> curVal;

        int badFound = -1;

        for(int ct = 0; ct < curVal.size() - 1; ct++) {

            if(curVal[ct] > curVal[ct + 1]) {

                badFound = ct;

                for(int ctc = ct - 1; ctc >= 0; ctc--) {

                    if(curVal[ct] == curVal[ctc]) {

                        badFound = ctc;

                    }

                }
                break;
            }

        }

        string ret = "";

        if(badFound == -1)

            ret = curVal;

        else {

            for(int ct = 0; ct < badFound; ct++) {

                ret += curVal[ct];

        }

        int remLen = curVal.size() - badFound - 1;

        if(curVal[badFound] > '1') {

        ret += (curVal[badFound] - 1);

        }

        for(int ct = 0; ct < remLen; ct++)

        ret += '9';

        }



        cout << "Case #"<<cnt+1<<": "<< ret << endl;

    }

return 0;

}

//////////////////////////////
