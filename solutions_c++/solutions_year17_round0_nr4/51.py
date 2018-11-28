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
const string filename = "D-large";
int Test, N, M, match[222];
int grid[222][222], ans[222][222];
char str[22];
int s[222], t[222];
bool e[222][222], vis[222];

bool find_match(int i)
{
    for (int j = 1; j <= 200; j ++)
    if (e[i][j] && !vis[j]) {
        vis[j] = true;
        if (match[j] == 0 || find_match(match[j])) {
            match[j] = i;
            return true;
        }
    }
    return false;
}

void maximumMatch()
{
    memset(match, 0, sizeof(match));
    for (int i = 1; i <= 200; i ++) {
        memset(vis, false, sizeof(vis));
        find_match(i);
    }
}

void solve1()
{
    memset(s, 0, sizeof(s));
    memset(t, 0, sizeof(t));
    for (int i = 1; i <= N; i ++) {
        for (int j = 1; j <= N; j ++)
        if (grid[i][j] != 0 && grid[i][j] != 1) {
            s[i] ++;
            t[j] ++;
            //if (s[i] > 1) cerr << "xx" << endl;
            //if (t[i] > 1) cerr << "xx" << endl;
        }
    }
    memset(e, false, sizeof(e));
    memset(match, 0, sizeof(match));
    for (int i = 1; i <= N; i ++) {
        for (int j = 1; j <= N; j ++)
        if ((grid[i][j] == 0 || grid[i][j] == 1) && s[i] == 0 && t[j] == 0) {
            e[i][j] = true;
        }
    }
    maximumMatch();
    for (int j = 1; j <= N; j ++)
    if (match[j]) {
        int i = match[j];
        ans[i][j] |= 2;
    }
}

void solve2()
{
    memset(s, 0, sizeof(s));
    memset(t, 0, sizeof(t));
    for (int i = 1; i <= N; i ++) {
        for (int j = 1; j <= N; j ++)
        if (grid[i][j] != 0 && grid[i][j] != 2) {
            s[i+j] ++;
            t[i-j+N] ++;
            //if (s[i+j] > 1) cerr << "xx" << endl;
            //if (t[i-j+N] > 1) cerr << "xx" << endl;
        }
    }
    memset(e, false, sizeof(e));
    memset(match, 0, sizeof(match));
    for (int i = 1; i <= N; i ++) {
        for (int j = 1; j <= N; j ++)
        if ((grid[i][j] == 0 || grid[i][j] == 2) && s[i+j] == 0 && t[i-j+N] == 0) {
            e[i+j][i-j+N] = true;
        }
    }
    maximumMatch();
    for (int j = 1; j <= 200; j ++)
    if (match[j]) {
        int i = match[j];
        int x = (i+j-N)/2;
        int y = (i-j+N)/2;
        ans[x][y] |= 1;
    }
}

int main()
{
	freopen((filename+".in").c_str(), "r", stdin);
	freopen((filename+".out").c_str(), "w", stdout);
	scanf("%d", &Test);
	for (int Case = 1; Case <= Test; Case ++) {
        scanf("%d%d", &N, &M);
        memset(grid, 0, sizeof(grid));
        for (int i = 0; i < M; i ++) {
            int x, y;
            scanf("%s%d%d", str, &x, &y);
            if (str[0] == '+') grid[x][y] = 1;
            if (str[0] == 'x') grid[x][y] = 2;
            if (str[0] == 'o') grid[x][y] = 3;
        }
        memset(ans, 0, sizeof(ans));
        solve1();
        solve2();
		printf("Case #%d: ", Case);
		int ret = 0, cnt = 0;
		for (int i = 1; i <= N; i ++) {
            for (int j = 1; j <= N; j ++) {
                int k = ans[i][j] | grid[i][j];
                ret += (k+1)/2;
                if (ans[i][j] > 0) cnt ++;
            }
		}
		printf("%d %d\n", ret, cnt);
		//if (ret != N*2) cerr << "xxx" << endl;
		for (int i = 1; i <= N; i ++) {
            for (int j = 1; j <= N; j ++) {
                int k = ans[i][j] | grid[i][j];
                //printf("%c", ".+xo"[k]);
                if (ans[i][j] > 0) {
                    printf("%c %d %d\n", ".+xo"[k], i, j);
                }
            }
            //printf("\n");
		}
	}
	return 0;
}
