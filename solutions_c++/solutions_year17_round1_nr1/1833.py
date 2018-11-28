#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<string> split(vector<string> matrix) {
    vector<string> result;
    for (string& row : matrix) {
        string new_row = "";
        int begin = 0, end = 0;
        while (end < matrix[0].size()) {
            if (isalpha(row[end])) {
                for (int i = begin; i <= end; ++i) new_row.push_back(row[end]);
                begin = end + 1;
                end = begin;
            } else {
                ++end;
            }
        }

        if (new_row.empty() && !result.empty()) new_row = result.back();
        if (!new_row.empty()) {
            const char c = new_row.back();
            const int size = new_row.size();
            for (int i = 0; i < matrix[0].size() - size; ++i) new_row.push_back(c);
        }

        result.push_back(new_row);
    }
    // for (int i = 0; i < result.size() - 1; ++i)
    //     if (result[i].empty()) result[i] = result[i + 1];
    for (int i = result.size() - 1; i >= 0; --i)
        if (result[i].empty()) result[i] = result[i + 1];

    return result;
}

int main() {
    int T, id = 1;
    int R, C;
    cin >> T;
    while (T--) {
        cout << "Case #" << id << ": " << endl;
        cin >> R >> C;
        id++;
        vector<string> matrix;
        while (R > 0) {
            string row;
            cin >> row;
            matrix.push_back(row);
            --R;
        }

        vector<string> result = split(matrix);
        for (auto & str : result) cout << str << endl;
    }

    return 0;
}