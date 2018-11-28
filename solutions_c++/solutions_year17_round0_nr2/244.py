#include <iostream>
#include <string>
#include <set>

using namespace std;

void gen(const string& prefix, const string& input, size_t pos, set<string>& output) {
    if (pos == input.length()) {
        output.insert(prefix);
        return;
    }
    if (input[pos] >= prefix.back()) {
        gen(prefix + input[pos], input, pos + 1, output);
    }
    if (input[pos] > '0' && (input[pos] - 1) >= prefix.back()) {
        const string candidate = prefix + char(input[pos] - 1) + string(input.length() - pos - 1, '9');
        output.insert(candidate);
    }
}

int main() {
    int num_cases;
    cin >> num_cases;
    for (int case_index = 1; case_index <= num_cases; ++case_index) {
        string input;
        cin >> input;
        set<string> feasible;
        // Add all feasible solutions, then pick the biggest one, and trip all leading zeroes.
        gen("0", input, 0, feasible);
        string answer = *feasible.rbegin();
        // Trip all leading zeroes.
        size_t pos = 0;
        while (answer[pos] == '0') ++pos;
        cout << "Case #" << case_index << ": " << answer.substr(pos) << endl;
    }
    return 0;
}
