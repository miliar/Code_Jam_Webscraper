#include <iostream>
#include <string>

using namespace std;

int
sw(int *N, int K) {
        int ret = 0;
        for (int i = 0; i < K; ++i) {
                if (N[i] == 0)
                        ret++;
                else
                        ret--;
                N[i] = 1 - N[i];
        }
        return ret;
}

int
solve(int *N, int len, int bc, int K)
{
        int result;

//      cout << len << " " << bc << endl;
        if (bc == 0)
                return 0;

        if (len < K)
                return -1;

        if (N[0] == 0) {
//              cout << len << " switched" << endl;
                if ((result = solve(N + 1, len - 1, bc - sw(N, K), K)) != -1)
                        return result + 1;
                else
                        return -1;
        } else {
                if ((result = solve(N + 1, len - 1, bc, K)) != -1)
                        return result;
                else
                        return -1;
        }

        return -1;
}

int
main(void)
{
        int T;
        cin >> T;


        for (int i = 0; i < T; ++i) {
                string S;
                int K;
                int *N;
                int bc = 0;
                int result;
                cin >> S >> K;

                N = new int[S.length()];
                for (int j = 0; j < S.length(); ++j) {
                        if (S[j] == '-') {
                                N[j] = 0;
                                bc++;
                        }
                        else
                                N[j] = 1;
                }

                cout << "Case #" << i+1 << ": ";
                if ((result = solve(N, S.length(), bc, K)) != -1)
                        cout << result << endl;
                else
                        cout << "IMPOSSIBLE" << endl;
        }
}