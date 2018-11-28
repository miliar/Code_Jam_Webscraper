#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for(int i = 1; i <= t; i++)
    {
        string S;
        int kapa;
        cin >> S >> kapa;
        int napa = 0;
        for(int j = 0; j <= S.size() - kapa; j++)
        {
            if(S[j] == '-')
            {
                for(int k = 0; k < kapa; k++)
                    if(S[j + k] == '-')
                        S[j + k] = '+';
                    else
                        S[j + k] = '-';
                napa++;
            }
        }
        bool alpha = true;
        for(int j = 0; j < S.size(); j++)
            if(S[j] == '-')
            {
                alpha = false;
                break;
            }
        if(!alpha)
            cout << "Case #" << i << ": IMPOSSIBLE" << endl; 
        else
            cout << "Case #" << i << ": " << napa << endl;
    }
    return 0;
}
