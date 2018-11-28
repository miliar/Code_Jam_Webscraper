#include<iostream>
#include<algorithm>
#include<cstdio>
using namespace std;
char cake[30][30];

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int ca = 1;ca <= T;ca++) {
        int n, m;
        scanf("%d%d", &n, &m);
        for (int i = 0;i < n;i++) scanf("%s", cake[i]);
        int pos1 = -1;
        for (int i = 0;i < n;i++) {
            bool flag = false;
            for (int j = 0;j < m;j++) {
                if (cake[i][j] != '?') {
                    flag = true;
                    break;
                }
            }
            if (flag) {
                pos1 = i;
                break;
            }
        }
        for (int i = pos1;i < n;i++) {
            int pos = -1;
            for (int j= 0;j< m;j++) {
                if (cake[i][j] != '?') {
                    pos = j;
                    break;
                }
            }
            if (pos == -1) {
                for (int j = 0;j < m;j++) {
                    cake[i][j] = cake[i - 1][j];
                }
               
            }
            else {
                int p = 0;
                while (true) {
                    for (int j = p;j < pos;j++) cake[i][j] = cake[i][pos];
                    p = pos + 1;
                    for (int j = p;j < m;j++) {
                        if (cake[i][j] != '?') {
                            pos = j;
                            break;
                        }
                    }
                    if (pos == p - 1) {
                        for (int j = p;j < m;j++) {
                            cake[i][j] = cake[i][p - 1];
                        }
                        break;
                    }
                }
            }
        }
        for (int i = 0;i < pos1;i++) {
            for (int j = 0;j < m;j++) {
                cake[i][j] = cake[pos1][j];
            }
        }
        printf("Case #%d:\n", ca);
        for (int i = 0;i < n;i++) printf("%s\n", cake[i]);
    }
    return 0;
}