#include <cstdio>
#include <string>
using namespace std;


int N;
int R, O, Y, G, B, V;


void print(char a) {
    if (a == 'B') {
        for (int i = 0; i < O; i ++) {
            printf("BO");
        }
        O = 0;
    }
    if (a == 'R') {
        for (int i = 0; i < G; i ++) {
            printf("RG");
        }
        G = 0;
    }
    if (a == 'Y') {
        for (int i = 0; i < V; i ++) {
            printf("YV");
        }
        V = 0;
    }

    printf("%c", a);
}

void dfs(int x, int y, int z, char a, char b, char c) {
    if (x == 0 && y == 0 && z == 0) {
        return;
    }
    if (x == y + z) {
        if (y > 0) {
            print(a);
            print(b);
            dfs(x - 1, y - 1, z, a, b, c);
        } else {
            print(a);
            print(c);
            dfs(x - 1, y, z - 1, a, b, c);
        }
        return;
    }

    if (x > 0) {
        print(a);
        x --;
    }
    if (y > 0) {
        print(b);
        y --;
    }
    if (z > 0) {
        print(c);
        z --;
    }
    dfs(x, y, z, a, b, c);
}

void process() {
    if (R > N / 2 || O > N / 2 || Y > N / 2 || G > N / 2 || B > N / 2 || V > N / 2) {
        printf("IMPOSSIBLE\n");
        return;
    }
    if (O > B || G > R || V > Y) {
        printf("IMPOSSIBLE\n");
        return;
    }

    if (B + O == N) {
        for (int i = 0; i < B; i ++) {
            printf("BO");
        }
    } else if (G + R == N) {
        for (int i = 0; i < R; i ++) {
            printf("RG");
        }
    } else if (V + Y == N) {
        for (int i = 0; i < Y; i ++) {
            printf("YV");
        }
    } else {
        if ((O > 0 && O == B) || (G > 0 && G == R) || (V > 0 && V == Y)) {
            printf("IMPOSSIBLE\n");
            return;
        }

        B -= O;
        R -= G;
        Y -= V;

        if (R > (R + Y + B) / 2 || Y > (R + Y + B) / 2 || B > (R + Y + B) / 2) {
            printf("IMPOSSIBLE\n");
            return;
        }

        if (R >= Y && R >= B) {
            dfs(R, Y, B, 'R', 'Y', 'B');
        } else if (Y >= R && Y >= B) {
            dfs(Y, R, B, 'Y', 'R', 'B');
        } else if (B >= R && B >= Y) {
            dfs(B, R, Y, 'B', 'R', 'Y');
        }
    }
    printf("\n");
}

int main() {
    int T;
    scanf("%d", &T);

    for (int test = 1; test <= T; test ++) {
        scanf("%d %d %d %d %d %d %d", &N, &R, &O, &Y, &G, &B, &V);
        
        printf("Case #%d: ", test);
        process();
    }
    return 0;
}
