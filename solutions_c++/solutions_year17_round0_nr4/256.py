#include <iostream>
#include <string>
#include <vector>

using namespace std;

char symbols[4] = { '.', '+', 'x', 'o' };

char board[128][128];
char ans[128][128];
bool rows[128];
bool cols[128];

// Matching arrays.
// There are two dimensions: r + c and r - c.
// We will use plus and minus to name them.

bool matchedPlus[256];
bool matchedMinus[256];

struct Matcher {
    int N;
    vector<int> left;
    vector<int> right;
    vector<vector<bool>> adjacency;

    Matcher(int NN) : N(NN) {
        // Only those that are not matched can be considered.
        int maxV = 2 * N - 1;
        for (int i = 0; i < maxV; ++i) {
            if (!matchedPlus[i]) left.push_back(i);
            if (!matchedMinus[i]) right.push_back(i);
        }
        // cerr << left.size() << '\t' << right.size() << endl;
        // We only have a bunch of left and right.
        // Not all of them are intersectable.
        adjacency.resize(left.size(), vector<bool>(right.size(), false));
        for (size_t l = 0; l < left.size(); ++l) {
            for (size_t r = 0; r < right.size(); ++r) {
                const int sum = left[l], diff = right[r] - N + 1;
                if ((sum + diff) & 1) {
                    continue; // They must be of the same parity.
                }
                if (sum + diff < 0 || sum + diff >= 2 * N ||
                    sum - diff < 0 || sum - diff >= 2 * N) {
                    continue;
                }
                adjacency[l][r] = true;
            }
        }
        /*
        for (int r = 0; r < right.size(); ++r) {
            cerr << ' ' << (right[r] - N + 1);
        }
        cerr << endl;
        for (int l = 0; l < left.size(); ++l) {
            cerr << left[l];
            for (int r = 0; r < right.size(); ++r) {
                cerr << ' ' << adjacency[l][r];
            }
            cerr << endl;
        }
        */
    }

    vector<int> matchedL;
    vector<int> matchedR;
    vector<int> visitedL;
    int phase;

    bool dfs(int l) {
        if (visitedL[l] >= phase) {
            return false;
        }
        visitedL[l] = phase;
        for (int r = 0; r < matchedR.size(); ++r) {
            if (!adjacency[l][r]) {
                continue;
            }
            if (matchedR[r] == -1 || dfs(matchedR[r])) {
                // A match!
                matchedL[l] = r;
                matchedR[r] = l;
                return true;
            }
        }
        return false;
    }

    int match() {
        matchedL.resize(left.size(), -1);
        matchedR.resize(right.size(), -1);
        visitedL.resize(left.size(), -1);
        int ret = 0;
        for (int l = 0; l < left.size(); ++l) {
            phase = l;
            if (dfs(l)) {
                ++ret;
            }
        }
        for (int l = 0; l < left.size(); ++l) {
            if (matchedL[l] != -1) {
                const int sum = left[l], diff = right[matchedL[l]] - N + 1;
                const int r = (sum + diff) / 2, c = (sum - diff) / 2;
                ans[r][c] |= 1;
            }
        }
        return ret;
    }
};

int main() {
    int num_cases;
    cin >> num_cases;
    for (int case_index = 1; case_index <= num_cases; ++case_index) {
        // The problem is a combination of the n-rook and n-bishop problem.
        // The 'x' are rooks. They cannot be placed in the same row / column.
        // The '+' are bishops. They cannot be placed along the same diagonal.
        // If we ever place a '+' and an 'x' together, we "upgrade" it to an 'o'.
        // The question is how we can maximize the '+' and 'x' there.
        // The n-rook problem is trivial.
        // Only the n-bishop problem is hard here.
        // The n-bishop problem is essentially filling up the diagonal space:
        //      .
        //     . .
        //    . . .
        //   . . . .
        //  . . . . .
        // . . . . . .
        //  . . . . .
        //   . . . .
        //    . . .
        //     . .
        //      .
        // Here, we can use a matching algorithm to find the optimal solution.

        int N, M;
        cin >> N >> M;
        char ch;
        int r, c;
        if (N == 1) {
            ch = '\0';
            if (M == 1) {
                cin >> ch >> r >> c;
            }
            int num_steps = (ch != 'o') ? 1 : 0;
            cout << "Case #" << case_index << ": 2 " << num_steps << endl;
            if (num_steps) {
                cout << "o 1 1" << endl;
            }
        } else {
            // Now this can get interesting.
            memset(board, 0, sizeof(board));
            memset(ans, 0, sizeof(ans));
            memset(rows, 0, sizeof(rows));
            memset(cols, 0, sizeof(cols));

            memset(matchedPlus, 0, sizeof(matchedPlus));
            memset(matchedMinus, 0, sizeof(matchedMinus));

            int init_score = 0;
            for (int i = 0; i < M; ++i) {
                cin >> ch >> r >> c;
                --r; --c;
                if (ch != 'x') {  // This is a '+'.
                    board[r][c] |= 1;
                    ans[r][c] |= 1;
                    ++init_score;
                    const int plusCoor = r + c;
                    const int minusCoor = r - c + N - 1;
                    matchedPlus[plusCoor] = true;
                    matchedMinus[minusCoor] = true;
                }
                if (ch != '+') { // This is an 'x'.
                    board[r][c] |= 2;
                    ans[r][c] |= 2;
                    rows[r] = true;
                    cols[c] = true;
                    ++init_score;
                }
            }
            /*
            cerr << "Initial Score = " << init_score << endl;
            for (int rr = 0; rr < N; ++rr) {
                for (int cc = 0; cc < N; ++cc) {
                    cerr << symbols[ans[rr][cc]];
                }
                cerr << endl;
            }
            */
            int final_score = init_score;
            // Fill in the 'x' now.
            int rr = 0, cc = 0;
            for (rr = 0; rr < N; ++rr) {
                if (rows[rr]) continue;
                while (cols[cc]) ++cc;
                ans[rr][cc++] |= 2;
                ++final_score;
            }
            /*
            cerr << "After putting 'x': " << final_score << endl;
            for (rr = 0; rr < N; ++rr) {
                for (cc = 0; cc < N; ++cc) {
                    cerr << symbols[ans[rr][cc]];
                }
                cerr << endl;
            }
            */
            // We are done with the 'x'.
            // Now solve the n-bishop problems.
            final_score += Matcher(N).match();
            // cerr << "After matching: " << final_score << endl;

            // Now compute the diff.
            int num_diffs = 0;
            for (rr = 0; rr < N; ++rr) {
                for (cc = 0; cc < N; ++cc) {
                    if (ans[rr][cc] != board[rr][cc]) ++num_diffs;
                }
            }

            cout << "Case #" << case_index << ": " << final_score << " " << num_diffs << endl;
            for (rr = 0; rr < N; ++rr) {
                for (cc = 0; cc < N; ++cc) {
                    if (ans[rr][cc] != board[rr][cc]) {
                        cout << symbols[ans[rr][cc]] << ' ' << (rr + 1) << ' ' << (cc + 1) << endl;
                    }
                }
            }
        }
    }
    return 0;
}
