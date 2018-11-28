#include<cstdio>
#include<cmath>
#include<algorithm>

#define PI 3.14159265358979323846

using namespace std;


typedef struct {
    int index;
    long long int r;
    long long int h;
    long long int side;
    long long int top;
} PANCAKE;

long long int solve(PANCAKE* sorted_pancake, PANCAKE* pancake, int index, int n, int k) {
    long long int sum = 0;
    int cnt = k-1;
    int i = 0;
    int select = 0;
    while(cnt && i < n){
        if(index == sorted_pancake[i].index || sorted_pancake[i].r > pancake[index].r) {
            i++;
            continue;
        }
        select++;
        sum += sorted_pancake[i].side;
        i++;
        cnt--;
    }
    if(select < k-1) return 0;
    return sum + pancake[index].top + pancake[index].side;
}

bool cmp(PANCAKE lhs, PANCAKE rhs) {
    return lhs.side > rhs.side;
}

int main() {
    int T;
    int N;
    int K;
    PANCAKE pancake[1024];
    PANCAKE sorted_pancake[1024];
    scanf("%d", &T);
    int tmpr;
    int tmph;
    int cnt = 0;
    while(T--) {
        scanf("%d%d", &N, &K);
        long long int ans = 0;
        for(int i = 0; i < N; ++i) {
            scanf("%d%d", &tmpr, &tmph);
            sorted_pancake[i].index = pancake[i].index = i;
            sorted_pancake[i].r = pancake[i].r = (long long int)tmpr;
            sorted_pancake[i].h = pancake[i].h = (long long int)tmph;
            sorted_pancake[i].side = pancake[i].side = (long long int)2*tmpr*tmph;
            sorted_pancake[i].top = pancake[i].top = (long long int)tmpr*tmpr;
        }

        sort(sorted_pancake, sorted_pancake+N, cmp);

        for(int i = 0; i < N; ++i) {
            ans = max(ans, solve(sorted_pancake, pancake, i, N, K));
        }
        printf("Case #%d: %.10f\n", ++cnt, double(ans) * PI);
    }
}
