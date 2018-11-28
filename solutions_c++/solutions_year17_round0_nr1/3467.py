#include <iostream>
#include <c++/vector>
#include <c++/fstream>

using namespace std;

// -+-+-+--- 3   0-3
// +-++-+---     3-4
// ++---+---     4-5
// ++++++---
// +++++++++

struct solve {
    int flips = 0;
    vector<int> inversions;
    solve(const string& pancakes, const int k) {
        bool in_flip;
        bool face_down = false;
        inversions.resize(pancakes.size() + k + 1);
        int ic = 0;
        for (int i = 0; i < pancakes.size(); ++i) {
            const char c = pancakes[i];
            ic += inversions[i];
            in_flip = (ic % 2) != 0;
            face_down = in_flip ? (c == '+') : (c == '-');
            if (i > pancakes.size() - k) {
                if (face_down) {
                    break;
                }
                continue;
            }
            if (face_down) {
                ++flips;
                inversions[i + 1] += 1;
                inversions[i + k] -= 1;
            }
        }
        if (pancakes.empty()) {
            answer = "0";
            return;
        }
        if (face_down) {
            answer = "IMPOSSIBLE";
        } else {
            answer = to_string(flips);
        }

    }
    string answer = "blah";
};

int main() {

    ofstream ofs;
    ifstream ifs;

    ifs.open("in.txt");
    ofs.open("out.txt", ofstream::out | ofstream::app);

    string block;
    size_t T; // size of input

    ifs >> T;

    int _case = 1;

    while (ifs >> block) {
        int k;
        ifs >> k;

        solve solution(block, k);

        ofs << "Case #" << _case++ << ": " << solution.answer << endl;
    }

    return 0;
}