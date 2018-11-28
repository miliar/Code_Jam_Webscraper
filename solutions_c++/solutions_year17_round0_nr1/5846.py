#include<stdafx.h>
#include <iostream>
#include<string>
using namespace std;
int main()
{
    int test;
    cin >> test;
    int test1 = 1;
    while (test--)
    {
        
        string s;
        cin >> s;
        int k;
        cin >> k;
        int i = 0,cou = 0;
        for (; i < s.length(); i++)
        {
            while (i < s.length() && s[i] == '+')
                i++;
            if (s.length() - i >= k)
            {
                cou++;
                for (int j = i; j < i + k; j++)
                {
                    if (s[j] == '+')
                        s[j] = '-';
                    else
                        s[j] = '+';
                }
            }
            else if (i == s.length())
                break;
            else
            {
                cou = -1;
                break;
            }
        }
        cout << "Case #" << test1 << ": ";
        if (cou == -1)
            cout << "IMPOSSIBLE" << endl;
        else
            cout << cou << endl;
        test1++;
    }
    return 0;
}

