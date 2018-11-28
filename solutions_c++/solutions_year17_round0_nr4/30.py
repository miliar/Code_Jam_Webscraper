#include <string>
#include <iostream>
#include <cassert>
#include <tuple>
#include <vector>
#include <map>
#include <random>
#include <functional>
using namespace std;
using i64 = int64_t;

char CHAR_TO_ID[256];
const char ID_TO_CHAR[4] = {'.', 'x', '+', 'o'};

bool convertDiag(int d1, int d2, int N, int& x, int& y) {
    x = (d1 + d2 - N) / 2;
    y = d1 - x;
    if (x - y + N != d2) {
        return false;
    }
    return (x >= 0 && x < N && y >= 0 && y < N);
}

bool kuhn(int x, vector<bool>& was, const vector<bool>& banned, vector<int>& pr, function<bool(int,int)> ok) {
    if (was[x]) {
        return false;
    }
    was[x] = true;
    for (int y = 0; y < (int)was.size(); ++y) 
        if (!banned[y] && ok(x, y) && (pr[y] == -1 || kuhn(pr[y], was, banned, pr, ok))) {
            pr[y] = x;
            return true;
        }
    return false;
}

int main() {
    freopen(".in", "r", stdin);
    freopen(".out", "w", stdout);
    //ios::sync_with_stdio(0);

    for (int i = 0; i < 4; ++i) {
        CHAR_TO_ID[(int)ID_TO_CHAR[i]] = i;
    }

    int T;
    cin >> T;
    for (int __ = 1; __ <= T; ++__) {
        cerr << "Test " << __ << endl;

        int N, K;
        cin >> N >> K;

        int answer = 0;
        vector<bool> fixedR(N), fixedC(N);
        vector<int> pairC(N, -1);
        vector<bool> fixedD1(N*2), fixedD2(N*2);
        vector<int> pairD(N*2, -1);
        vector< vector<int> > field(N, vector<int>(N, 0));
        vector< vector<bool> > output(N, vector<bool>(N, false));
        for (int i = 0; i < K; ++i) {
            char ch;
            int x, y;
            cin >> ch >> x >> y;
            --x;
            --y;
            field[x][y] = CHAR_TO_ID[(int)ch];
            if (ch == 'x' || ch == 'o') {
                fixedR[x] = true;
                fixedC[y] = true;
                ++answer;
            }
            if (ch == '+' || ch == 'o') {
                fixedD1[x+y] = true;
                fixedD2[x-y+N] = true;
                ++answer;
            }
        }

        vector<bool> was(N);
        for (int x = 0; x < N; ++x) {
            if (!fixedR[x]) {
                was.assign(N, false);
                kuhn(x, was, fixedC, pairC, [](int,int){ return true; });
            }
        }
        for (int y = 0; y < N; ++y) {
            if (pairC[y] != -1) {
                int x = pairC[y];
                assert((field[x][y] & 1) == 0);
                field[x][y] |= 1;
                output[x][y] = true;
                ++answer;
            }
        }
        for (int d1 = 0; d1 < N+N; ++d1) {
            if (!fixedD1[d1]) {
                was.assign(N+N, false);
                kuhn(d1, was, fixedD2, pairD, [N](int d1,int d2){ 
                    int x, y;
                    return convertDiag(d1, d2, N, x, y); 
                });
            }
        }
        for (int d2 = 0; d2 < N+N; ++d2) {
            if (pairD[d2] != -1) {
                int d1 = pairD[d2];
                int x, y;
                assert(convertDiag(d1, d2, N, x, y));
                assert((field[x][y] & 2) == 0);
                field[x][y] |= 2;
                output[x][y] = true;
                ++answer;
            }
        }


        vector<tuple<char, int, int>> outputList;
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                if (output[i][j]) {
                    outputList.emplace_back(ID_TO_CHAR[field[i][j]], i + 1, j + 1);
                }
            }
        }
        cout << "Case #" << __ << ": " << answer << " " << outputList.size() << "\n";
        for (const auto& out : outputList) {
            cout << get<0>(out) << " " << get<1>(out) << " " << get<2>(out) << "\n";
        }

/*        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                putchar(ID_TO_CHAR[field[i][j]]);
            }
            putchar('\n');
        }
*/
    }

    return 0;
}
