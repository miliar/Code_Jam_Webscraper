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
const string filename = "A-large";
int Test, n, m;
char s[100][100];

int main()
{
	freopen((filename+".in").c_str(), "r", stdin);
	freopen((filename+".out").c_str(), "w", stdout);
    scanf("%d", &Test);
    for (int Case = 1; Case <= Test; Case ++){
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; i ++) {
            scanf("%s", s[i]);
        }
        for (int i = 0; i < n; i ++) {
            int k = -1;
            for (int j = 0; j < m && k == -1; j ++) {
                if (s[i][j] != '?') k = j;
            }
            if (k == -1) continue;
            for (int j = 0; j < m; j ++) {
                if (s[i][j] == '?') {
                    s[i][j] = s[i][k];
                } else {
                    k = j;
                }
            }
        }
        int k = -1;
        for (int i = 0; i < n && k == -1; i ++) {
            if (s[i][0] != '?') k = i;
        }
        for (int i = 0; i < n; i ++) {
            if (s[i][0] == '?') {
                for (int j = 0; j < m; j ++) {
                    s[i][j] = s[k][j];
                }
            } else {
                k = i;
            }
        }
        printf("Case #%d:\n", Case);
        for (int i = 0; i < n; i ++) {
            printf("%s\n", s[i]);
        }
    }
    return 0;
}
