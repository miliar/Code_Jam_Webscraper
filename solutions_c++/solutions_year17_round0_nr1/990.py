#include <iostream>
#include <string>
using namespace std;

int T, N, K;
string S;

int go()
{
    int ans = 0;
    for (int i = 0; i < N; i++)
        if (S[i] == '-')
        {
            if (i + K - 1 >= N)
                return -1;
            ans++;
            for (int j = 0; j < K; j++)
            {
                if (S[i + j] == '-')
                    S[i + j] = '+';
                else
                    S[i + j] = '-';
            }
        }
    return ans;
}

int main()
{
    ios::sync_with_stdio(0);

    freopen("Ain.txt", "r", stdin);
    freopen("Aout.txt", "w", stdout);

    cin >> T;
    for (int t = 1; t <= T; t++)
    {
        cin >> S >> K;
        N = S.size();
        int ans = go();
        cout << "Case #" << t << ": ";
        if (ans == -1)
            cout << "IMPOSSIBLE\n";
        else
            cout << ans << "\n";
    }

    return 0;
}
