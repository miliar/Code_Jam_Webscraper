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
const string filename = "B-large";
int Test, N, M;
int R[60], Q[60][60], P[60];
pair<int, int> A[60][60];

pair<int, int> calc(double x, double y)
{
    int l = int(x / y / 1.1 - 1e-8) + 1;
    int r = int(x / y / 0.9 + 1e-8);
    return make_pair(l, r);
}

int solve()
{
    for (int i = 0; i < N; i ++) {
        P[i] = 0;
    }
    int cnt = 0;
    while (true) {
        int l = 0;
        int r = 0;
        for (int i = 0; i < N; i ++) {
            while (P[i] < M && A[i][P[i]].first > A[i][P[i]].second) {
                P[i] ++;
            }
            if (P[i] == M) return cnt;
            if (A[i][P[i]].first > A[l][P[l]].first) l = i;
            if (A[i][P[i]].second < A[r][P[r]].second) r = i;
        }
        if (A[l][P[l]].first > A[r][P[r]].second) {
            P[r] ++;
        } else {
            cnt ++;
            for (int i = 0; i < N; i ++) {
                P[i] ++;
            }
        }
    }
    return -1;
}

int main()
{
	freopen((filename+".in").c_str(), "r", stdin);
	freopen((filename+".out").c_str(), "w", stdout);
	scanf("%d", &Test);
	for (int Case = 1; Case <= Test; Case ++) {
        scanf("%d%d", &N, &M);
        for (int i = 0; i < N; i ++) {
            scanf("%d", &R[i]);
        }
        for (int i = 0; i < N; i ++) {
            for (int j = 0; j < M; j ++) {
                scanf("%d", &Q[i][j]);
            }
            sort(Q[i], Q[i] + M);
            for (int j = 0; j < M; j ++) {
                A[i][j] = calc(Q[i][j], R[i]);
            }
        }
        printf("Case #%d: %d\n", Case, solve());
	}
	return 0;
}
