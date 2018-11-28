#include <vector>
#include <deque>
#include <set>
#include <map>
#include <iostream>
#include <string>
#include <sstream>

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

int main()
{
    LL T; cin>>T;
    for(LL t=0; t<T; t++)
    {
        string s; cin>>s;
        int k; cin >>k;
        cout << "Case #" << t+1 << ": ";

        int iRem = s.length();

        int ans=0;
        while(iRem>=k) {
            if(s[s.length()-iRem] == '-') {
                ans++;
                for(int i=0; i<k; i++) {
                    int iPos = i+(s.length()-iRem);
                    char c = s[iPos];
                    if(c=='+') {
                        s[iPos] = '-';
                    }
                    else {
                        s[iPos] = '+';
                    }
                }
            }
            iRem--;
        }
        if(s.find('-') != string::npos) {
            cout << "IMPOSSIBLE";
        } else {
            cout << ans;
        }
        cout << endl;
    }

    return 0;
}

