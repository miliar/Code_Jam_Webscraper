//
// Created by XelaPi.
//
#include <iostream>
#include <map>
#include <vector>

using namespace std;

map<vector<int>, int> possibilites;

int search(vector<int> state) {
    auto previous = possibilites.find(state);

    if (previous == possibilites.end()) {
        possibilites[state] = INT_MAX;

        if (state[2] <= 0) {
            possibilites[state] = 0;
            return 0;
        }

        if (state[0] <= 0) {
            return INT_MAX;
        }

        int best = INT_MAX;

        // We attack
        vector<int> attackVector = state;
        attackVector[2] -= attackVector[1];
        attackVector[0] -= attackVector[3];
        best = min(best, search(attackVector));

        if (best == INT_MAX || best > 0) {
            vector<int> buffVector = state;
            buffVector[1] += buffVector[4];
            buffVector[0] -= buffVector[3];
            best = min(best, search(buffVector));

            vector<int> cureVector = state;
            cureVector[0] = cureVector[6];
            cureVector[0] -= cureVector[3];
            best = min(best, search(cureVector));

            vector<int> debuffVector = state;
            debuffVector[3] -= debuffVector[5];
            if (debuffVector[3] < 0) {
                debuffVector[3] = 0;
            }
            debuffVector[0] -= debuffVector[3];
            best = min(best, search(debuffVector));
        }

        if (best == INT_MAX) {
            return INT_MAX;
        } else {
            possibilites[state] = 1 + best;
            return 1 + best;
        }

    } else {
        return previous->second;
    }
}

int main() {

    int num;

    cin >> num;

    for (int i = 0; i < num; i++) {
        cout << "Case #" << (i + 1) << ": ";

        int Hd, Ad, Hk, Ak, B, D;

        cin >> Hd >> Ad >> Hk >> Ak >> B >> D;

        vector<int> initState = {Hd, Ad, Hk, Ak, B, D, Hd};

        int minimum = search(initState);

        if (minimum == INT_MAX) {
            cout << "IMPOSSIBLE";
        } else {
            cout << minimum;
        }

        cout << endl;
    }

    return 0;
}