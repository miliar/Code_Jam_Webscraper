#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>
#include <unordered_map>

#pragma warning(disable:4996)

using namespace std;



unordered_map<short, unordered_map<short, unordered_map<short, char>>> data_map[3][3];

bool solve(short p1, short p2, short r, short y, short b) {
    char& cache = data_map[p1][p2][r][y][b];
    if (cache == -1) return false;
    else if (cache == 0) {
        if (p1 != 0 && r > 0 && solve(0, p2, r - 1, y, b)) {
            data_map[p1][p2][r][y][b] = 'R';
            return true;
        }
        if (p1 != 1 && y > 0 && solve(1, p2, r, y - 1, b)) {
            data_map[p1][p2][r][y][b] = 'Y';
            return true;
        }
        if (p1 != 2 && b > 0 && solve(2, p2, r, y, b - 1)) {
            data_map[p1][p2][r][y][b] = 'B';
            return true;
        }
        data_map[p1][p2][r][y][b] = -1;
        return false;
    }
    else return true;
}

void pchar(short c, int& insert) {
    if (c == 0) {
        printf("R");
        for (int i = 0; i < insert; i++) {
            printf("GR");
        }
    }
    if (c == 1) {
        printf("Y");
        for (int i = 0; i < insert; i++) {
            printf("VY");
        }
    }
    if (c == 2) {
        printf("B");
        for (int i = 0; i < insert; i++) {
            printf("OB");
        }
    }
    insert = 0;
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("test.out", "w", stdout);

    int T;
    scanf("%d", &T);

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (i != 2 && j != 2)
                data_map[i][j][0][0][1] = 'B';
            else
                data_map[i][j][0][0][1] = -1;
            
            if (i != 1 && j != 1)
                data_map[i][j][0][1][0] = 'Y';
            else
                data_map[i][j][0][1][0] = -1;

            if (i != 0 && j != 0)
                data_map[i][j][1][0][0] = 'R';
            else
                data_map[i][j][1][0][0] = -1;
        }
    }

    int insert[3];

    for (int t = 1; t <= T; t++) {
        int RYB[3];
        int GVO[3];
        int N;
        insert[0] = insert[1] = insert[2] = 0;

        scanf("%d %d %d %d %d %d %d", &N, &RYB[0], &GVO[2], &RYB[1], &GVO[0], &RYB[2], &GVO[1]);

        printf("Case #%d: ", t);

        if (RYB[0] == GVO[0] && RYB[1] == GVO[1] && RYB[2] == GVO[2]) {
           if (GVO[0] > 0 && GVO[1] == 0 && GVO[2] == 0) {
               for (int i = 0; i < GVO[0]; i++)
                   printf("RG");
            }
            else if (GVO[0] == 0 && GVO[1] > 0 && GVO[2] == 0) {
                for (int i = 0; i < GVO[1]; i++)
                    printf("YV");
            }
            else if (GVO[0] == 0 && GVO[1] == 0 && GVO[2] > 0) {
                for (int i = 0; i < GVO[2]; i++)
                    printf("BO");
            }
            else {
                printf("IMPOSSIBLE");
            }
            printf("\n");
            continue;
        }

        if (GVO[0] > 0) {
            if (RYB[0] <= GVO[0]) {
                printf("IMPOSSIBLE\n");
                continue;
            }
            else { 
                RYB[0] -= GVO[0];
                N -= 2 * GVO[0];
                insert[0] = GVO[0];
            }
        }
        if (GVO[1] > 0) {
            if (RYB[1] <= GVO[1]) {
                printf("IMPOSSIBLE\n");
                continue;
            }
            else {
                RYB[1] -= GVO[1];
                N -= 2 * GVO[1];
                insert[1] = GVO[1];
            }
        }
        if (GVO[2] > 0) {
            if (RYB[2] <= GVO[2]) {
                printf("IMPOSSIBLE\n");
                continue;
            }
            else {
                RYB[2] -= GVO[2];
                N -= 2 * GVO[2];
                insert[2] = GVO[2];
            }
        }

        
        if (RYB[0] > 0) {
            bool ans = solve(0, 0, --RYB[0], RYB[1], RYB[2]);
            if (!ans) {
                printf("IMPOSSIBLE\n");
            }
            else {
                // printf("R");
                pchar(0, insert[0]);
                int now = 0;
                for (int i = 1; i < N; i++) {
                    char next = data_map[now][0][RYB[0]][RYB[1]][RYB[2]];
                    // printf("%c", next);
                    if (next == 'R') now = 0;
                    else if (next == 'Y') now = 1;
                    else if (next == 'B') now = 2;
                    pchar(now, insert[now]);
                    RYB[now]--;
                }
                printf("\n");
            }
        }
        else if (RYB[1] > 0) {
            bool ans = solve(1, 1, RYB[0], --RYB[1], RYB[2]);
            if (!ans) {
                printf("IMPOSSIBLE\n");
            }
            else {
                // printf("Y");
                pchar(1, insert[1]);
                int now = 1;
                for (int i = 1; i < N; i++) {
                    char next = data_map[now][1][RYB[0]][RYB[1]][RYB[2]];
                    // printf("%c", next);
                   // pchar(next, insert[next]);
                    if (next == 'R') now = 0;
                    else if (next == 'Y') now = 1;
                    else if (next == 'B') now = 2;
                    pchar(now, insert[now]);
                    RYB[now]--;
                }
                printf("\n");
            }
        }
        else {
            bool ans = solve(2, 2, RYB[0], RYB[1], --RYB[2]);
            if (!ans) {
                printf("IMPOSSIBLE\n");
            }
            else {
                // printf("B");
                pchar(2, insert[2]);
                int now = 2;
                for (int i = 1; i < N; i++) {
                    char next = data_map[now][2][RYB[0]][RYB[1]][RYB[2]];
                    // printf("%c", next);
                   //  pchar(next, insert[next]);
                    if (next == 'R') now = 0;
                    else if (next == 'Y') now = 1;
                    else if (next == 'B') now = 2;
                    pchar(now, insert[now]);
                    RYB[now]--;
                }
                printf("\n");
            }
        }

    }

    return 0;
}
