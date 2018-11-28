#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t; cin >> t;
    for(int Case = 1; Case <= t; Case++)
    {
        string pancakes; cin >> pancakes;

        int k; cin >> k;
        int n = pancakes.size();
        int f = 0;
        for(int i = 0; i <= n-k; i++)
        {
            if(pancakes[i] == '-')
            {
                f++;
                for(int j = 0; j < k; j++)
                {
                    pancakes[i+j] = pancakes[i+j] == '+' ? '-':'+';
                }
            }
            //cout << pancakes << endl;
        }

        bool pos = true;
        for(int i = 1; i < k; i++)
        {
            if(pancakes[n-i] == '-') pos = false;
        }
        if(pos)
        {
            printf("Case #%d: %d\n", Case, f);
        }
        else
        {
            printf("Case #%d: IMPOSSIBLE\n", Case);
        }
    }
    return 0;
}

// +++---++++++++++++++
