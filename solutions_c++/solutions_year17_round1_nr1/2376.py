#include <bits/stdc++.h>
using namespace std;
struct node{
    int r, c;
};
node lu[26], rd[26];
char graph[30][30];


int main()
{

    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; i++) {
        int r, c;
        scanf("%d%d", &r, &c);
        for (int j = 0; j < 26 ;j++) {
            lu[j].r = rd[j].r = rd[j].c = -1;
        }
        for (int j = 0 ;j < r; j++){
            scanf("%s", graph[j]);
        }
        for (int j = 0; j < r; j++) {
            for (int k = 0; k < c; k++) {
                if (lu[graph[j][k]-'A'].r == -1) {
                    lu[graph[j][k]-'A'].r = j;
                    lu[graph[j][k]-'A'].c = k;
                }
                if (rd[graph[j][k]-'A'].r < j || rd[graph[j][k]-'A'].c < k) {
                    rd[graph[j][k]-'A'].r = j;
                    rd[graph[j][k]-'A'].c = k;
                }
            }
        }
        for (int j = 0; j < 26; j++) {
            for (int k = lu[j].r; k <= rd[j].r; k++){
                for (int l = lu[j].c; l <= rd[j].c; l++)
                    graph[k][l] = j+'A';
            }
        }

        for (int j = 0; j < r; j++) {
            int k=0;
            while (k < c){
                while (graph[j][k]=='?') k++;
                int l = k;
                char ch = graph[j][k];
                while (graph[j][k]==ch && k<c) k++;
                int fail = 0;
                for (int x = l; x < k; x++)
                    if (graph[j+1][x] != '?') fail=1;
                if (fail) continue;
                for (int x = l; x < k; x++)
                    graph[j+1][x] = ch;
            }
        }
        for (int j = r-1; j>=0; j--) {
            int k=0;
            while (k < c){
                while (graph[j][k]=='?') k++;
                int l = k;
                char ch = graph[j][k];
                while (graph[j][k]==ch && k<c) k++;
                int fail=0;
                for (int x = l; x < k; x++)
                    if (graph[j-1][x] != '?') fail=1;
                if (fail) continue;
                for (int x = l; x < k; x++)
                    graph[j-1][x] = ch;
            }
        }
        for (int k = 0; k < c; k++) {
            int j = 0;
            while (j < r){
                while (graph[j][k]=='?') j++;
                int u = j;
                char ch = graph[j][k];
                while (graph[j][k]==ch && j<r) j++;
                int fail=0;
                for (int x = u; x < j; x++)
                    if (graph[x][k+1] != '?') fail=1;
                if (fail) continue;
                for (int x = u; x < j; x++)
                    graph[x][k+1] = ch;
            }
        }
        for (int k = c-1; k >= 0; k--) {
            int j = 0;
            while (j < r){
                while (graph[j][k]=='?') j++;
                int u = j;
                char ch = graph[j][k];
                while (graph[j][k]==ch && j<r) j++;
                int fail=0;
                for (int x = u; x < j; x++)
                    if (graph[x][k-1] != '?') fail=1;
                if (fail) continue;
                for (int x = u; x < j; x++)
                    graph[x][k-1] = ch;
            }
        }

        printf("Case #%d:\n", i);
        for (int j = 0; j < r; j++){
            for (int k = 0; k < c; k++)
                printf("%c", graph[j][k]);
            printf("\n");
        }
    }






    return 0;
}
