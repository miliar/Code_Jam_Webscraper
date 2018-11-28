#include <cstdio>
#include <iostream>
#include <map>
using namespace std;

string create(char A, char B, char C, int a, int b, int c) {
    int r = c + b - a;
    string s = "";
    for (int i = 0; i < r; i++) {
        s += A;
        s += B;
        s += C;
    }
    for (int i = r; i < b; i++) {
        s += A;
        s += B;
    }
    for (int i = b; i < a; i++) {
        s += A;
        s += C;
    }
    return s;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ca++) {
        int N, R, O, Y, G, B, V;
        scanf("%d%d%d%d%d%d%d", &N, &R, &O, &Y, &G, &B, &V);
        if (R + Y < B || R + B < Y || B + Y < R) {
            printf("Case #%d: IMPOSSIBLE\n", ca);
        } else {
            string s;
            if (R >= Y && Y >= B)
                s = create('R', 'Y', 'B', R, Y, B);
            else if (R >= B && B >= Y)
                s = create('R', 'B', 'Y', R, B, Y);
            else if (Y >= R && R >= B)
                s = create('Y', 'R', 'B', Y, R, B);
            else if (Y >= B && B >= R)
                s = create('Y', 'B', 'R', Y, B, R);
            else if (B >= R && R >= Y)
                s = create('B', 'R', 'Y', B, R, Y);
            else if (B >= Y && Y >= R)
                s = create('B', 'Y', 'R', B, Y, R);
            cout << "Case #" << ca << ": " << s << endl;
        }
    }
    return 0;
}