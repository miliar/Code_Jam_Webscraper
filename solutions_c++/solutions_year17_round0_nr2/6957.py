#include <bits/stdc++.h>
#define endl "\n"
using namespace std;

bool done(string num)
{
    int len = num.length();
    for(int i = 0; i < len - 1; i++)
    {
        if(num[i + 1] < num[i])
            return false;
    }
    return true;
}

int main()
{
    ios::sync_with_stdio(false);
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    string str;
    int tc, cases = 1, len;
    cin >> tc;
    while(tc--)
    {
        cin >> str;
        len = str.length();
        while(!done(str))
        {
            for(int i = 1; i < len; i++)
            {
                if(str[i - 1] > str[i])
                {
                    if(str[i - 1] == '0')
                        str[i - 1] = '9';
                    else
                        str[i - 1] -= 1;

                    for(int j = i; j < len; j++)
                        str[j] = '9';
                }
            }
            //cout << str << endl;
        }

        for(int i = 0; str[i] == '0'; i++)
        {
            str = str.substr(1, str.size());
        }
        cout << "Case #" << cases++ << ": " << str << endl;
    }
    return 0;
}

