#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>

using namespace std;

const int maxn = 1e5 + 10;



int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    int cas = 0;
    while (T--)
    {
        cout << "Case #" << ++cas << ": ";
        string s;
        int k;
        cin >> s >> k;
        int size = s.size();
        int flag = 0;
        int sum = 0;
        for (int i = 0; i < size; ++i)
        {
            if (s[i] == '-')
            {
                sum++;
                if (size - i < k)
                {
                    flag = 1;
                    break;
                }
                for (int j = i; j < i + k; ++j)
                {
                    if (s[j] =='-')
                    {
                        s[j] = '+';
                    }
                    else
                    {
                        s[j] = '-';
                    }
                }
            }
        }
        if (flag)
        {
            cout << "IMPOSSIBLE\n";
        }
        else
        {
            cout << sum << endl;
        }
    }
    
    


    return 0;
}