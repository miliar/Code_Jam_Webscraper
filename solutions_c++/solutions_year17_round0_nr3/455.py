#include<cstdio>
#include<cstdlib>
#include<cstring>


using namespace std;


long long N;
long long K;

void solve() {
    if(K == 1) {
        printf("%lld %lld", N/2, (N-1)/2);
        return;
    }
    long long h = 2; // 区切り方の決まっている場合の分割数
    while(h-1 < K) h *= 2;
    h /= 2;
    K -= h-1; // 高さがlog hの木のノード数: 区切り方が決まっている
    N -= h-1; // 使用中の分を消去
    long long width = N / h; // h分割したときの幅の下限
    long long wider = N % h; // 下限より1大きい幅の数
    if(wider < K) {
        printf("%lld %lld", width/2, (width-1)/2);
    }
    else {
        printf("%lld %lld", (width+1)/2, width/2);
    }
}

void solve_and_print() {
    scanf("%lld%lld", &N, &K);
    solve();
    printf("\n");
}


int main() {
    int dataset_num, case_num;
    char pass[10];

    scanf("%d", &dataset_num);
    gets(pass);
    for(case_num = 1; case_num <= dataset_num; ++case_num) {
        printf("Case #%d: ", case_num);

        solve_and_print();
    }

    return 0;
}
