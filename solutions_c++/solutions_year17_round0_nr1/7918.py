//#include<iostream>
//#include<unordered_map>
//#include<unordered_set>
//#include<map>
//#include<set>
#include<vector>
//#include<queue>
#include<list>
#include<string>
//#include<numeric>
//#include<algorithm>
using namespace std;

#include"debug.h"
using namespace mylib;

#include"data.h"
#include"solution.h"
#include"input.h"

void flip(char& c) {
    if (c == '+') {
        c = '-';
    } else {
        c = '+';
    }
}

int solve(string& s, int k) {
    int count = 0;

    for (int i = 0; i + k <= s.size(); ++i) {
        if (s[i] == '-') {
            count++;
            for (int j = i; j < i + k; ++j) {
                flip(s[j]);
            }
        }
    }

    for (int i = s.size() - k + 1; i < s.size(); ++i) {
        if (s[i] == '-') {
            return -1;
        }
    }

    return count;
}

int main() {
    int T, K;
    string S;

    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cin >> S >> K;
        //cout << S << K << endl;
        int result = solve(S, K);

        printf("Case #%d: %s\n", i, result == -1 ? "IMPOSSIBLE" : to_string(result).c_str());

    }
    return 0;
}


