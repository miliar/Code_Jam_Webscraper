#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <climits>

using namespace std;

int solve(string S, int K) {
        int x = 0, n = S.size();
        for (int i = 0; i < n - K + 1; i++) {
                if (S[i] == '+')
                        continue;
                x++;
                for (int j = i; j < i + K; j++)
                        S[j] = S[j] == '-' ? '+' : '-';
        }
        for (int i = n - K; i < n; i++) {
                if (S[i] == '-') {
                        x = -1;
                        break;
                }
        }
        return x;
}

int main(int argc, char **argv)
{
        int T;
        cin >> T;
        for (int testcase = 0; testcase < T; testcase++) {
                int K;
                string S;
                cin >> S >> K;
                int x = solve(S, K);
                cout << "Case #" << testcase+1 << ": ";
                if (x < 0)
                        cout << "IMPOSSIBLE";
                else
                        cout << x;
                cout << endl;
        }
        return 0;
}
