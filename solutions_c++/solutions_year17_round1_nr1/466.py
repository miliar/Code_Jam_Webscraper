#include <iostream>
#include <string>
#include <vector>

int main()
{
    int T;
    std::cin >> T;
    for (int t = 1; t <= T; ++t) {
        int R, C;
        std::cin >> R >> C;
        std::vector<std::string> matrix;

        for (int r = 0; r < R; ++r) {
            std::string row;
            std::cin >> row;
            matrix.push_back(row);
        }

        bool top_good = false;
        for (int r = 0; r < R; ++r) {
            bool left_good = false;
            for (int c = 0; c < C; ++c) {
                if (matrix[r][c] == '?') {
                    if (left_good) {
                        matrix[r][c] = matrix[r][c - 1];
                    }
                } else {
                    if (!left_good) {
                        for (int cc = 0; cc < c; ++cc) {
                            matrix[r][cc] = matrix[r][c];
                        }
                        left_good = true;
                    }
                }
            }
            if (!left_good) {
                if (top_good) {
                    matrix[r] = matrix[r - 1];
                }
            } else {
                if (!top_good) {
                    for (int rr = 0; rr < r; ++rr) {
                        matrix[rr] = matrix[r];
                    }
                    top_good = true;
                }
            }
        }

        std::cout << "Case #" << t << ":" << std::endl;
        for (int r = 0; r < R; ++r) {
            std::cout << matrix[r] << std::endl;
        }
    }
}
