#include<cstdio>

using namespace std;


// for qsort
/*
int compare(int *t, int *s) {
    return *t - *s;
}
*/

int N;
int P;
int mods[4];

void solve() {
    int result = mods[0]; // 最初に割り当てれば常に新鮮なものを食べられる
    if(P == 2) {
        printf("%d\n", result + (mods[1]+1)/2);
    }
    else if(P == 3) {
        int rest;
        if(mods[1] < mods[2]) {
            result += mods[1];
            rest = mods[2] - mods[1];
        }
        else {
            result += mods[2];
            rest = mods[1] - mods[2];
        }
        result += (rest+2)/3;
        printf("%d\n", result);
    }
    else { // P = 4
        result += mods[2]/2; // 余りがあるかに注意
        int rest;
        if(mods[1] < mods[3]) {
            result += mods[1];
            rest = mods[3]-mods[1];
        }
        else {
            result += mods[3];
            rest = mods[1]-mods[3];
        }
        result += rest/4;
        if(rest%4 == 3 && mods[2] % 2 == 1) {
            result += 2; // 2組うまく作れる 2 1 1 1とか2 3 3 3とかで（最初と最後が揃う）
        }
        else if(rest%4 != 0 || mods[2]%2 != 0) result += 1; // どっちか残ってるなら使う
        printf("%d\n", result);
    }
}

void solve_and_print() {
    scanf("%d %d", &N, &P);
    for(int i = 0; i < P; ++i) {
        mods[i] = 0;
    }
    for(int i = 0; i < N; ++i) {
        int t;
        scanf("%d", &t);
        mods[t%P]++;
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
