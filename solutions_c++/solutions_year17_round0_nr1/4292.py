#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

int num(string& S, int K)
{
    int num = 0;

    for (int i = 0; i < S.size() - K; ++i)
    {
        if (S[i] == '-')
        {
            for (int j = i; j < i + K; ++j)
            {
                S[j] = (S[j] == '+') ? '-' : '+';
            }
            
            ++num;
        }
    }

    if (S[S.size() - K] == '-')
    {
        ++num;
    }

    for (int i = S.size() - K + 1; i < S.size(); ++i)
    {
        if (S[i] != S[i - 1])
        {
            num = -1;
            break;
        }
    }

    return num;
}

int main(int argc, char* argv[])
{
    int T;
    cin >> T;

    for (int i = 0; i < T; ++i)
    {
        string S;
        cin >> S;

        int K;
        cin >> K;

        int ans = num(S, K);
        
        cout << "Case #" << i + 1 << ": ";
        if (ans == -1)
        {
            cout << "IMPOSSIBLE";
        }
        else
        {
            cout << ans;
        }
        cout << endl;
    }
}