#include<stdafx.h>
#include <iostream>
#include<string>
#include<queue>
#include<map>
#include <functional>
#include<algorithm>
#include<math.h>
using namespace std;
int main()
{
    long long int test;
    cin >> test;
    int test1 = 1;
    while (test--)
    {
        long long int r, c;
        cin >> r >> c;
        char** s = new char*[r];
        for (long long int i = 0; i < r; i++)
        {
            s[i] = new char[c];
            cin >> s[i];
        }
        vector<long long int>col(c,-2);
        for (long long int i = 0; i < c; i++)
        {
            long long int prev = -1;
            char cur;// = s[j][i];
            int flag = 0;
            for (long long int j = 0; j < r; j++)
            {
                if (s[j][i] != '?')
                {
                    flag = 1;
                    cur = s[j][i]; 
                    long long int p = prev + 1;
                    while (p<r && (p==j || s[p][i]=='?'))
                    {
                        s[p][i] = cur;
                        p++;
                    }
                    j = p-1; prev = j;
                }
            }
            if (flag == 0)
                col[i] = -1;
        }
        long long int pp = 0,prev = 0;
        for (long long int i = 0; i < c; i++)
        {
            if (col[i] == -2)
            {
                for (long long int p = i - 1; p >= 0; p--)
                {
                    if (col[p] != -1 || col[p] == -2)
                        break;
                    else
                        col[p] = i;
                }
                for (long long int p = i + 1; p < c; p++)
                {
                    if (col[p] != -1 || col[p] == -2)
                        break;
                    else
                        col[p] = i;
                }
            }
        }


        cout << "Case #"<<test1<<":"<< endl;
        for (long long int i = 0; i < r; i++)

        {
            for (long long int j = 0; j < c; j++)
            {
                if (col[j] == -2)
                {
                    long long int cp = j;
                    cout << s[i][cp];
                }
                else
                {
                    long long int cp = col[j];
                    cout << s[i][cp];
                }
            }
            cout << endl;
        }
        test1++;
    }
    return 0;
}

