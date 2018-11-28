#include <bits/stdc++.h>

#define D(a)
using namespace std;

void update_LR(vector<int> &state, vector<int64_t> &L, vector <int64_t> &R, int64_t choice) {
    D(cout << "Chosen one," << choice << ", now updating for next guy" << endl;)
    // calculate between which "1"s is this choice
    int64_t pre_1, post_1;

    for (int64_t i = choice + 1; i < state.size(); i++) {
        if (state[i] == 1) {
            post_1 = i;
            break;
        }
    }

    for (int64_t i = choice - 1; i >= 0; i--) {
        if (state[i] == 1) {
            pre_1 = i;
            break;
        }
    }

    // update L and R for numbers between pre_1 to choice
    for (int64_t i = pre_1 + 1; i < choice; i++) {
        L[i] = i - (pre_1 + 1);
        R[i] = (choice - 1) - i;
    }

    // update L and R for numbers between choice to post_1
    for (int64_t i = choice + 1; i < post_1; i++) {
        L[i] = i - (choice + 1);
        R[i] = (post_1 - 1) - i;
    }
}

void choose_toilet(vector<int> &state, vector<int64_t> &L, vector<int64_t> &R, int64_t& y, int64_t &z) {
    D(cout << "Choosing toilet" << endl;)

    int64_t n = state.size() - 2;
    vector<int64_t> LR_min(n+2, -1), LR_max(n+2, -1);

    for (int i = 1; i <= n; ++i) {
        LR_min[i] = min(L[i], R[i]);
        LR_max[i] = max(L[i], R[i]);
    }

    int64_t curr = -1, tmp;
    vector<int64_t> max_minLR;

    for (int64_t i = 1; i <= n; ++i) {
        tmp = LR_min[i];

        if (tmp >= curr) {
            if (tmp > curr) {
                max_minLR.clear();
            }

            curr = tmp;
            max_minLR.push_back(i);
        }
    }

    curr = -1;
    int64_t choice;

    for (int64_t i = 0; i < max_minLR.size(); i++) {
        tmp = LR_max[max_minLR[i]];

        if (tmp > curr) {
            curr = tmp;
            choice = max_minLR[i];
        }
    }

    state[choice] = 1;
    L[choice] = -1;
    R[choice] = -1;
    update_LR(state, L, R, choice);
    y = LR_max[choice];
    z = LR_min[choice];
}




int main() {
    int t;
    cin >> t;

    for (int i = 1; i <= t; ++i) {
        // scan input
        int64_t n, k;
        cin >> n;
        cin >> k;
        // process input
        vector<int> state(n + 2, 0);
        vector<int64_t> L(n + 2, -1), R(n + 2, -1);
        state[0] = 1;
        state[n + 1] = 1;

        for (int64_t j = 1; j <= n; j++) {
            L[j] = j - 1;
            R[j] = n - j;
        }

        int64_t y, z;

        for (int64_t j = 0; j < k; j++) {
            choose_toilet(state, L, R, y, z);
        }

        // print answer
        cout << "Case #" << i << ": " << y << " "  << z << endl;
    }

    return 0;
}

