//
//  main.cpp
//  B-large
//
//  Created by Xudong Ma on 4/8/17.
//  Copyright © 2017 Xudong Ma. All rights reserved.
//

#include <iostream>

using namespace std;

char res[20];

bool dfs(const string& n, int idx, char pre, bool dec) {
    if (idx == n.length()) {
        res[idx] = '\0';
        return true;
    }
    char i;
    if (dec) i = '9';
    else i = n[idx];
    for (; i >= '0'; i--) {
        if (i < pre) return false;
        res[idx] = i;
        if (dfs(n, idx + 1, i, dec || i < n[idx])) return true;
    }
    return false;
}

string solve(string n) {
    if (n.length() == 1) return n;
    dfs(n, 0, '0', false);
    string ans = res;
    while(ans[0] == '0') ans.erase(0, 1);
    return ans;
}

int main(int argc, const char * argv[]) {
    int T;
    scanf("%d", &T);
    for (int caseno = 0; caseno < T; caseno++) {
        char n[20];
        scanf("%s", n);
        string num(n);
        string ans = solve(n);
        printf("Case #%d: %s\n", caseno + 1, ans.c_str());
    }
    return 0;
}
