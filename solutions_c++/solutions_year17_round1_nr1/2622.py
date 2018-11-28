/*************************************************************************
	> File Name: a.cpp
	> Author: Anson
	> Mail: 354830997@qq.com
	> Created Time: Sat 15 Apr 2017 10:38:26 AM CST
 ************************************************************************/

#include <iostream>
#include <cstdio>
#include <cstring>
#define LL long long
#define clr(x) memset(x,0,sizeof(x))
using namespace std;
#define MAX 26

char g[MAX][MAX];
int n, m;

int main()
{
    //ios::sync_with_stdio(false);
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int t = 0;
    scanf ("%d", &t);
    //cin>> t;
    for (int cas = 1; cas <= t; cas++) 
    {
        scanf("%d%d", &n, &m);
        //cin>> n>> m;
        for(int i = 0; i < n; i++)
            scanf("%s", &g[i]);
            //cin>> g[i];
        for (int i = 1; i < n; i++) 
            for (int j  = 0; j < m; j++) 
                if (g[i][j] == '?') 
                    g[i][j] = g[i-1][j];
        for (int i = n-2; i >= 0; i--)
            for (int j = 0; j < m; j++) 
                if (g[i][j] == '?')
                    g[i][j] = g[i+1][j];
        for (int j = 1; j < m; j++)
            for (int i = 0; i < n; i++) 
                if (g[i][j] == '?')
                    g[i][j] = g[i][j-1];
        for (int j = m-2;j >= 0; j--) 
            for (int i = 0; i < n; i++)
                if (g[i][j] == '?')
                    g[i][j] = g[i][j+1];
        printf("case #%d:\n", cas);
        //cout<< "case #"<< cas<< ":"<<endl;
        for (int i = 0; i < n; i++) {
            printf ("%s\n", g[i]);
            //for (int i = 0; i < n; i++) {
                //cout<< g[i]<< endl;
            }
        //}
    }

	return 0;
}
