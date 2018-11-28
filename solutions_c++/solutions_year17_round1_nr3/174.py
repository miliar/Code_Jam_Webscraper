#include <set>
#include <map>
#include <cmath>
#include <ctime>
#include <queue>
#include <string>
#include <cstdio>
#include <vector>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>
using namespace std;
const string filename = "C-small-attempt0";
long long INF = 1000000000000000000LL;
int Test;
int H_d, A_d, H_k, A_k, B, D;
int h_d, a_d, h_k, a_k;

long long calc_debuff(int a)
{
    if (a >= a_k) return 0;
    long long cnt = 0;
    if (a_k - 1 + a_k - 2 >= h_d) return INF;
}

long long solve(int n, int m)
{
    h_d = H_d;
    a_d = A_d;
    h_k = H_k;
    a_k = A_k;
    long long cnt = 0;
    for (int i = 0; i < n; i ++) {
        if (h_d <= a_k - D) {
            cnt += 1;
            h_d = H_d - a_k;
        }
        a_k -= D;
        h_d -= a_k;
        cnt ++;
        if (h_d <= 0) return INF;
    }
    for (int i = 0; i < m; i ++) {
        if (h_d <= a_k) {
            h_d = H_d - a_k;
            cnt ++;
        }
        h_d -= a_k;
        a_d += B;
        cnt ++;
        if (h_d <= 0) return INF;
    }
    while (h_k > 0) {
        h_k -= a_d;
        cnt ++;
        if (h_k <= 0) break;
        if (h_d <= a_k) {
            h_d = H_d - a_k;
            cnt ++;
        }
        h_d -= a_k;
        if (h_d <= 0) return INF;
    }
    return cnt;
}

int main()
{
	freopen((filename+".in").c_str(), "r", stdin);
	freopen((filename+".out").c_str(), "w", stdout);
	scanf("%d", &Test);
	for (int Case = 1; Case <= Test; Case ++) {
        scanf("%d%d%d%d%d%d", &H_d, &A_d, &H_k, &A_k, &B, &D);
        long long ret = INF;
        for (int i = 0; i <= 100; i ++) {
            for (int j = 0; j <= 100; j ++) {
                ret = min(ret, solve(i, j));
            }
        }
        printf("Case #%d: ", Case);
        if (ret == INF) {
            printf("IMPOSSIBLE\n");
        } else {
            printf("%lld\n", ret);
        }
	}
	return 0;
}
