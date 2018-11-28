#include<bits/stdc++.h>
using namespace std;

int R, C;

vector<vector<char> > G, ans;

void main2(int tc) {
    scanf("%d %d", &R, &C);

    G.clear();
    G = vector<vector<char> >(R, vector<char>(C));

    for(int i = 0; i < R; i++) {
        scanf("\n");
        for(int j = 0; j < C; j++) {
            scanf("%c", &G[i][j]);
        }
    }

    ans.clear();
    ans = vector<vector<char> >(R, vector<char>(C, '?'));

    for(int i = 0; i < R; i++) {
        for(int j = 0; j < C; j++) {
            if(G[i][j] != '?') {

                ans[i][j] = G[i][j];
                for(int k = i + 1; k < R; k++) {
                    if(G[k][j] != '?') break;
                    ans[k][j] = G[i][j];
                }

            }
        }
    }

    for(int i = 0; i < R; i++) {
        for(int j = 0; j < C; j++) {
            if(G[i][j] != '?') {

                for(int k = i - 1; k >= 0; k--) {
                    if(ans[k][j] != '?') break;
                    ans[k][j] = G[i][j];
                }

            }
        }
    }

    for(int i = 0; i < R; i++) {
        for(int j = 0; j < C; j++) {
            if(ans[i][j] != '?') {

                for(int k = j + 1; k < C; k++) {
                    if(ans[i][k] != '?') break;
                    ans[i][k] = ans[i][j];
                }

            }
        }
    }

    for(int i = 0; i < R; i++) {
        for(int j = 0; j < C; j++) {
            if(ans[i][j] != '?') {

                for(int k = j - 1; k >= 0; k--) {
                    if(ans[i][k] != '?') break;
                    ans[i][k] = ans[i][j];
                }

            }
        }
    }

    printf("Case #%d:\n", tc);

    for(int i = 0; i < R; i++) {
        for(int j = 0; j < C; j++) {
            printf("%c", ans[i][j]);
        }
        printf("\n");
    }
}

int TC;
int main() {

    freopen("inA.txt", "r", stdin);
    freopen("outA.txt", "w", stdout);

    scanf("%d", &TC);
    for(int i = 1; i <= TC; i++) main2(i);
}
