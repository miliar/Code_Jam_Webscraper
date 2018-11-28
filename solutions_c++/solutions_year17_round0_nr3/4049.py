#include<iostream>
#include<cstring>
#include<cstdio>

using namespace std;

long long pangkat[70],N,K;
int T;

int main() {
    pangkat[0] = 0;
    for (int i=1;i<=62;++i) pangkat[i] = 2LL*pangkat[i-1] + 1LL;

    scanf("%d",&T);
    for (int l=1;l<=T;++l) {
        scanf("%I64d %I64d",&N,&K);
        int pakai = 0;
        
        while (pangkat[pakai] < K) ++pakai;
        --pakai;
        
        long long ukur = (N-pangkat[pakai]) / (pangkat[pakai]+1LL);
        long long sisa = (N-pangkat[pakai]) % (pangkat[pakai]+1LL);
        
        if (sisa > 0 && K-pangkat[pakai] <= sisa) ++ukur;
        --ukur;
        printf("Case #%d: %I64d %I64d\n",l,(ukur+1LL)/2LL,ukur/2LL);
    }
    return 0;
}
