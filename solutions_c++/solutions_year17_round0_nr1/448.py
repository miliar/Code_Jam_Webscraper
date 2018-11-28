#include<cstdio>

using namespace std;


int K;
int S;
char set[1000];


void solve() {
    int n = 0;
    for(int i = 0; i <= S-K; ++i) {
        if(set[i] != '+') {
            ++n;
            for(int j = 0; j < K; ++j) {
                if(set[i+j] == '+') {
                    set[i+j] = '-';
                }
                else {
                    set[i+j] = '+';
                }
            }
        }
    }
    for(int i = 0; i < S; ++i) {
        if(set[i] != '+') {
            printf("IMPOSSIBLE");
            return;
        }
    }
    printf("%d", n);
}

void solve_and_print() {
    int c;
    gets(set);
    S = 0;
    while((c = getchar()) == '-' || c == '+') {
        set[S] = c;
        ++S;
    }
    scanf("%d", &K);
    solve();
    // something to print answer
    printf("\n");
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
