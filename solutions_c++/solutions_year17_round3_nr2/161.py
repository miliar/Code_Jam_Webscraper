#include <bits/stdc++.h>
#define DEBUG(x) cout << #x << " = " << x << endl;
using namespace std;
const int MAXN = 24 * 60;
const int HALF = 12 * 60;
const int inf = 1000000;

int dp[MAXN][2][MAXN][2];
int timeLine[MAXN];

void Init()
{
    for (int i = 0; i < MAXN; i++)
    {
        timeLine[i] = inf;
    }

    for (int i = 0; i < MAXN * 2 * MAXN * 2; i++)
    {
        int x = i;
        int firstSits = x % 2;    x /= 2;
        int timeFirst = x % MAXN; x /= MAXN;
        int currSits  = x % 2;    x /= 2;
        int currTime  = x % MAXN; x /= MAXN;

        dp[currTime][currSits][timeFirst][firstSits] = inf;
    }
}

int main()
{
    freopen("inputB.in" , "r" , stdin );
    freopen("output.out" , "w" , stdout );

    int T;
    cin >> T;

    for (int _t = 1 ; _t <= T; _t++ )
    {
        Init();

        int A[2];
        cin >> A[0] >> A[1];

        for (int person = 0; person < 2; person++)
        {
            for (int i = 0; i < A[person]; i++)
            {
                int L, R;
                cin >> L >> R;
                for (int t = L; t < R; t++)
                {
                    timeLine[t] = 1 - person;
                }
            }
        }

        for (int i = 0; i < MAXN * 2 * MAXN * 2; i++)
        {
            int x = i;
            int firstSits = x % 2;    x /= 2;
            int timeFirst = x % MAXN; x /= MAXN;
            int currSits  = x % 2;    x /= 2;
            int currTime  = x % MAXN; x /= MAXN;

            if (timeLine[currTime] != inf && timeLine[currTime] != currSits)
            {
                continue;
            }

            if (currSits == 0 && timeFirst == 0)
            {
                continue;
            }

            if (currSits == 1 && timeFirst == currTime + 1)
            {
                continue;
            }

            if (timeFirst > currTime + 1)
            {
                continue;
            }

            if (currTime == 0)
            {
                if (currSits == firstSits)
                {
                    dp[currTime][currSits][timeFirst][firstSits] = 0;
                }
            }
            else
            {
                int prevTimeFirst = timeFirst - (currSits == 0);
                for (int prevSits = 0; prevSits < 2; prevSits++)
                {
                    int res = dp[currTime - 1][prevSits][prevTimeFirst][firstSits] + (prevSits != currSits);
                    dp[currTime][currSits][timeFirst][firstSits] = min(dp[currTime][currSits][timeFirst][firstSits], res);
                }
            }
        }

        /// No midnight change
        int resNoMidnight = min(dp[MAXN - 1][0][HALF][0], dp[MAXN - 1][1][HALF][1]);
        /// Midnight change
        int resMidnight = min(dp[MAXN - 1][0][HALF][1], dp[MAXN - 1][1][HALF][0]) + 1;

        int res = min(resNoMidnight, resMidnight);
        assert(res != inf);

        cout << "Case #" << _t << ": " << res << endl;
    }

    return 0;
}
