#include <iostream>
#include <vector>
#include <string>
#include <utility>

using namespace std;

pair<int, int> get_state(string& pancakes, int start, int end) {
    int happy = 0, sad = 0;
    for (int i = start; i < end; ++i) {
        if (pancakes[i] == '+') {
            happy++;
        }
        else {
            sad++;
        }
    }
    return{ happy, sad };
}

void flip(string& pancakes, int start, int K) {
    for (int i = start; i < start+K; ++i) {
        pancakes[i] = (pancakes[i] == '-') ? '+' : '-';
    }
}

string solve(string& pancakes, int S, int K)
{
    if (S - K < K - 1) {
        auto mid = get_state(pancakes, S - K, K);
        if (mid.first > 0 && mid.second > 0) {
            return "IMPOSSIBLE";
        }
    }
    int i = 0;
    int flip_count = 0;
    while (i < S-K+1) {
        if (pancakes[i] == '+') {
            i++;
            continue;
        }
        flip(pancakes, i++, K);
        flip_count++;
    }
    auto state = get_state(pancakes, 0, S);
    return state.second == 0 ? to_string(flip_count) : "IMPOSSIBLE";
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        int S, K;
        string pancakes;
        cin >> pancakes;
        cin >> K;
        S = (int)pancakes.size();

        cout << "Case #" << t << ": ";
        cout << solve(pancakes, S, K);
        cout << endl;
    }
}