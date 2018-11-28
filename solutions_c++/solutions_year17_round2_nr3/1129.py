// A C program to implement Ukkonen's Suffix Tree Construction
// Here we build generalized suffix tree for two strings
// And then we find longest common substring of the two input strings
#include <stdio.h>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <iostream>
#include <string.h>
#include <string>
#include <stdlib.h>
#include <vector>
#include <cmath>
using namespace std;

typedef long long ll;
#define MAXN 105

#define INF 1e15

ll t;

double n, q;
double eps = 1e-7;


ll s[MAXN], e[MAXN];
ll d[MAXN][MAXN];
ll dist[MAXN][MAXN];
double cst[MAXN][MAXN];
double bst[MAXN][MAXN];

int main()
{
    cin >> t;
    for (int cse = 1; cse <= t; cse++){
        cin >> n >> q;
        for (int i = 1; i <= n; i++){
            cin >> e[i] >> s[i];
        }
        for (int i = 1; i <= n; i++){
            for (int j = 1; j <= n; j++){
                cin >> d[i][j];
                if (d[i][j] > e[i] || d[i][j] == -1){
                    dist[i][j] = INF;
                }
                else {
                    dist[i][j] = d[i][j];
                }
                if (i == j) dist[i][j] = 0;
                bst[i][j] = INF;
                cst[i][j] = INF;
            }
        }
        for (int k = 1; k <= n; k++){
            for (int i = 1; i <=n; i++){
                for (int j = 1; j <= n; j++){
                    if (dist[i][j] > dist[i][k] + dist[k][j]){
                        dist[i][j] = dist[i][k] + dist[k][j];
                    }
                }
            }
        }
        
        for (int k = 1; k <= n; k++){
            for (int i = 1; i <= n; i++){
                if (dist[k][i] <= e[k]){
                    cst[k][i] = dist[k][i]/double(s[k]);
                }
                else
                    cst[k][i] = INF;
            }
        }
        
        for (int k = 1; k <= n; k++){
            for (int i = 1; i <= n; i++){
                for (int j = 1; j <= n; j++){
                    if (cst[i][j] > cst[i][k] + cst[k][j]){
                        cst[i][j] = cst[i][k]+ cst[k][j];
                    }
                }
            }
        }
        cout << "Case #" << cse << ":";
        for (int i = 0; i < q; i++){
            ll u, v;
            cin >> u >> v;
            printf(" %0.07f", cst[u][v]);
        }
        cout << endl;
        
    }
    return 0;
}

