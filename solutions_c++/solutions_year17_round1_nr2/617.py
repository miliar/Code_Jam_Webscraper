#include<cstdio>
#include<cstdlib>

using namespace std;


int N, P;

int R[50];
int Q[50][50];
int least[50][50];
int greatest[50][50];
double frac[50][50];


int compare(const void *t, const void *s) {
    return *(const int *)t - *(const int *)s;
}

// i番目の材料の重さqは最大何個分？
int greatest_number_of_rata(int i, int q) {
    return (q*100)/(R[i]*90); // 最小時の必要量で割った
}

int least_number_of_rata(int i, int q) {
    return (q*100+R[i]*110-1)/(R[i]*110); // 最大時の必要量で割った（材料が残ってはいけない）
}


int solve() {
    int num = 0;
    int point[50];
    for(int i = 0; i < N; ++i) {
        qsort(Q[i], P, sizeof(int), compare);
    }
    for(int i = 0; i < N; ++i) {
        point[i] = 0;
    }
    for(int i = 0; i < N; ++i) {
        for(int j = 0; j < P; ++j) {
            least[i][j] = least_number_of_rata(i, Q[i][j]);
            greatest[i][j] = greatest_number_of_rata(i, Q[i][j]);
            frac[i][j] = (double)Q[i][j]/(double)R[i];
        }
    }
    int check = 1;
    while(check) {
        int lt = least[0][point[0]];
        for(int i = 1; i < N; ++i) {
            int lt_i = least[i][point[i]];
            if(lt < lt_i) lt = lt_i;
        }

        int gt = greatest[0][point[0]];
        for(int i = 1; i < N; ++i) {
            int gt_i = greatest[i][point[i]];
            if(gt > gt_i) gt = gt_i;
        }
        if(gt < lt) {
            for(int i = 0; i < N; ++i) {
                while(greatest[i][point[i]] < lt && point[i] < P) ++point[i];
                if(point[i] == P) { // 材料の関係上これ以上作れない
                    check = 0;
                    break;
                }
            }
            continue;
        }

        for(int i = 0; i < N; ++i) {
            if(++point[i] == P) check = 0;
        }
        ++num;
    }
    return num;
}

void solve_and_print() {
    scanf("%d %d", &N, &P);
    for(int i = 0; i < N; ++i) {
        scanf("%d", R+i);
    }
    for(int i = 0; i < N; ++i) {
        for(int j = 0; j < P; ++j) {
            scanf("%d", &Q[i][j]);
        }
    }
    printf("%d\n", solve());
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
