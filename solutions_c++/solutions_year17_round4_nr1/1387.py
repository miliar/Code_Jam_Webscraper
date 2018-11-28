#include <bits/stdc++.h>
using namespace std;

int dp3[101][101];
int dp4[101][101][101];

int solve3(const int N, const vector<int>& counts)
{
    memset(dp3, 0, sizeof(dp3));
    for (auto iterations = 0; iterations < N; iterations++)
        for (auto i = counts[1]; i >= 0; i--)
            for (auto j = counts[2]; j >= 0; j--)
            {
                const auto fresh = (i + 2*j) % 3 == 0;
                const auto option = fresh + dp3[i][j];
                if (i != counts[1])
                    dp3[i+1][j] = max(dp3[i+1][j], option);
                if (j != counts[2])
                    dp3[i][j+1] = max(dp3[i][j+1], option);
            }
    return counts[0] + dp3[counts[1]][counts[2]];
}

int solve4(const int N, const vector<int>& counts)
{
    memset(dp4, 0, sizeof(dp4));
    for (auto iterations = 0; iterations < N; iterations++)
        for (auto i = counts[1]; i >= 0; i--)
            for (auto j = counts[2]; j >= 0; j--)
                for (auto k = counts[3]; k >= 0; k--)
                {
                    const auto fresh = (i + 2*j + 3*k) % 4 == 0;
                    const auto option = fresh + dp4[i][j][k];
                    if (i != counts[1])
                        dp4[i+1][j][k] = max(dp4[i+1][j][k], option);
                    if (j != counts[2])
                        dp4[i][j+1][k] = max(dp4[i][j+1][k], option);
                    if (k != counts[3])
                        dp4[i][j][k+1] = max(dp4[i][j][k+1], option);
                }
    return counts[0] + dp4[counts[1]][counts[2]][counts[3]];
}

void solve_case()
{
    int N, P; cin >> N >> P;

    auto counts = vector<int>(P);
    for (auto i = 0; i < N; i++)
    {
        int G; cin >> G;
        counts[G%P]++;
    }

    if (P == 2) cout << counts[0] + (counts[1]+1)/2 << endl;
    if (P == 3) cout << solve3(N, counts) << endl;
    if (P == 4) cout << solve4(N, counts) << endl;
}

int main()
{
    int T; cin >> T;
    for (auto t = 1; t <= T; t++)
    {
        cerr << t << endl;
        cout << "Case #" << t << ": ";
        solve_case();
    }
}
