#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++)
    {
        int count = 0;
        bool flag = true;
        string s;
        int k;
        cin >> s >> k;
        int len = s.length();
        for(int i = 0; s[i] != '\0'; i++)
        {
            if(s[i] == '-')
            {
                for(int j = i; (j < k+i); j++)
                {
                    if(j < len)
                    {
                        if(s[j] == '-')
                            s[j] = '+';
                        else
                            s[j] = '-';
                    }
                    else
                    {
                        flag = false;
                        goto done;
                    }
                }
                count ++;
            }
        }
        done:
        for(int i = 0; s[i] != '\0'; i++)
        {
            if(s[i] == '-' || flag == false)
            {
                cout << "Case #" << t << ": IMPOSSIBLE";
                flag = false;
                break;
            }
        }
        if(flag)
        {
            cout << "Case #" << t << ": " <<count;
        }
        cout << "\n";
    }

}
