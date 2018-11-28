#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <deque>
#include <cmath>
using namespace std;

deque<long long> label, num;
/*
void debug() {
    if(label.size() != num.size()) {
        cout << "size not same" << endl;
        return;
    }
    cout << "hehe" << endl;
    for(int i = 0;i < label.size();i ++) {
        cout << label.at(i) << " " << num.at(i) << endl;
    }
}
*/

#define pi acos(-1.0)

double dp[55];

int main()
{
    //freopen("C-small-1-attempt0.in", "r", stdin);
    //freopen("out.out", "w", stdout);
    int casenum;  scanf("%d", &casenum);
    for(int cs = 1; cs <= casenum; cs ++) {
        double U;
        int N, K;
        scanf("%d%d%lf", &N, &K, &U);
        for(int i = 0;i < N;i ++) {
            scanf("%lf", dp + i);
        }
        sort(dp, dp + N);
        int tt = 0;
        double last = 0.0;
        for(int i = 0;i < N;i ++) {
            double delta = dp[i] - last;
            double need = delta * tt;
            if(need >= U) {
                last += U / tt;
                U = 0.0;
                break;
            } else {
                last = dp[i];
                tt += 1;
                U -= need;
            }
        }
        double ans = 1.0;
        if(tt == N) {
            last += U / tt;
        }
        if(last >= 1.0) last = 1.0;
        for(int i = 0;i < tt;i ++) {
            ans *= last;
        }
        for(int i = tt;i < N;i ++) {
            ans *= dp[i];
        }
        printf("Case #%d: %lf\n", cs, ans);
    }
    return 0;
}
