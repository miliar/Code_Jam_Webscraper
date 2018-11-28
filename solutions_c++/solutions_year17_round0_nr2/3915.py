#include<iostream>
#include<cstring>
#include<cstdio>

using namespace std;

int T,N;
long long X;

int ndigit(long long x) {
    int n = 0;
    while (x) {
        ++n;
        x /= 10;
    }
    return n;
}

int main() {
    scanf("%d",&T);
    for (int l=1;l<=T;++l) {
        scanf("%I64d",&X);
        int N = ndigit(X);
        
        long long ans = 0;
        for (int i=0;i<N;++i) {
            bool flag = false;
            for (int j=9;j>-1;--j) {
                long long coba = ans;
                for (int k=1;k<=N-i;++k) coba = coba*10 + j;
                
                if (coba <= X) {
                    flag = true;
                    ans = 10*ans + j;
                    break;
                }
            }
            if (!flag) {
                ans = 0;
                for (int j=1;j<N;++j) ans = 10*ans + 9;
                break;
            }
        }
        
        printf("Case #%d: %I64d\n",l,ans);
    }
    return 0;
}
