#include<cstdio>
#include<cstdlib>
#include<cstring>

#include<vector>
#include<map>
#include<string>

using namespace std;


int N;
int M;

char stage[100][100];

int num;
int xs[10000];
int ys[10000];
int models[10000];


// ˆá”½‚Í‚µ‚Ä‚¢‚È‚¢‚Æ‚·‚éB
int point() {
    int p = 0;
    for(int i = 0; i < N; ++i) {
        for(int j = 0; j < N; ++j) {
            if(stage[i][j] == 'o') p += 2;
            else if(stage[i][j] == 'x' || stage[i][j] == '+') ++p;
        }
    }
    return p;
}


void set_model(char m, int x, int y) {
    stage[x][y] = models[num] = m;
    xs[num] = x; ys[num] = y;
    ++num;
}

void print_stage(int p) {
    printf("point: %d\n", p);
    for(int i = 0; i < N; ++i) {
        for(int j = 0; j < N; ++j) {
            putchar(stage[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}


void solve() {
    int circle = 0;
    // ‚·‚²‚¢l‚ğ’u‚­êŠ‚ğŒˆ‚ß‚é
    for(int i = 0; i < N; ++i) {
        if(stage[0][i] == 'x') {
            circle = i;
        }
        if(stage[0][i] == 'o') {
            circle = -1;
        }
        if(stage[0][i] == '.') {

        }
    }
    for(int i = 0; i < N; ++i) {
        if(i == circle) set_model('o', 0, i);
        else if(stage[0][i] == '.') set_model('+', 0, i);
        else if(stage[0][i] == 'o') circle = i;
    }
    for(int i = 1; i < N-1; ++i) {
        set_model('+', N-1, i);
    }
    if(circle != N-1) {
        for(int i = 1; i < N; ++i) {
            if(i-1 < circle) set_model('x', i, i-1);
            else set_model('x', i, i);
        }
    }
    else {
        for(int i = 1; i < N; ++i) {
            set_model('x', i, N-i-1);
        }
    }

    printf("%d %d\n", point(), num);
    for(int i = 0; i < num; ++i) {
        printf("%c %d %d\n", models[i], xs[i]+1, ys[i]+1);
    }

    //print_stage(point());
}

void solve_and_print() {
    for(int i = 0; i < 100; ++i) {
        for(int j = 0; j < 100; ++j) {
            stage[i][j] = '.';
        }
    }
    char line[20];
    scanf("%d%d", &N, &M);
    num = 0;
    gets(line);
    for(int i = 0; i < M; ++i) {
        gets(line);
        int x, y;
        sscanf(line+1, "%d%d", &x, &y);
        stage[x-1][y-1] = line[0];
    }
    solve();
}


int main() {
    int dataset_num, case_num;

    scanf("%d", &dataset_num);
    for(case_num = 1; case_num <= dataset_num; ++case_num) {
        printf("Case #%d: ", case_num);

        solve_and_print();
    }

    return 0;
}
