#include <bits/stdc++.h>

using namespace std;

#define fo "A.out"

int main()
{
    //freopen(fo,"w",stdout);
    int T;
    cin >> T;
    int test=0;
    while (T--)
    {
        test++;
        string str;
        cin >> str;
        while (true)
        {
            bool xet=true;
            for (int i=0; i<str.length()-1; ++i)
                if (str[i]>str[i+1])
                {
                    xet=false;
                    str[i]=str[i]-1;
                    for (int j=i+1; j<str.length(); ++j) str[j]='9';
                    break;
                }
            if (xet) break;
        }
        cout << "Case #" << test << ": ";
        while (str[0]=='0') str.erase(0,1);
        cout << str << '\n';
    }
}
