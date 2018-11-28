#include <bits/stdc++.h>

using namespace std;

#define ff first
#define ss second

typedef pair<int, int> ii;
typedef long long ll;

char mat[25][25];

int main()
{
    int t;
    cin >> t;

    int tc = 1;
    while (t--) {
        int r, c;
        cin >> r >> c;

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                cin >> mat[i][j];
            }
        }

        for (int i = 0; i < r; i++) {
            char name = 0;
            int j = 0;

            while (j < c) {
                if (mat[i][j] != '?') {
                    if (!name) for (int k = 0; k < j; k++) mat[i][k] = mat[i][j];
                    name = mat[i][j];
                } else if (name) {
                    mat[i][j] = name;
                }
                j++;
            }
        }

        for (int j = 0; j < c; j++) {
            char name = 0;
            int i = 0;

            while (i < r) {
                if (mat[i][j] != '?') {
                    if (!name) for (int k = 0; k < i; k++) mat[k][j] = mat[i][j];
                    name = mat[i][j];
                } else if (name) {
                    mat[i][j] = name;
                }
                i++;
            }
        }

        printf("Case #%d:\n", tc++);
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                printf("%c", mat[i][j]);
            }
            printf("\n");
        }
    }

    return 0;
}

/*
? ? ?
C C D
A B B
*/
