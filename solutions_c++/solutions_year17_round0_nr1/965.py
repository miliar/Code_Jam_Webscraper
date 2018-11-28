#include <iostream>
#include <string>

using namespace std;

int T, K, ans;

string S;

int main()
{
    ios::sync_with_stdio();
    cin >> T;
    for (int t = 1; t <= T; ++t)
    {
        cin >> S >> K;
        cout << "Case #" << t << ": ";
        ans = 0;
        for (int i = 0; i <= S.length() - K; ++i)
        {
            if (S[i] == '-')
            {
                ++ans;
                for (int j = i; j < i + K; ++j)
                    if (S[j] == '-')
                        S[j] = '+';
                    else
                        S[j] = '-';
            }
        }
        for (int i=S.length() - K + 1; i < S.length(); ++i)
        {
            if (S[i] == '-') 
            {
                cout << "IMPOSSIBLE" << endl;
                ans = -1;
                break;
            }
        }
        if (ans >= 0)
            cout << ans << endl;
    }
    return 0;
}