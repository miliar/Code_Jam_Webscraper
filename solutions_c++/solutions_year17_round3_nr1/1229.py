#include <stdio.h>
#include <utility>
#include <algorithm>

#define MAXN 1000
#define pld pair<long long, int>

using namespace std;

int main() {
    int T, N, K;
    long long R[MAXN], H[MAXN], S[MAXN];
    pld rs[MAXN], ss[MAXN];
    long long sum;
    long long maxi;
    bool che[MAXN];
    long long mr;
    int i, j;
    
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    scanf("%d", &T);
    for(i = 0; i < T; i++) {
        scanf("%d %d", &N, &K);
        for(j = 0; j < N; j++) scanf("%lld %lld", &R[j], &H[j]);
        for(j = 0; j < N; j++) S[j] = 2 * R[j] * H[j];
        for(j = 0; j < N; j++) {
            rs[j].first = R[j];
            ss[j].first = S[j];
            rs[j].second = ss[j].second = j;
        }
        sort(rs, rs + N);
        sort(ss, ss + N);
        for(j = 0; j < N; j++) che[j] = false;
        sum = 0;
        mr = 0;
        for(j = 0; j < K - 1; j++) {
            che[ss[N - j - 1].second] = true;
            sum += ss[N - j - 1].first;
            if(R[ss[N - j - 1].second] > mr) mr = R[ss[N - j - 1].second];
        }
        if(R[ss[N - K].second] > mr) maxi = R[ss[N - K].second] * R[ss[N - K].second] + ss[N - K].first;
        else maxi = mr * mr + ss[N - K].first;
        for(j = 0; j < N; j++) if(!che[j] && R[j] * R[j] + S[j] > maxi && R[j] >= mr) maxi = R[j] * R[j] + S[j];
        printf("Case #%d: %Lf\n", i + 1, (long double)(sum + maxi) * 3.14159265358979);
    }
    return 0;
}
