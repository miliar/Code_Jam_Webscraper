#include <bits/stdc++.h>
using namespace std;
void solve() {
    int r,c;
    scanf("%d %d",&r,&c);
    char arr[r][c];
    char ss[1000];
    for(int i = 0;i < r;i++) {
        scanf("%s",ss);
        for(int j = 0;j < c;j++) {
            arr[i][j] = ss[j];
        }
    }
    // expand col first
    for(int i = 0;i < r;i++) {
        for(int j = 0;j < c;j++) {
            if(arr[i][j] != '?') {
                // expand up
                int di = 1;
                while(i-di >= 0) {
                    if(arr[i-di][j] != '?') break;
                    arr[i-di][j] = arr[i][j];
                    di++;
                }
                di = 1;
                while(i+di < r) {
                    if(arr[i+di][j] != '?') break;
                    arr[i+di][j] = arr[i][j];
                    di++;
                }

            }
        }
    }
    // expand row
    for(int i = 0;i < r;i++) {
        for(int j = 0;j < c;j++) {
            if(arr[i][j] != '?') {
                // expand row
                int dj = 1;
                while(j-dj >= 0) {
                    if(arr[i][j-dj] != '?') break;
                    arr[i][j-dj] = arr[i][j];
                    dj++;
                }
                dj = 1;
                while(j+dj < c) {
                    if(arr[i][j+dj] != '?') break;
                    arr[i][j+dj] = arr[i][j];
                    dj++;
                }
            }
        }
    }
    printf("\n");
    for(int i = 0;i < r;i++) {
        for(int j = 0;j < c;j++) {
            printf("%c",arr[i][j]);
        }
        printf("\n");
    }
}
int main() {
    int t;
    scanf("%d",&t);
    for(int i = 0;i < t;i++) {
        printf("Case #%d: ",i+1);
        solve();
    }
}
