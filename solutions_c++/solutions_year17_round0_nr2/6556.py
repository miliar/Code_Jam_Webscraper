#include <bits/stdc++.h>
#define int long long
using namespace std;

int result;

void solve(int actNum, int const & N) {

    for (int i = 9; i >= 1 && i >= actNum%10; --i) {
        int tempNum = actNum*10 + i;

        if (tempNum <= N) {
            result = max(result, tempNum);
            solve(tempNum, N);
        }
    }
}

main() {
    ios_base::sync_with_stdio(false);

    int T;
    cin >> T;

    for (int caseNum = 1; caseNum <= T; ++caseNum) {

        int N;
        cin >> N;

        result = 0LL;
        solve(0, N);

        cout << "Case #" << caseNum << ": " <<  result << endl;
    }
    return 0;
}
