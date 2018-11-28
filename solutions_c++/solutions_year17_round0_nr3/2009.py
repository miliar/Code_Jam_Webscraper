#include <cstdio>

int main(){
    //freopen("C-large.in", "r", stdin);
    //freopen("C-large.out", "w", stdout);
    int T;
    long long N, K;
    long long occupied, groups;
    scanf("%d", &T);

    for(int t = 1; t <= T; t++){
        scanf("%lld%lld", &N, &K);

        occupied = 0;
        groups = 1;

        while((occupied << 1) + 1 < K){
            occupied = (occupied << 1) + 1;
            groups <<= 1;
        }

        long long groupPos = K - occupied;
        long long groupSize = (N - occupied) / groups;
        if(N - occupied - groups*groupSize >= groupPos) groupSize++;

        /*
        printf("occupied = %lld\n", occupied);
        printf("groups = %lld\n", groups);
        printf("groupPos = %lld\n", groupPos);
        printf("groupSize = %lld\n", groupSize);
        //*/

        printf("Case #%d: %lld %lld\n", t, groupSize/2, (groupSize-1)/2);
    }
}
