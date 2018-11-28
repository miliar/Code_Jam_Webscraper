#include <iostream>
#include <string>
#include <vector>
#include <limits>

using namespace std;

int solve(int i, int k, string row, string correct) {
        if (row == correct) {
                return 0;
        }
        if (i + k > row.size()) {
                return row.size() + 1;
        }
        if (i >= (int)(row.size()) - 1)
                return row.size() + 1;

        string flip(row);
        for (int j = i; j < i + k; j++)
                flip[j] = flip[j] == '+' ? '-' : '+';

        return min(solve(i + 1, k, flip, correct) + 1, solve(i + 1, k, row, correct));

}

int main() {
        int T; cin >> T;

        for (int i = 1; i <= T; i++) {
                string row; cin >> row;
                int K; cin >> K;
                string correct(row.size(), '+');

                int flips = solve(0, K, row, correct);
                cout << "Case #" << i << ": ";
                if (flips > row.size()) {
                        cout << "IMPOSSIBLE";
                } else {
                        cout << flips;
                }
                cout << endl;
        }
}
