#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream cin("B.in");
    ofstream cout("B.out");
    int T;
    cin >> T;
    for (int t = 0; t < T; t++)
    {
        string S;
        cin >> S;
        int m = 0;
        while(m < S.size()-1 && S[m] <= S[m+1])
            m++;
        for (int i = m+1; i < S.size(); i++)
        {
            S[i] = '9';
        }
        if (m+1 < S.size())
        {
            S[m]--;
            while(m > 0 && S[m-1] > S[m])
            {
                S[--m]--;
                S[m+1] = '9';
            }
        }
        cout << "Case #" << t+1 << ": ";
        if (S[0] == '0')
        {
            for (int i = 1; i < S.size(); i++)
            {
                cout << 9;
            }
        }
        else
        {
            cout << S;
        }
        cout << endl;
    }

}
