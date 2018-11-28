#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

typedef uint64_t my_int;

string all_nines(int L) {
    string s = "";
    for (int i = 0; i < L; i++) {
        s += "9";
    }

    return s;
}

string solve(my_int N) {
    string S = to_string(N);
    int L = S.size();

    // check non-decreasing property
    bool prop = true;
    int violation_position = -1;
    for (int i = 0; i < L-1; i++) {
        int cur = S[i] - '0';
        int next = S[i+1] - '0';

        if (next < cur) {
            prop = false;
            violation_position = i;
            break;
        }
    }

    // property holds for input number
    if (prop) {
        return S;
    }

    // back propagate
    int last_violation = violation_position;
    for (int i = violation_position; i >= 0; i--) {
        if (S[i+1] < S[i]) {
            S[i] = S[i] - 1;
            last_violation = i;
        }
    }

    if (S[0] == '0') {
        return all_nines(L-1);
    }
    else {
        for (int i = last_violation + 1; i < L; i++) {
            S[i] = '9';
        }
        return S;
    }
}

bool non_decreasing(my_int N) {
    string S = to_string(N);
    int L = S.size();

    for (int i = 0; i < L-1; i++) {
        if (S[i+1] < S[i]) {
            return false;
        }
    }

    return true;
}

string count_backwards(my_int N) {
    for (int i = N; i >= 1; i--) {
        if (non_decreasing(i)) {
            return to_string(i);
        }
    }

    return "error";
}

int main() {
    int T;

    cin >> T;

    for (int c = 1; c <= T; c++) {
        my_int N;
        cin >> N;

        string res = solve(N);
        
        /*
        string res2 = count_backwards(N);

        if (res != res2) {
            printf("For N = %llu, got %s and %s\n", N, res.c_str(), res2.c_str());
        }
        */

        printf("Case #%d: %s\n", c, res.c_str());
    }

    return 0;
}