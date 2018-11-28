#include <vector>
#include <iostream>

using namespace std;

int main() {
    int T, K;


    cin >> T;
    for (int t = 0; t < T; ++t) {
        vector<int> turned;
        string s;
        cin >> s;
        cin >> K;
        bool start = s[0] == '+';
        bool prev = start;
        if (!start) {
            turned.push_back(0);
        }
        for (int i = 1; i < s.size(); ++i) {
            const bool current = s[i] == '+';
            if (current != prev) {
                turned.push_back(i);
                prev = current;
            }
        }
        vector<int> flip;
        vector<int> introduced_turns;
        bool impossible = false;
        
        {   int i = 0;
            int j = 0;
            while (i < turned.size() || j < introduced_turns.size()) {
                int turn = -1;
                if (i < turned.size() && j < introduced_turns.size()) {
                    if (turned[i] == introduced_turns[j]) {
                        ++i;
                        ++j;
                        continue;
                    }
                    if (turned[i] < introduced_turns[j]) {
                        turn = turned[i];
                        ++i;
                    } else {
                        turn = introduced_turns[j];
                        ++j;
                    }
                } else {
                    if (i < turned.size()) {
                        turn = turned[i];
                        ++i;
                    } else {
                        turn = introduced_turns[j];
                        ++j;
                    }
                }
                if (turn + K > s.size()) {
                    impossible = true;
                } else {
                    flip.push_back(turn);
                    if (turn + K < s.size()) {
                        introduced_turns.push_back(turn + K);
                    }
                }
        }   }
        cout << "Case #" << t+1 << ": ";
        if (impossible) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            cout << flip.size() << endl;
        }
    }
    return 0;
}

