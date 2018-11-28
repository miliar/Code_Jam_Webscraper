// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <string>
using namespace std;

int main()
{
    int T;
    cin >> T;
    int t = 0;
    while (++t <= T)
    {
        string str;
        cin >> str;
        int n = str.length();
        int x = 0;
        int subStart = 0;
        for (int i = 0;i < n - 1;i++)
        {
            if (str[i] > str[i + 1])
            {
                int start = i;
                bool hasDif = false;
                for (int j = i - 1;j >= 0;j--)
                {
                    if (str[j] != str[i])
                    {
                        hasDif = true;
                        start = j + 1;
                        break;
                    }
                    
                }
                if (!hasDif)
                {
                    start = 0;
                }
                str[start] = str[start] - 1;
                if (start == 0 && str[start] == '0')
                {
                    subStart = start + 1;
                }
                for (int j = start + 1;j < n;j++)
                {
                    str[j] = '9';
                }
                break;
            }
        }

        cout << "Case #" << t << ": " << str.substr(subStart) << endl;
    }
}

