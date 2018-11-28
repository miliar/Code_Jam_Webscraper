#include <iostream>
#include <string>
#include <algorithm>
using namespace std;


string prettify(int n) {
    if (n < 0) return "IMPOSSIBLE";
    return to_string(n);

}


void flip(vector<bool>& panState, int start, int end) {
    while (start < end) {
        panState[start] = !panState[start];
        ++start;
    }
}


int findMinNumFlips(const string& pan, int flipperLength) {
    vector<bool> panState(pan.size());
    for (size_t i = 0; i < pan.size(); ++i) panState[i] = pan[i] == '+';
    int result = 0;
    for (size_t i = 0; i + flipperLength <= panState.size(); ++i) {
        if (panState[i] == 0) {
            ++result;
            flip(panState, i, i + flipperLength);
        }
    }
    if (!all_of(panState.begin(), panState.end(), [](bool state) {return state; })) result = -1;
    return result;
}

int main() {
    ios_base::sync_with_stdio(false);
    int numTests;
    cin >> numTests;
    for (int testId = 0; testId < numTests; ++testId) {
        string pan;
        int flipperLength;
        cin >> pan >> flipperLength;
        cout << "Case #" << testId + 1 << ": " << prettify(findMinNumFlips(pan, flipperLength)) << endl;
    }
    return 0;
}
