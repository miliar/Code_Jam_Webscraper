#include <bits/stdc++.h>
#define DEBUG(x) cout << #x << " = " << x << endl;
using namespace std;
const int MAXN = 1005;

int buyerCnt[MAXN];
int placeCnt[MAXN];
int N, M, C;

bool possible(int coasterCnt, int& swaps)
{
    for (int i = 1; i <= C; i++)
    {
        if (coasterCnt < buyerCnt[i]) return false;
    }

    int free = 0;
    int currSwaps = 0;
    for (int i = 1; i <= N; i++)
    {
        if (placeCnt[i] > coasterCnt + free) return false;

        if (placeCnt[i] <= coasterCnt)
        {
            free += coasterCnt - placeCnt[i];
        }
        else
        {
            currSwaps += placeCnt[i] - coasterCnt;
            free -= placeCnt[i] - coasterCnt;
        }
    }

    swaps = currSwaps;
    return true;
}

int main()
{
    freopen("inputB.in" , "r" , stdin );
    freopen("outputB.out" , "w" , stdout );

    int T;
    cin >> T;

    for (int _t = 1 ; _t <= T; _t++ )
    {
        cin >> N >> C >> M;

        for (int i = 0; i < MAXN; i++)
        {
            buyerCnt[i] = 0;
            placeCnt[i] = 0;
        }

        for (int i = 1; i <= M; i++)
        {
            int place, buyer;
            cin >> place >> buyer;
            buyerCnt[buyer]++;
            placeCnt[place]++;
        }

        int coasterCnt = 1;
        int swaps = -1;
        while(!possible(coasterCnt, swaps))
        {
            coasterCnt++;
        }

        assert(swaps != -1);
        cout << "Case #" << _t << ": " << coasterCnt  << " " << swaps << endl;
    }

    return 0;
}
