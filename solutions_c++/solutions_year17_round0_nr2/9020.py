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
        cin >> s;
        int size = s.size();
        for (int i = size - 2; i >= 0; --i)
        {
            if (s[i] > s[i + 1])
            {
                s[i] -= 1;
                for (int j = i + 1; j < size; ++j)
                {
                    s[j] = '9';
                }
            }
        }
        for (int i = 0; i < size; ++i)
        {
            if (s[i] != '0')
            {
                cout << s[i];
            }
        }
        cout << endl;
    }
    
    


    return 0;
}