/**
 * http://code.google.com/codejam/contest/3264486/dashboard#s=p0
 */

#include <bits/stdc++.h>

using namespace std;

int solve(const string& S, int K)
{
    auto N = S.size();

    int counts[N + 1];
    fill(counts, counts + N + 1, 0);

    int count = 0;
    int cur_count = 0;
    for (size_t i = 0; i < N; ++i)
    {
        cur_count += counts[i];

        if ((S[i] == '+') == (cur_count % 2 == 0)) continue; // already '+'

        // '-'

        if (i + K > N) return -1; // impossible

        ++count;
        ++cur_count;
        --counts[i + K];
    }

    return count;
}

int main()
{
    int T;
    cin >> T;

    for (int t = 1; t <= T; ++t)
    {
        string S;
        int K;
        cin >> S >> K;
        auto answer = solve(S, K);

        cout << "Case #" << t << ": ";
        if (answer < 0) cout << "IMPOSSIBLE\n";
        else cout << answer << '\n';
    }

    return 0;
}
