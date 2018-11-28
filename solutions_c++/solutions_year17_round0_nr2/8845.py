//
//  main.cpp
//  task
//
//  Created by Vadim Zakharenko on 09/04/2017.
//  Copyright © 2017 Vadim Zakharenko. All rights reserved.
//

#include <iostream>

using namespace std;

bool ok(int n) {
    int last = 10;
    while (n > 0) {
        if (last < n%10) {
            return false;
        }
        last = n%10;
        n /= 10;
    }
    return true;
}

int main(int argc, const char * argv[]) {
    freopen("/Users/vadimantiy/Developer/codejam17/task2/task2/input.txt", "r", stdin);
    freopen("/Users/vadimantiy/Developer/codejam17/task2/task2/output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
    int caseNumber;
    cin >> caseNumber;
    for (int casen = 0; casen < caseNumber; casen++) {
        cerr << casen << '\n';
        cout << "Case #" << casen + 1 << ": ";
        int n, ans = 0;
        cin >> n;
        while (n > 0) {
            if (ok(n)) {
                ans = n;
                break;
            }
            n--;
        }
        cout << ans << '\n';
    }
    return 0;
}
