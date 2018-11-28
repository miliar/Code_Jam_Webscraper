#include <cstdio>
#include <iostream>

using namespace std;

int N;
int R, O, Y, G, B, V;
bool rflag, yflag, bflag;
void printR();
void printY();
void printB();

void print() {
    if(R >= Y && R >= B) {
        if (G > 0) { /// print G
            for(int i = 0; i < G; ++i)
                printf("RG");
            printf("R");
            G = 0;
        }
        else {
            printf("R");
        }
        --R;
    }
    else if (Y >= R && Y >= B) {
        if (V > 0) { /// print G
            for(int i = 0; i < V; ++i)
                printf("YV");
            printf("Y");
            V = 0;
        }
        else {
            printf("Y");
        }
        --Y;
    }
    else if (B >= R && B >= Y) { /// ?
        if (O > 0) { /// print O
            for(int i = 0; i < O; ++i)
                printf("BO");
            printf("B");
            O = 0;
        }
        else {
            printf("B");
        }
        --B;
    }
}

bool check() {
    if (!R && !O && !Y && !G && !B && !V) return true;
    return false;
}

void printR() {
    if (check() == true) return;
    if (G > 0) { /// print G
        for(int i = 0; i < G; ++i)
            printf("RG");
        printf("R");
        G = 0;
    }
    else {
        printf("R");
    }
    --R;
    if (Y > B || (Y == B && bflag == false)) printY();
    else printB();
}

void printY() {
    if (check() == true) return;
    if (V > 0) { /// print G
        for(int i = 0; i < V; ++i)
            printf("YV");
        printf("Y");
        V = 0;
    }
    else {
        printf("Y");
    }
    --Y;
    if (R > B || (R == B && bflag == false)) printR();
    else printB();
}

void printB() {
    if (check() == true) return;
    if (O > 0) { /// print G
        for(int i = 0; i < O; ++i)
            printf("BO");
        printf("B");
        O = 0;
    }
    else {
        printf("B");
    }
    --B;
    if (R > Y || (R == Y && yflag == false)) printR();
    else printY();
}


bool solve() {
    rflag = yflag = bflag = false;
    scanf("%d",&N);
    scanf("%d%d%d%d%d%d",&R,&O,&Y,&G,&B,&V);
    if (R < G || Y < V || B < O) return false;
    if (R == G && R != 0) {
        if (N != R+G) return false;
        for(int i = 0; i < G; ++i)
            printf("RG");
        return true;
    }
    if (Y == V && Y != 0) {
        if (N != Y+V) return false;
        for(int i = 0; i < V; ++i)
            printf("YV");
        return true;
    }
    if (B == O && B != 0) {
        if (N != B+O) return false;
        for(int i = 0; i < O; ++i)
            printf("BO");
        return true;
    }
    R = R-G; Y = Y-V; B = B-O;
    //printf("%d %d %d\n\n",R,Y,B);
    //system("pause");
    if(R > Y+B || Y > B+R || B > R+Y) return false;
    if (R >= B && R >= Y) {
        rflag = true;
        printR();
    }
    else if (Y >= R && Y >= B) {
        yflag = true;
        printY();
    }
    else {
        bflag = true;
        printB(); ///
    }
    return true;
}


int main() {
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int test;
    scanf("%d",&test);
    for (int t = 1; t <= test; ++t) {
        printf("Case #%d: ",t);
        if (solve() == false)
            printf("IMPOSSIBLE");
        printf("\n");
    }
    return 0;
}
