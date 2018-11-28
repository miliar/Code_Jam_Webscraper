#include <cstdio>
#include <cstring>
#include <ctime>
#include <stack>
#include <tuple>
#include <queue>
#include <bitset>
#include <algorithm>
#include <iostream>
using namespace std;

int significant(uint64_t K)
{
    int c = 0;
    while (K != 0) {
        K >>= 1;
        c++;
    }
    return c;
}

pair<uint64_t, uint64_t> doCase(uint64_t N, uint64_t K)
{
    /*
    if (K >= (N >> 1)) {
        return {0, 0};
    }
    */

    /*
    int sig = significant(K);
    uint64_t sigbit = (1 << (sig - 1));
    uint64_t remain = (K & ~sigbit);

    if (remain == 0) {
        remain = (1 << sig);
        sig -= 1;
    }
    int round = sig;
    */

    int round, remain;
    round = significant(K) - 1;
    remain = K - (1 << round) + 1;

    // cout << "round: " << round << " remain: " << remain << endl;

    uint64_t segLen = (N >> round);
    uint64_t segCnt = (1 << round);
    // number of minor segments (segment of length segLen -1)
    //                     supposed len       actual len = N - occupied in previous round
    uint64_t minorSegCnt = segLen * segCnt - (N - (1 << round) + 1);
    uint64_t majorSegCnt = segCnt - minorSegCnt;

    // cout << "segLen: " << segLen << " segCnt: " << segCnt << endl;
    // cout << "minorSegCnt: " << minorSegCnt << " majorSegCnt: " << majorSegCnt << endl;

    if (remain > majorSegCnt) {
        // use a minor segment
        segLen -= 1;
    }
    return {segLen - 1 - (segLen-1) / 2, (segLen - 1) / 2};
}

int main()
{
#ifdef ACM_SUBMIT
    freopen("output.txt", "w", stdout);
#endif // ACM_SUBMIT
    freopen("input.txt", "r", stdin);

    int T;

    cin >> T;

    uint64_t N, K;
    for (int i = 0; i != T; ++i) {
        cin >> N >> K;
        uint64_t y, z;
        tie(y, z) = doCase(N, K);
        cout << "Case #" << i + 1 << ": " << y << " " << z << endl;
    }

#ifdef ACM_LOCAL
    printf("Used time: %lf\n", clock() / (double) CLOCKS_PER_SEC);
#endif // ACM_LOCAL
    return 0;
}
