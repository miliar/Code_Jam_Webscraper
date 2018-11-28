#include <cstdio>
#include <algorithm>
#include <string>
#include <map>
#include <vector>
#include <iostream>

using namespace std;
int T, R, C, qcnt;
char arr[100][100];

vector<char> alpha;
int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> T;
    for(int test = 1; test <= T; ++test) {
        memset(arr, 0, sizeof(arr));
        cin >> R >> C;
        for (int i = 1; i <= R; ++i)
            scanf("%s", arr[i] + 1);

        for(int i = 1; i <= R; ++i) {
            for(int j = 2; j <= C; ++j) {
                if(arr[i][j] == '?')
                    arr[i][j] = arr[i][j - 1];
            }
            for(int j = C - 1; j >= 1; --j) {
                if(arr[i][j] == '?')
                    arr[i][j] = arr[i][j + 1];
            }
        }
        for(int i = 2; i <= R; ++i) {
            if(arr[i][1] != '?')
                continue;
            for(int j = 1; j <= C; ++j)
                arr[i][j] = arr[i - 1][j];
        }

        for(int i = R - 1; i >= 1; --i) {
            if(arr[i][1] != '?')
                continue;
            for(int j = 1; j <= C; ++j)
                arr[i][j] = arr[i + 1][j];
        }

        printf("Case #%d:\n", test);
        for(int i = 1; i <= R; ++i) {
            printf("%s\n", arr[i] + 1);
        }

    }
    return 0;
}