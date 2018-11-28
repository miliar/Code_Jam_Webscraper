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

string solve(const string& s) {
    string result;
    int i = 1;

    result.push_back(s[0]);
    while (i < s.size() && s[i] >= result.back()) {
        result.push_back(s[i]);
        i++;
    }

    if (i != s.size()) {
        result.push_back(s[i]);
        while (i != 0 && result[i-1] > result[i]) {
            result.pop_back();
            i--;
            result[i]--;
        }

        if (result.back() == '0') {
            result.pop_back();
        }

        for (i++; i < s.size(); ++i) {
            result.push_back('9');
        }
    }

    return result;
}

int main() {
    int T;
    string N;

    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cin >> N;
        //cout << S << K << endl;

        printf("Case #%d: %s\n", i, solve(N).c_str());

    }
    return 0;
}


