//
//  main.cpp
//  task
//
//  Created by Vadim Zakharenko on 09/04/2017.
//  Copyright © 2017 Vadim Zakharenko. All rights reserved.
//

#include <iostream>

using namespace std;

int getls(int i, int *a) {
    int res = 0;
    int j = i - 1;
    while (j > 0 && a[j] == 0) {
        res++;
        j--;
    }
    return res;
}

int getrs(int i, int n, int *a) {
    int res = 0;
    int j = i + 1;
    while (j <= n && a[j] == 0) {
        res++;
        j++;
    }
    return res;
}

int main(int argc, const char * argv[]) {
    freopen("/Users/vadimantiy/Developer/codejam17/task3/task3/input.txt", "r", stdin);
    freopen("/Users/vadimantiy/Developer/codejam17/task3/task3/output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
    int caseNumber;
    cin >> caseNumber;
    for (int casen = 0; casen < caseNumber; casen++) {
        cerr << casen << '\n';
        cout << "Case #" << casen + 1 << ": ";
        int n, k;
        cin >> n >> k;
        int a[1111] = {0};
        a[0] = a[n + 1] = 1;
        int ans_ls, ans_rs, l;
        while (k--) {
            ans_ls = ans_rs = -1; l = 0;
            for (int i = 1; i <= n; i++) if (a[i] == 0) {
                int ls = getls(i, a), rs = getrs(i, n, a);
                bool acc = false;
                if (min(ls, rs) > min(ans_ls, ans_rs)) {
                    acc = true;
                } else if (min(ls, rs) == min(ans_ls, ans_rs)) {
                    if (max(ls, rs) > max(ans_ls, ans_rs)) {
                        acc = true;
                    }
                }
                if (acc) {
                    ans_ls = ls, ans_rs = rs;
                    l = i;
                }
            }
            a[l] = 1;
        }
        cout << max(ans_ls, ans_rs) << " " << min(ans_rs, ans_ls) << '\n';
    }
    return 0;
}
