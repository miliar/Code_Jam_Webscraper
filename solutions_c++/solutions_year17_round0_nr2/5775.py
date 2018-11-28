#include <iostream>
#include <string>
#include <cstdlib>
#include <stdio.h>


using namespace std;

void probA(){
    int t, k;
    string s;
    cin >> t;
    int res;
    bool can;

    for (int c=1; c<=t; c++){
        cin >> s >> k;
        cout << "Case #" << c << ": ";
        can  = true;
        res=0;
        for (int i=0; i<s.size(); i++){
            if (s[i] == '-'){
                int j;
                for ( j=i; j<s.size()&&j<(i+k); j++){
                    s[j] = (s[j] == '+')? '-':'+';
                }

                if (j < i+k){
                    can = false;
                    break;
                }
                res++;

            }
            if (!can)
                break;
        }

        if (can)
            cout<< res << endl;
        else
            cout << "IMPOSSIBLE\n";

    }
}

void probB(){
    int t;
    cin >> t;
    string strNum;
    int sz ;
    for (int c=1; c<=t; c++){
        cin >> strNum;
        cout << "Case #" << c << ": ";
        sz = strNum.size();
        int ind=0;
        while (ind < (sz-1) && strNum[ind] <= strNum[ind+1]) ind++;
        if (ind < (sz-1)) {
            while (ind > 0 && (strNum[ind] == strNum[ind - 1]) ) ind--;

            strNum[ind] = strNum[ind]-1;
            ind++;
            while (ind < sz){
                strNum[ind++] = '9';
            }

            if (strNum[0] == '0')
                strNum = strNum.substr(1, sz-1);
        }

        cout << strNum << endl;


    }
}
int main() {
    //cout << "Hello, World!" << endl;
    freopen ("in.txt", "r", stdin);
    freopen ("out.txt", "w", stdout);

    probB();
    return 0;
}