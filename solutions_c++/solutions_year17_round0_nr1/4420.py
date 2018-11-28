#include <bits/stdc++.h>
using namespace std;

int main()
{
    int tetC;

    cin >> tetC;

    for(int cnt = 0; cnt < tetC; cnt++) {

        long long ret = 0;

        string curVal;

        int tVal;

        cin >> curVal >> tVal;

        for(int ct = 0; ct <= (curVal.size() - tVal); ct++) {

        if(curVal[ct] == '-') {

            ret++;

            for(int ctc = 0; ctc < tVal; ctc++) {

            curVal[ct + ctc] = curVal[ct + ctc] == '-' ? '+' : '-';

            }

        }

    }

    bool ft = true;

    for(int ct = 0; ct < curVal.size(); ct++) {

        if(curVal[ct] == '-') {

            ft = false;

            break;

        }

    }

    if(ft)
        //Case #1: 3
        cout << "Case #"<<cnt+1 << ": " << ret << endl;

    else

        cout << "Case #"<<cnt+1 << ": " << "IMPOSSIBLE" << endl;

    }

return 0;
}
//////////////////////////////
