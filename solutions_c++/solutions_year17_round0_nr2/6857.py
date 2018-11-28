#include <bits/stdc++.h>

using namespace std;

int digits[20];
string solution;

bool DFS(int pos, int pre, bool limit) {
    if (pos == -1)
        return true;

    int end = limit ? digits[pos] : 9;
    for (int i = end; i >= pre; i--) {
        solution.push_back(i + '0');
        if (DFS(pos - 1, i, limit && i == end))
            return true;
        solution.pop_back();
    }
    return false;
}

string solve(string N) {
    solution.clear();
    for (int i = 0; i < N.size(); i++)
        digits[i] = N[N.size() - 1 - i] - '0';
    DFS(N.size() - 1, 0, true);
    while (solution[0] == '0')
        solution = solution.substr(1);
    return solution;
}

int main() {
    int T;
    cin >> T;
    for (int tc = 0; tc < T; tc++) {
        string N;
        cin >> N;
        cout << "Case #" << tc + 1 << ": " << solve(N) << "\n";
    }
}
