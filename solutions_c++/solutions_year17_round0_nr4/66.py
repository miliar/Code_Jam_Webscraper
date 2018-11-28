#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <random>
#include <queue>

template<class T>
inline T read() {
    T value;
    std::cin >> value;
    return value;
}

struct PendingCell {
    int cost;
    int row;
    int col;

    PendingCell(int cost, int row, int col) : cost(cost), row(row), col(col) {}

    friend bool operator<(const PendingCell& a, const PendingCell& b) {
        return b.cost < a.cost;
    }
};

class Grid {
    int N;
    std::vector<bool> x_sets;
    std::vector<bool> p_sets;

    std::vector<bool> x_rows;
    std::vector<bool> x_cols;
    std::vector<bool> p_sums;
    std::vector<bool> p_diffs;

    std::vector<int> x_rows_free;
    std::vector<int> x_cols_free;
    std::vector<int> p_sums_free;
    std::vector<int> p_diffs_free;

public:
    std::priority_queue<PendingCell> x_queue;
    std::priority_queue<PendingCell> p_queue;

    Grid(int N)
      : N(N)
      , x_sets(N * N)
      , p_sets(N * N)
      , x_rows(N)
      , x_cols(N)
      , p_sums(N * 2)
      , p_diffs(N * 2)
      , x_rows_free(N, N)
      , x_cols_free(N, N)
      , p_sums_free(N * 2)
      , p_diffs_free(N * 2)
    {
        for (int sum = 0; sum < N * 2; ++sum) {
            p_sums_free[sum] = N - std::abs(N - 1 - sum);
        }
        for (int diff = 0; diff < N * 2; ++diff) {
            p_diffs_free[diff] = N - std::abs(diff - N);
        }
        for (int row = 0; row < N; ++row) {
            for (int col = 0; col < N; ++col) {
                int x_cost = x_rows_free[row] + x_cols_free[col] - 1;
                x_queue.push(PendingCell(x_cost, row, col));
                int p_cost = p_sums_free[row + col] + p_diffs_free[N + row - col] - 1;
                p_queue.push(PendingCell(p_cost, row, col));
            }
        }
    }

    bool has_x(int row, int col) const {
        return x_sets[row * N + col];
    }

    bool has_p(int row, int col) const {
        return p_sets[row * N + col];
    }

    bool x_row(int row) const {
        return x_rows[row];
    }

    bool x_col(int col) const {
        return x_cols[col];
    }

    bool can_x(int row, int col) const {
        return !has_x(row, col) && !x_row(row) && !x_col(col);
    }

    bool p_sum(int sum) const {
        return p_sums[sum];
    }

    bool p_diff(int diff) const {
        return p_diffs[N + diff];
    }

    bool can_p(int row, int col) const {
        return !has_p(row, col) && !p_sum(row + col) && !p_diff(row - col);
    }

    char get(int row, int col) const {
        if (has_x(row, col)) {
            if (has_p(row, col)) {
                return 'o';
            } else {
                return 'x';
            }
        } else {
            if (has_p(row, col)) {
                return '+';
            } else {
                return '.';
            }
        }
    }

    void set_x(int row, int col) {
        x_sets[row * N + col] = true;
        // rows/cols are now fully occupied
        x_rows[row] = true;
        x_cols[col] = true;
        x_rows_free[row] = 0;
        x_cols_free[col] = 0;
    }

    void set_p(int row, int col) {
        p_sets[row * N + col] = true;
        // diagonals are now fully occupied
        p_sums[row + col] = true;
        p_diffs[N + row - col] = true;
        p_sums_free[row + col] = 0;
        p_diffs_free[N + row - col] = 0;
    }

    int x_cost(int row, int col) {
        return x_rows_free[row] + x_cols_free[col] - 1;
    }

    int p_cost(int row, int col) {
        return p_sums_free[row + col] + p_diffs_free[N + row - col] - 1;
    }
};

struct RowCol {
    int row;
    int col;

    RowCol(int row, int col) : row(row), col(col) {}
};

struct Change {
    char ch;
    int row;
    int col;

    Change(char ch, int row, int col) : ch(ch), row(row), col(col) {}
};

int main() {
    int T = read<int>();
    for (int caseNum = 1; caseNum <= T; ++caseNum) {
        int N = read<int>();
        int M = read<int>();
        Grid G(N);
        int style = 0;
        for (int i = 0; i < M; ++i) {
            std::string s = read<std::string>();
            char ch = s[0];
            int row = read<int>() - 1;
            int col = read<int>() - 1;
            switch (ch) {
                case 'o':
                    G.set_x(row, col);
                    G.set_p(row, col);
                    style += 2;
                    break;
                case 'x':
                    G.set_x(row, col);
                    style += 1;
                    break;
                case '+':
                    G.set_p(row, col);
                    style += 1;
                    break;
            }
        }

        // std::vector<bool> changed(N * N);
        // while (!G.x_queue.empty()) {
        //     auto& top = G.x_queue.top();
        //     if (!G.can_x(top.row, top.col)) {
        //         G.x_queue.pop();
        //         continue;
        //     }
        //     G.set_x(top.row, top.col);
        //     style += 1;
        //     changed[top.row * N + top.col] = true;
        // }
        // while (!G.p_queue.empty()) {
        //     auto& top = G.p_queue.top();
        //     if (!G.can_p(top.row, top.col)) {
        //         G.p_queue.pop();
        //         continue;
        //     }
        //     G.set_p(top.row, top.col);
        //     changed[top.row * N + top.col] = true;
        //     style += 1;
        // }

        // std::vector<Change> changes;
        // for (int row = 0; row < N; ++row) {
        //     for (int col = 0; col < N; ++col) {
        //         if (changed[row * N + col]) {
        //             changes.emplace_back(G.get(row, col), row, col);
        //         }
        //     }
        // }

        std::vector<Change> changes;
        while (!G.p_queue.empty()) {
            auto top = G.p_queue.top();
            G.p_queue.pop();
            bool changed = false;
            if (G.can_x(top.row, top.col)) {
                G.set_x(top.row, top.col);
                changed = true;
                ++style;
            }
            if (G.can_p(top.row, top.col)) {
                G.set_p(top.row, top.col);
                changed = true;
                ++style;
            }
            if (changed) {
                changes.emplace_back(G.get(top.row, top.col), top.row, top.col);
            }
        }

        // for (int row = 0; row < N; ++row) {
        //     for (int col = 0; col < N; ++col) {
        //         std::cerr << ' ' << G.get(row, col);
        //     }
        //     std::cerr << std::endl;
        // }
        // std::cerr << "new style: " << style << std::endl;

        printf("Case #%d: %d %lu\n", caseNum, style, changes.size());
        for (auto& change : changes) {
            printf("%c %d %d\n", change.ch, change.row + 1, change.col + 1);
        }
    }
    return 0;
}
