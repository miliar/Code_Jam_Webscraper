#include <iostream>
#include <string>
#include <vector>

void printMatrix(std::vector<std::string>& matrix) {
    int r = matrix.size();
    int c = matrix[0].size();

    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            // std::cerr << matrix[i][j];
        }
        // std::cerr << std::endl;
    }
}

bool emptyRow(std::vector<std::string>& matrix, int row, int startCol, int endCol) {
    for (int i = startCol; i < endCol; ++i) {
        if (matrix[row][i] != '?') {
            return false;
        }
    }

    return true;
}

void fillRow(std::vector<std::string>& matrix, int row, int startCol, int endCol, char el) {
    for (int i = startCol; i < endCol; ++i) {
        if (matrix[row][i] == '?') {
            matrix[row][i] = el;
        }
    }
}

void handle(std::vector<std::string>& matrix, int elR, int elC) {
    int r = matrix.size();
    int c = matrix[0].size();

    const auto el = matrix[elR][elC];
    // std::cerr << "Handling --- " << el << std::endl;


    int i;
    int firstCol = elC;
    int lastCol = elC + 1;

    for (i = elC + 1; i < c; ++i) {
        if (matrix[elR][i] == '?') {
            lastCol = i + 1;
            matrix[elR][i] = el;
        } else {
            break;
        }
    }

    for (i = elC - 1; i >= 0; --i) {
        if (matrix[elR][i] == '?') {
            firstCol = i;

            matrix[elR][i] = el;
        } else {
            break;
        }
    }

    // // std::cerr << "first = " << firstCol << " " << "last = " << lastCol << std::endl;
    // std::cerr << std::endl;


    for (i = elR + 1; i < r; ++i) {
        // std::cerr << "Checking row " << i << std::endl;;

        if (emptyRow(matrix, i, firstCol, lastCol)) {
            // std::cerr << "   fill" << std::endl;
            fillRow(matrix, i, firstCol, lastCol, el);
        } else {
            // std::cerr << "   no" << std::endl;
            break;
        }
    }

    for (i = elR - 1; i >= 0; --i) {
        if (emptyRow(matrix, i, firstCol, lastCol)) {
            fillRow(matrix, i, firstCol, lastCol, el);
        } else {
            break;
        }
    }
}

void solve(std::vector<std::string>& matrix) {
    int r = matrix.size();
    int c = matrix[0].size();
    bool handled[30] = {};

    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            // // std::cerr << i << " " << j << std::endl;

            if (matrix[i][j] != '?' && (!handled[matrix[i][j] - 'A'])) {
                handle(matrix, i, j);
                handled[matrix[i][j] - 'A'] = true;

                printMatrix(matrix);

            }
        }
    }

    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            if (matrix[i][j] == '?') {
                throw "fail";
            }

            std::cout << matrix[i][j];
        }
        std::cout << std::endl;
    }
}

int main() {
    int tt = 0;
    std::cin >> tt;

    for (int tc = 1; tc <= tt; ++tc) {
        int r, c;
        std::cin >> r >> c;
        std::vector<std::string> matrix;
        for (int i = 0; i < r; ++i) {
            std::string row;
            std::cin >> row;
            matrix.emplace_back(std::move(row));
        }

        std::cout << "Case #" << tc << ":" << std::endl;
        solve(matrix);
    }

    return 0;
}
