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

vector<char> ans;
struct cake{
    double r, h;
    bool operator < (cake & a) {
        return r > a.r;
    }
}c[1010];
struct sray{
    double r, h;
    bool operator < (sray & a) {
        return r * h > a.r * a.h;
    }
}tmp[1010];
double dp[1010];
int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("out.out", "w", stdout);
    int casenum;  scanf("%d", &casenum);
    for(int cs = 1; cs <= casenum; cs ++) {
        int N, K; scanf("%d%d", &N, &K);
        for(int i = 0;i < N;i ++) {
            int aa, bb;
            scanf("%d%d", &aa, &bb);
            c[i].r = aa;
            c[i].h = bb;
        }
        sort(c, c + N);
        memset(dp, 0, sizeof(dp));
        for(int i = 0;i < N;i ++) {
            dp[i] = ((double)c[i].r) * ((double)c[i].r) + 2.0 * c[i].r * c[i].h;
            for(int j = i + 1;j < N;j ++) {
                tmp[j - i - 1].r = c[j].r;
                tmp[j - i - 1].h = c[j].h;
            }
            if(i + K > N) break;
            sort(tmp, tmp + N - i - 1);
            for(int j = 0;j < K - 1;j ++) {
                dp[i] += 2.0 * tmp[j].r * tmp[j].h;
            }
        }
        double ans = 0.0;
        for(int i = 0;i < N;i ++) {
            if(ans < dp[i]) {
                ans = dp[i];
            }
        }
        ans *= pi;
        printf("Case #%d: %.9f\n", cs, ans);
    }
    return 0;
}
