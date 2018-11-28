#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

string flip(int beg, int k, string s)
{
    if ((beg + k) > s.size())
        return s;
    else
    {
        for (int i = beg; i < beg + k; i++)
        {
            if (s[i] == 43)
                s[i] = 45;
            else
                s[i] = 43;
        }
        return s;
    }
}

int main()
{
    string pancake, result;
    int t, k, flips;
    scanf("%d", &t);
    for (int i = 1; i <= t; i++)
    {
        cin >> pancake;
        scanf("%d", &k);
        int d = pancake.size();
            flips = 0;
            result = " ";
            for (int j = 0; j < d; j++)
            {
                if (pancake[j] == 45)
                {
                    pancake = flip(j, k, pancake);
                    flips++;
                }
            }
            for (int j = 0; j < d; j++)
            {
                if (pancake[j] != 43)
                    result = "IMPOSSIBLE";
            }
            if (result == "IMPOSSIBLE")
                 cout << "Case #" << i <<": " << result << endl;
            else
                 cout << "Case #" << i <<": " << flips << endl;
    }
}

