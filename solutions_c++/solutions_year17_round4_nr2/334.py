#include<cstdio>
#include<cstdlib>
#include<cstring>

#include<vector>
#include<map>
#include<string>

using namespace std;


// for qsort
/*
int compare(int *t, int *s) {
    return *t - *s;
}
*/

int N;
int C;
int M;
int P[1000];
int B[1000];
int rides;
int proms;
// for small
int Ps[1000];
int nums[1000];

void solve() {
    for(int i = 0; i < N; ++i) {
        Ps[i] = 0;
    }
    for(int i = 0; i < C; ++i) {
        nums[i] = 0;
    }
    for(int i = 0; i < M; ++i) {
        nums[B[i]]++;
        Ps[P[i]]++;
    }
    // 最低、最大の所持数の人の回数回す
    for(int i = 0; i < C; ++i) {
        if(rides < nums[i]) rides = nums[i];
    }
    int fronts = 0;
    for(int i = 0; i < N; ++i) {
        fronts += Ps[i]; // i番目までで乗る数
        // 乗る人数が回す回数の許容より多いと更新
        if(rides * (i+1) < fronts) rides = (fronts+i)/(i+1); // 切り上げ
    }
    for(int i = N-1; i >= 0; --i) {
        if(Ps[i] > rides) {
            proms += Ps[i] - rides;
        }
    }
}

void solve_and_print() {
    scanf("%d %d %d", &N, &C, &M);
    for(int i = 0; i < M; ++i) {
        scanf("%d %d", P+i, B+i);
        P[i]--; B[i]--;
    }
    rides = 0;
    proms = 0;
    solve();
    // something to print answer
    printf("%d %d\n", rides, proms);
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
