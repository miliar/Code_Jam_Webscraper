#include <cstdio>
#include <cstring>
#include <ctime>
#include <stack>
#include <queue>
#include <bitset>
#include <algorithm>
#include <iostream>
using namespace std;

const static int MAXT = 100;
const static int MAXS = 1000;
const static int MAXK = MAXS;


int doCase(const string &setup, int K) {
    static string maskstr(MAXK, '1');

    bitset<MAXS> storage(setup, 0, string::npos,
                         '+', // zero
                         '-'); // one
    bitset<MAXK> mask(maskstr, 0, K);
    int S = setup.size();

    int count = 0;
    // no need to flip: storage[pos] == 0
    // need to flip: storage[pos] == 1
    for (int pos = 0; pos <= S - K; ++pos) {
        if (storage.test(pos)) {
            count += 1;
            storage ^= (mask << pos);
        }
    }
    return storage.none() ? count : -1;
}

int main()
{
#ifdef ACM_LOCAL
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif // ACM_LOCAL

    int T;

    cin >> T;

    for (int i = 0; i != T; ++i) {
        string line;
        int K;
        cin >> line >> K;
        auto ans = doCase(line, K);

        cout << "Case #" << i + 1 << ": ";
        if (ans < 0) {
            cout << "IMPOSSIBLE";
        } else {
            cout << ans;
        }
        cout << endl;
    }


#ifdef ACM_LOCAL_TIME
    printf("Used time: %lf\n", clock() / (double) CLOCKS_PER_SEC);
#endif // ACM_LOCAL
    return 0;
}
