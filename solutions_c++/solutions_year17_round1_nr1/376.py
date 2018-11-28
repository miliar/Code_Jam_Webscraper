#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    int num_cases;
    cin >> num_cases;
    for (int case_index = 1; case_index <= num_cases; ++case_index) {
        int R, C;
        cin >> R >> C;
        vector<string> input(R);
        vector<int> num_non_question(R, 0);
        for (int r = 0; r < R; ++r) {
            cin >> input[r];
            for (char ch : input[r]) {
                if (ch != '?') ++num_non_question[r];
            }
        }
        for (int r = 0; r < R; ++r) {
            if (num_non_question[r] == 0) continue;
            int index = 0;
            char ch;
            while (index < C && (ch = input[r][index++]) == '?');
            for (int c = 0; c < index; ++c) input[r][c] = ch;
            for (; index < C; ++index) {
                if (input[r][index] == '?') input[r][index] = ch;
                else ch = input[r][index];
            }
        }
        int last_known = 0;
        while (num_non_question[last_known] == 0) ++last_known;
        int r_index = 0;
        for (; r_index < last_known; ++r_index) {
            input[r_index] = input[last_known];
        }
        for (r_index = last_known + 1; r_index < R; ++r_index) {
            if (num_non_question[r_index] == 0) {
                input[r_index] = input[last_known];
            } else {
                last_known = r_index;
            }
        }
        cout << "Case #" << case_index << ":" << endl;
        for (auto s : input) cout << s << endl;
    }
    return 0;
}
