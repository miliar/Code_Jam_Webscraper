/*
 *  Author:
 *      Indestinee
 *  Date:
 *      2017/04/15
 *  Name:
 *      a.cpp
 */

#include <bits/stdc++.h>
using namespace std;
const int maxn = 30;
char a[maxn][maxn], o;
int n, m, cas, id[maxn];
int main() {
    scanf("%d", &cas);
    for (int t = 1; t <= cas; t++) {
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; i++) {
            scanf("%s", a[i]);
            id[i] = i;
        }
        for (int i = 0; i < n; i++) {
            bool flag = false;
            for (int j = 0; j < m; j++)
                if (a[i][j] != '?')
                    flag = true;
            if (flag)
                continue;
            id[i] = -1;
        }
        for (int i = 1; i < n; i++)
            if (id[i] == -1)
                id[i] = id[i - 1];
        for (int i = n - 2; i >= 0; i--)
            if (id[i] == -1)
                id[i] = id[i + 1];
        for (int i = 0; i < n; i++) {
            if (id[i] != i)
                continue;
            int j = 0;
            while (j < m) {
                while (j < m && a[i][j] == '?')
                    j++;
                if (j == m)
                    break;
                o = a[i][j];
                for (int k = 0; k < n; k++)
                    if (id[k] == i)
                        a[k][j] = o;    
                j++;
                while (j < m && a[i][j] == '?') {
                    for (int k = 0; k < n; k++)
                        if (id[k] == i)
                            a[k][j] = o; 
                    j++;
                }
            }
            j = m - 1;
            while (j >= 0) {
                while (j >= 0 && a[i][j] == '?')
                    j--;
                if (j < 0)
                    break;
                o = a[i][j];
                for (int k = 0; k < n; k++)
                    if (id[k] == i)
                        a[k][j] = o;
                j--;
                while (j >= 0 && a[i][j] == '?') {
                    for (int k = 0; k < n; k++)
                        if (id[k] == i)
                            a[k][j] = o;
                    j--;
                }
            }
        }
        printf("Case #%d:\n", t);
        for (int i = 0; i < n; i++)
            puts(a[i]);
    }
    return 0;
}
