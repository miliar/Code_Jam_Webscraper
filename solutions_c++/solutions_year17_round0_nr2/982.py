#include <iostream>
#include <string>
using namespace std;

int T, N;
string S, ans;

void go()
{
    ans = "";
    int idx = 1;
    bool changed = false;
    for (; idx < N; idx++)
        if (S[idx - 1] > S[idx])
        {
            changed = true;
            if (S[idx - 1] == '1')
                idx = 1;
            else
            {
                for (int j = idx - 1; j >= 0; j--)
                    if (j == 0 || S[j - 1] != S[idx - 1])
                    {
                        ans += S.substr(0, j);
                        ans += (S[j] - 1);
                        idx = j + 1;
                        break;
                    }
            }
            break;
        }

    if (!changed)
    {
        ans = S;
        return;
    }

    for (; idx < N; idx++)
        ans += "9";
}

int main()
{
    ios::sync_with_stdio(0);

    freopen("Bin.txt", "r", stdin);
    freopen("Bout.txt", "w", stdout);

    cin >> T;
    for (int t = 1; t <= T; t++)
    {
        cin >> S;
        N = S.size();
        go();

        cout << "Case #" << t << ": " << ans << "\n";
    }

    return 0;
}
