//
//  main.cpp
//  task
//
//  Created by Vadim Zakharenko on 09/04/2017.
//  Copyright © 2017 Vadim Zakharenko. All rights reserved.
//

#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    freopen("/Users/vadimantiy/Developer/task/task/input.txt", "r", stdin);
    freopen("/Users/vadimantiy/Developer/task/task/output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
    int caseNumber;
    cin >> caseNumber;
    for (int casen = 0; casen < caseNumber; casen++) {
        cerr << casen << '\n';
        cout << "Case #" << casen + 1 << ": ";
        string s;
        int k;
        cin >> s >> k;
        bool imp = false;
        int ans = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '+') {
                continue;
            }
            if (i + k - 1 >= s.length()) {
                imp = true;
                break;
            }
            ans++;
            for (int j = i; j <= i + k - 1; j++) {
                if (s[j] == '+') {
                    s[j] = '-';
                } else {
                    s[j] = '+';
                }
            }
        }
        if (imp) {
            cout << "IMPOSSIBLE\n";
        } else {
            cout << ans << "\n";
        }
    }
    return 0;
}
