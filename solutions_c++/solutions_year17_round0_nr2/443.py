#include<cstdio>
#include<cctype>


using namespace std;

char N[30];

int check(int magn) {
    int d = 0;
    for(int i = 0; i < magn; ++i) {
        if(d <= N[i]) {
            d = N[i];
        }
        else {
            return 0;
        }
    }
    return 1;
}

void solve() {
    int magn;
    for(magn = 0; magn < 30; ++magn) {
        if(!isdigit(N[magn])) break;
    }
    N[magn] = '\0';

    for(int i = magn-1; !check(magn) && i > 0; --i) {
        N[i] = '9';
        N[i-1]--;
    }
    if(N[0] == '0') {
        printf("%s\n", N+1);
    }
    else {
        printf("%s\n", N);
    }
}

void solve_and_print() {
    gets(N);
    solve();
}


int main() {
    int dataset_num, case_num;

    scanf("%d", &dataset_num);
    gets(N);
    for(case_num = 1; case_num <= dataset_num; ++case_num) {
        printf("Case #%d: ", case_num);

        solve_and_print();
    }

    return 0;
}
