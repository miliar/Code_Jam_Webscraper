#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

template<class T>
inline T read() {
    T value;
    std::cin >> value;
    return value;
}

int main() {
    auto T = read<int>();
    for (int caseNum = 1; caseNum <= T; ++caseNum) {
        auto R = read<int>();
        auto C = read<int>();
        bool filled = false;
        std::vector<std::string> rows;
        for (int i = 0; i < R; ++i) {
            auto row = read<std::string>();
            char last = '?';
            char first = '?';
            for (int j = 0; j < C; ++j) {
                if (row[j] == '?') {
                    row[j] = last;
                } else {
                    last = row[j];
                    if (first == '?') {
                        first = last;
                        for (int k = 0; k < j; ++k) {
                            // fill everything to the left
                            row[k] = first;
                        }
                    }
                }
            }
            if (first == '?') {
                // this row is totally empty
                if (filled) {
                    // fill with the previous row
                    for (int j = 0; j < C; ++j) {
                        row[j] = rows.back()[j];
                    }
                }
            } else {
                // this row is not empty
                if (!filled) {
                    // fill all previous rows
                    for (auto& prev : rows) {
                        for (int j = 0; j < C; ++j) {
                            prev[j] = row[j];
                        }
                    }
                    filled = true;
                }
            }
            rows.push_back(row);
        }
        printf("Case #%d:\n", caseNum);
        for (auto& row : rows) {
            printf("%s\n", row.c_str());
        }
    }
    return 0;
}
