#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <queue>
#include <cmath>
#include <set>
#include <set>
#include <string>
#include <ctime>
#include <cstring>
#include <algorithm>
#include <functional>
//#include <bits/stdc++.h>
#define FOR(i, l, r) for (int i = int(l), __border_right##i = int(r); i < __border_right##i; i++)
#define STRUCT3(v1, v2, v3, name) struct name \
		{   \
			int v1, v2, v3; \
			name(int v1 = 0, int v2 = 0, int v3 = 0) : v1(v1), v2(v2), v3(v3) {} \
			friend bool operator < (const name& athis, const name& other) \
			{   \
				if (athis.v1 != other.v1) return athis.v1 < other.v1;   \
				if (athis.v2 != other.v2) return athis.v2 < other.v2;   \
				return athis.v3 < other.v3;   \
			}\
		}
#define PB push_back
#define LS (((k) << 1) + 1)
#define RS (((k) << 1) + 2)
#define LM ((l) + (r) >> 1)
#define RM (LM + 1)
//#define LOG(x) tb[(UI(x) * (UI)263572066) >> 27]
#define FST first
#define SCD second
#define retunr return
#define modp 1000000007
#define EPS 1e-7
#define INF 0x3f3f3f3f
#define MAX2 113
#define MAX3 1013
#define MAX4 10013
#define MAX5 100013
#define MAX6 1000013
#define MAXN 51
#define MANX MAXN
using namespace std;
typedef long long LL;
typedef unsigned int UI;
typedef pair<int, int> PA;

int T;
int N, P;
int R[MAXN], Q[MAXN][MAXN];
int mi[MAXN][MAXN], ma[MAXN][MAXN];
priority_queue<PA, vector<PA>, greater<PA> > que;
int pt[MAXN];

int main()
{
//    freopen("B-large.in", "r", stdin);
//    freopen("data.out", "w", stdout);
    scanf("%d", &T);
    FOR(Ce, 1, T + 1) {
        scanf("%d%d", &N, &P);
        FOR(i, 0, N) {
            scanf("%d", &R[i]);
        }
        FOR(i, 0, N) {
            FOR(j, 0, P) {
                scanf("%d", &Q[i][j]);
            }
            sort(Q[i], Q[i] + P);
            FOR(j, 0, P) {
                mi[i][j] = (10 * Q[i][j] + (11 * R[i] - 1)) / (11 * R[i]);
                ma[i][j] = 10 * Q[i][j] / (9 * R[i]);
            }
        }
        memset(pt, 0, sizeof(pt));
        int res = 0;
        FOR(i, 0, N) {
            que.push(PA(ma[i][0], i));
        }
        while (true) {
            PA p = que.top();
            que.pop();
            int tmp = 0;
            FOR(i, 0, N) {
                tmp = max(tmp, mi[i][pt[i]]);
            }
            if (p.FST >= tmp)  {
                res++;
                while (!que.empty()) {
                    que.pop();
                }
                bool flag = false;
                FOR(i, 0, N) {
                    pt[i]++;
                    if (pt[i] == P) {
                        flag = true;
                        break;
                    }
                    que.push(PA(ma[i][pt[i]], i));
                }
                if (flag) {
                    break;
                }
            }
            else {
                int x = p.SCD;
                pt[x]++;
                if (pt[x] == P) {
                    break;
                }
                que.push(PA(ma[x][pt[x]], x));
            }
        }
        while (!que.empty()) {
            que.pop();
        }
        printf("Case #%d: %d\n", Ce, res);
    }
    return 0;
}
