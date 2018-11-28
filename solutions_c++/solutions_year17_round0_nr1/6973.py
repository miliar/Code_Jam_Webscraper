#include <bits/stdc++.h>
#define endl "\n"
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    //freopen("A-large.in", "r", stdin);
    //freopen("output.txt", "w", stdout);
    string str;
    int tc, cases = 1;
    int k, len, counts, i;
    bool flag;
    cin >> tc;
    while(tc--)
    {
        flag = true;
        cin >> str >> k;
        len = str.length();
        counts = 0;
        for(i = 0; i <= len - k; i++)
        {
            if(str[i] == '-')
            {
                counts++;

                for(int j = i; j < i + k; j++)
                {
                    if(str[j] == '-')
                        str[j] = '+';
                    else
                        str[j] = '-';
                }
            }
        }
        for(; i < len; i++)
        {
            if(str[i] == '-')
            {
                flag = false;
                break;
            }
        }
        if(flag)
            cout << "Case #" << cases++ <<": " << counts << endl;
        else
            cout << "Case #" << cases++ <<": " << "IMPOSSIBLE" << endl;


    }
}
