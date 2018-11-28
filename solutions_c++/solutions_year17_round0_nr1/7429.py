#include <cmath>
#include <cstring>
#include <iostream>
#include <queue>
#include <string>
#include <unordered_set>
#include <valarray>

using namespace std;

string vp(valarray<bool> *v) {
    string s;
    for (bool *it = begin(*v); it != end(*v); ++it) {
        if (*it) {
            s += "+";
        } else {
            s += "-";
        }
    }
    return s;
}

bool invb(bool a) { return !a; }
void invr(valarray<bool> *a, int start, int size) {
    transform(begin(*a) + start, begin(*a) + start + size, begin(*a) + start,
    invb);
}

struct State {
    int steps;
    valarray<bool> state;
};

int main(void) {
    int t;
    cin >> t;
    for (int c = 1; c <= t; c++) {
        string s;
        int k;
        cin >> s;
        cin >> k;
        int l = s.size();

        State state;
        state.steps = 0;
        state.state = valarray<bool>(l);
        for (int c = 0; c < l; c++) {
            state.state[c] = s[c] == '+';
        }

        for (int i = 0; i < l - k + 1; i++) {
            if (!state.state[i]) {
                invr(&state.state, i, k);
                state.steps++;
            }
        }

        cout << "Case #" << c << ": ";
        if (state.state.min()) {
            cout << state.steps;
        } else {
            cout << "IMPOSSIBLE";
        }
        cout << endl;
    }
    return 0;
}
