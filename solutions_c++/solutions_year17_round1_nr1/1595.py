#include <iostream>
#include <c++/vector>
#include <c++/fstream>
#include <c++/cmath>
#include <c++/algorithm>
#include <functional>

using namespace std;

struct Solve {
    Solve(vector<string>& data) {

        // if each row has a letter, we're ok.
        // if missing a row, replicate the row above it?

        vector<int> empty_row_indices;
        int last_good_row = -1;

        for (int r = 0; r < data.size(); ++r) {
            string& row = data[r];
            bool empty = fill_row(row);
            if (empty) {
                empty_row_indices.push_back(r);
            } else {
                last_good_row = r;
                for (auto er : empty_row_indices) {
                    data[er] = row;
                }
                empty_row_indices.clear();
            }
        }

        if (last_good_row != -1) {
            for (auto er : empty_row_indices) {
                data[er] = data[last_good_row];
            }
        }

        for (int i = 0; i < data.size() - 1; ++i) {
            auto& row = data[i];
            answer += row + "\n";
        }
        answer += data.back();
    }

    // ret: if row is empty
    bool fill_row(string& rs) {
        char last = '?';
        for (int c = 0; c < rs.size(); ++c) {
            char initial = rs[c];
            if (last == '?' && initial == '?') {
                continue;
            } else if (last == '?') {
                // sweep back
                for (int i = c - 1; i > -1; --i) {
                    rs[i] = initial;
                }
            } else if (initial == '?') {
                rs[c] = last;
            }
            if (initial != '?') {
                last = initial;
            }
        }
        return last == '?';
    }

    string answer = "\n";
};

int main() {

    ofstream ofs;
    ifstream ifs;

    ifs.open("in.txt");
    ofs.open("out.txt", ofstream::out | ofstream::app);


    size_t T; // size of input

    ifs >> T;

    int _case = 1;

    string line;
    int R;
    int C;

    while (T-- > 0) {
        ifs >> R;
        ifs >> C;

        vector<string> data;

        while (R--) {
            ifs >> line;
            data.emplace_back(line);
        }

        Solve solution(data);

        ofs << "Case #" << _case++ << ": " << solution.answer << endl;
    }

    return 0;
}